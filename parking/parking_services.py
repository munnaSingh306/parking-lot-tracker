import re
from parking.constants import (VEHICLE_NOT_PARKED_YET,
                               INVALID_VEHICLE_NUMBER,
                               INVALID_CHOICE)
from parking.parking import Parking


def initial_prompt() -> str:
    print("\n")
    print("*" * 30)
    print(" 1. Park a vehicle")
    print(" 2. Retrieve a vehicle")
    print(" 3. Exit")
    print("*" * 30)

    choice = input("Enter your choice: ")
    return choice


def is_valid_vehicle_number(vehicle_number: str) -> bool:
    valid_vehicle_number_regex = r'^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$'
    is_valid = False
    if not vehicle_number:
        return is_valid
    vehicle_number = vehicle_number.replace(" ", "")
    if not re.match(valid_vehicle_number_regex, vehicle_number, re.IGNORECASE):
        return is_valid
    is_valid = True
    return is_valid


def input_prompt() -> str:
    vehicle_number = input("Enter the vehicle number:")
    if not is_valid_vehicle_number(vehicle_number=vehicle_number):
        print(INVALID_VEHICLE_NUMBER)
        return input_prompt()
    return vehicle_number


def parking_service():
    vehicle_parker = Parking()
    while True:
        choice = initial_prompt()
        if choice == "1":
            vehicle_number = input_prompt()
            parking_details = vehicle_parker.park(vehicle_number=vehicle_number)
            print(parking_details)

        elif choice == "2":
            vehicle_number = input_prompt()
            parked_spot = vehicle_parker.retrieve_parked_vehicle(vehicle_number=vehicle_number)
            print(parked_spot) if parked_spot else print(VEHICLE_NOT_PARKED_YET % vehicle_number)

        elif choice == "3":
            break

        else:
            print(INVALID_CHOICE)
