import unittest

from robot_challenge import CommandParser
from robot_challenge.robot_direction import RobotDirection


class CommandParserTests(unittest.TestCase):

    def test_empty_string_returns_nothing(self):
        test_input = ""
        expected_output = []

        result = CommandParser.process_string(test_input)

        self.assertEqual(expected_output, result)

    def test_north_string_returns_north(self):
        test_input = "N"
        expected_output = [RobotDirection.NORTH]

        result = CommandParser.process_string(test_input)

        self.assertEqual(expected_output, result)

    def test_south_string_returns_south(self):
        test_input = "S"
        expected_output = [RobotDirection.SOUTH]

        result = CommandParser.process_string(test_input)

        self.assertEqual(expected_output, result)

    def test_east_string_returns_west(self):
        test_input = "E"
        expected_output = [RobotDirection.EAST]

        result = CommandParser.process_string(test_input)

        self.assertEqual(expected_output, result)

    def test_west_string_returns_west(self):
        test_input = "W"
        expected_output = [RobotDirection.WEST]

        result = CommandParser.process_string(test_input)


        self.assertEqual(expected_output, result)

    def test_sequence_N_S_E_W_W(self):
        test_input = "N S E W W"
        expected_output = [RobotDirection.NORTH, RobotDirection.SOUTH, RobotDirection.EAST, RobotDirection.WEST, RobotDirection.WEST]

        result = CommandParser.process_string(test_input)

        self.assertEqual(expected_output, result)

    def test_sequence_N_G_D_E_W(self):
        test_input = "N G D E W"
        expected_output = [RobotDirection.NORTH, RobotDirection.GRAB, RobotDirection.DROP, RobotDirection.EAST, RobotDirection.WEST]

        result = CommandParser.process_string(test_input)

        self.assertEqual(expected_output, result)

    # def test_sequence_N_E_returns_N_E_Command(self):
    #     test_input = "N E"
    #     expected_output = [RobotCommand.NORTH_EAST]
    #     result = CommandParser.process_string(test_input)
    #
    #     self.assertEqual(expected_output, result)

if __name__ == '__main__':
    unittest.main()
