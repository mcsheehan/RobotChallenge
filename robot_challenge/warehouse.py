from typing import List

from robot_challenge.command_parser import CommandParser
from robot_challenge.robot import Robot
from robot_challenge.robot_direction import RobotDirection
from robot_challenge.location import Location
from robot_challenge.robot_warehouse_interface import RobotWarehouseInterface


class Crate:
    def __init__(self, starting_location):
        self.crate_location = starting_location
        self.in_transit = False


class Warehouse(RobotWarehouseInterface):

    def take_crate_at_location(self, location: Location):
        pass

    def create_crate_at_location(self, location: Location):
        pass

    GRID_X_MAX = 9
    GRID_Y_MAX = 9

    def issue_command_to_robot(self, robot_command: RobotDirection):
        self.robot.process_direction(robot_command)
        return

    def check_crate_at_location(self, location: Location):
        for crate in self.crates:
            if crate.crate_location == location:
                return True

        return False

    def change_location_to_be_in_boundaries(self, location: Location) -> Location:
        result_location: Location = location

        result_location.x = 0 if result_location.x < 0 else result_location.x
        result_location.y = 0 if result_location.y < 0 else result_location.y
        result_location.x = self.GRID_X_MAX if result_location.x > self.GRID_X_MAX else result_location.x
        result_location.y = self.GRID_Y_MAX if result_location.y > self.GRID_Y_MAX else result_location.y

        return result_location

    def spawn_crate(self, crate: Crate):
        self.crates.append(crate)

    def __init__(self, robot_start_location: Location):
        self.robot = Robot(self, robot_start_location)
        self.crates: List[Crate] = []


if __name__ == '__main__':

    robot_start_x = 0
    robot_start_y = 0
    robot_location = Location(robot_start_x, robot_start_y)

    warehouse = Warehouse(robot_location)
    warehouse.spawn_crate(Crate(Location(4, 4)))
    warehouse.spawn_crate(Crate(Location(9, 9)))

    commandString = "N E"

    commands = CommandParser.process_string(commandString)

    for command in commands:
        warehouse.issue_command_to_robot(command)
