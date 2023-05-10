from parking.constants import (VEHICLE_NOT_PARKED_YET,
                               INVALID_CHOICE)
from parking.parking import Parking
from parking.utility import Utility


def parking_service():
    vehicle_parker = Parking()
    parking_utility = Utility()
    while True:
        choice = parking_utility.initial_prompt()
        if choice == "1":
            vehicle_number = parking_utility.input_prompt()
            parking_details = vehicle_parker.park(vehicle_number=vehicle_number)
            print(parking_details)

        elif choice == "2":
            vehicle_number = parking_utility.input_prompt()
            parked_spot = vehicle_parker.retrieve_parked_vehicle(vehicle_number=vehicle_number)
            print(parked_spot) if parked_spot else print(VEHICLE_NOT_PARKED_YET % vehicle_number)

        elif choice == "3":
            break

        else:
            print(INVALID_CHOICE)
