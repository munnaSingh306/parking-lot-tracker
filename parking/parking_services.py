from parking.constants import VEHICLE_NOT_PARKED_YET
from parking.parking import Parking


def parking_service():

    vehicle_parker = Parking()
    while True:
        print("\n")
        print("*" * 30)
        print(" 1. Park a vehicle")
        print(" 2. Retrieve a vehicle")
        print(" 3. Exit")
        print("*" * 30)

        choice = input("Enter your choice: ")
        if choice == "1":
            vehicle_number = input("Enter the vehicle number: ")
            parking_details = vehicle_parker.park(vehicle_number=vehicle_number)
            print(parking_details)

        elif choice == "2":
            vehicle_number = input("Enter the vehicle number: ")
            parked_spot = vehicle_parker.retrieve_parked_vehicle(vehicle_number=vehicle_number)
            print(parked_spot) if parked_spot else print(VEHICLE_NOT_PARKED_YET % vehicle_number)

        elif choice == "3":
            break

        else:
            print("Please enter a valid option. Like 1, 2 or 3")
