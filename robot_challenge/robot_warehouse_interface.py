from abc import abstractmethod, ABC

from robot_challenge.location import Location


class RobotWarehouseInterface(ABC):
    @abstractmethod
    def check_crate_at_location(self, location: Location) -> bool:
        pass

    @abstractmethod
    def take_crate_at_location(self, location: Location):
        pass

    @abstractmethod
    def create_crate_at_location(self, location: Location):
        pass

    @abstractmethod
    def change_location_to_be_in_boundaries(self, location: Location) -> Location:
        pass