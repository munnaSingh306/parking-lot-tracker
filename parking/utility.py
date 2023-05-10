import re
import sys
from parking.constants import (INVALID_VEHICLE_NUMBER,
                               MAXIMUM_ATTEMPT_ALLOWED,
                               MAXIMUM_ATTEMPT_EXCEEDED)


class Utility:
    prompt_count = 0

    def is_valid_vehicle_number(self, vehicle_number: str) -> bool:
        valid_vehicle_number_regex = r'^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$'
        is_valid = False
        if not vehicle_number:
            return is_valid
        vehicle_number = vehicle_number.replace(" ", "")
        if not re.match(valid_vehicle_number_regex, vehicle_number, re.I):
            return is_valid
        is_valid = True
        return is_valid

    def initial_prompt(self) -> str:
        print("\n")
        print("*" * 30)
        print(" 1. Park a vehicle")
        print(" 2. Retrieve a vehicle")
        print(" 3. Exit")
        print("*" * 30)
        choice = input("Enter your choice: ")
        return choice

    def input_prompt(self) -> str:
        self.prompt_count += 1
        if self.prompt_count > MAXIMUM_ATTEMPT_ALLOWED:
            sys.exit(MAXIMUM_ATTEMPT_EXCEEDED)
        vehicle_number = input("Enter the vehicle number:")
        if not self.is_valid_vehicle_number(vehicle_number=vehicle_number):
            print(INVALID_VEHICLE_NUMBER)
            self.input_prompt()

        self.prompt_count = 0
        vehicle_number = vehicle_number.replace(" ", "")
        return vehicle_number.upper()
