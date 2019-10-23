from typing import List

from robot_challenge.robot_direction import RobotDirection


class CommandParser:
    @staticmethod
    def process_string(commandString : str) -> List[RobotDirection]:
        """
        Processes strings containing sequences of commands for the robot_challenge and parses them. These sequences should be space
        delimited.
        :param commandString:
        :return: an array of strings
        """
        command_string = commandString.split(" ")
        directions_result = []

        if command_string == [""]:
            return directions_result

        for direction in command_string:
            parsed_direction = RobotDirection(direction)
            directions_result.append(parsed_direction)

        # previous_direction : RobotCommand

        # for direction in command_string:
        #
        #     previous_direction = direction

        return directions_result

    def __init__(self):
        return
