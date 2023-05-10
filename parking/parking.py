from parking.constants import (TOTAL_PARKING_LOTS,
                               PER_LEVEL_TOTAL_SLOTS,
                               VEHICLE_ALREADY_PARKED,
                               VEHICLE_PARKED_SUCCESSFULLY,
                               PARKING_LOT_IS_FULL)


class ParkingLot:
    def __init__(self):
        self.available_spots = set(range(TOTAL_PARKING_LOTS))
        self.vehicle_spots = {}

    def assign_spot(self, vehicle_number: str) -> str:
        if vehicle_number in self.vehicle_spots:
            return VEHICLE_ALREADY_PARKED % vehicle_number

        if not self.available_spots:
            return PARKING_LOT_IS_FULL

        parking_spot = self.available_spots.pop()
        self.vehicle_spots[vehicle_number] = parking_spot
        return VEHICLE_PARKED_SUCCESSFULLY % vehicle_number

    def get_parked_spot(self, vehicle_number: str) -> dict:
        if vehicle_number in self.vehicle_spots:
            parking_spot = self.vehicle_spots.get(vehicle_number)
            if parking_spot is None:
                return {}
            parking_level = "A" if parking_spot < PER_LEVEL_TOTAL_SLOTS else "B"
            parking_spot = parking_spot % PER_LEVEL_TOTAL_SLOTS + 1
            return {"level": parking_level, "spot": parking_spot}
        return {}


class Parking:
    def __init__(self):
        self._parking_lot = None

    @property
    def parking_lot(self) -> ParkingLot:
        if self._parking_lot is None:
            self._parking_lot = ParkingLot()
        return self._parking_lot

    def park(self, vehicle_number: str) -> str:
        parking_status = self.parking_lot.assign_spot(vehicle_number=vehicle_number)
        return parking_status

    def retrieve_parked_vehicle(self, vehicle_number: str) -> dict:
        parking_details = self.parking_lot.get_parked_spot(vehicle_number=vehicle_number)
        return parking_details
