from parking.constants import (TOTAL_PARKING_LOTS,
                               PER_LEVEL_TOTAL_SLOTS,
                               VEHICLE_ALREADY_PARKED,
                               VEHICLE_PARKED_SUCCESSFULLY,
                               PARKING_LOT_IS_FULL)


class ParkingLot:
    def __init__(self):
        self.parking_spots = [None] * TOTAL_PARKING_LOTS

    def get_parking_level_and_spot(self, parking_spot_index: int) -> dict:

        parking_level = "A" if parking_spot_index < PER_LEVEL_TOTAL_SLOTS else "B"
        parking_spot = parking_spot_index % PER_LEVEL_TOTAL_SLOTS + 1
        return {"level": parking_level, "spot": parking_spot}

    def assign_spot(self, vehicle_number: str) -> str:

        for i, spot in enumerate(self.parking_spots):
            if spot is None and vehicle_number not in self.parking_spots:
                self.parking_spots[i] = vehicle_number
                return VEHICLE_PARKED_SUCCESSFULLY % vehicle_number

            elif vehicle_number in self.parking_spots:
                return VEHICLE_ALREADY_PARKED % vehicle_number

        return PARKING_LOT_IS_FULL

    def get_parked_spot(self, vehicle_number: str) -> dict:
        for i, spot in enumerate(self.parking_spots):
            if spot == vehicle_number:
                parking_details = self.get_parking_level_and_spot(parking_spot_index=i)
                return parking_details
        return {}
