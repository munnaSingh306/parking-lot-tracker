from parking.parkingLot import ParkingLot


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
