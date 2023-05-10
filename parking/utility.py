import re
import sys
from parking.constants import (INVALID_VEHICLE_NUMBER,
                               MAXIMUM_ATTEMPT_ALLOWED,
                               MAXIMUM_ATTEMPT_EXCEEDED,
                               VEHICLE_NUMBER_PATTERN)


class Utility:
    prompt_count = 0

    def is_valid_vehicle_number(self, vehicle_number: str) -> bool:
        vehicle_number = (vehicle_number or "").replace(" ", "")
        if not (vehicle_number or re.match(VEHICLE_NUMBER_PATTERN, vehicle_number, re.I)):
            return False
        return True

    def initial_prompt(self) -> str:
        print(f"\n{'*' * 30}", " 1. Park a vehicle", " 2. Retrieve a vehicle",
              " 3. Exit", "*" * 30, sep="\n")
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
