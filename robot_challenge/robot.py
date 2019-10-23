from robot_challenge.location import Location
from robot_challenge.robot_direction import RobotDirection
from robot_challenge.robot_warehouse_interface import RobotWarehouseInterface


class Robot:

    def __init__(self, warehouse_calls_in: RobotWarehouseInterface, initial_location: Location):
        self.warehouse_calls = warehouse_calls_in
        self.location = initial_location
        self.has_crate = False
        self.movement_to_location_map = {RobotDirection.NORTH: Location(0, 1),
                                         RobotDirection.SOUTH: Location(0, -1),
                                         RobotDirection.WEST: Location(-1, 0),
                                         RobotDirection.EAST: Location(1, 0)}
        return

    def grab_crate(self):
        # Check the warehouse has a crate at this location.
        if self.warehouse_calls.check_crate_at_location(self.location):
            self.warehouse_calls.take_crate_at_location(self.location)
            self.has_crate = True

    def drop_crate(self):
        if self.warehouse_calls.check_crate_at_location(self.location):
            return

        if self.has_crate == False:
            return

            # Drop the crate spawn one on the warehouse at this location

            pass

        return

    def process_direction(self, robot_command: RobotDirection):
        command_location: Location = self.movement_to_location_map[robot_command]
        self.location += command_location
        self.warehouse_calls.change_location_to_be_in_boundaries(self.location)
