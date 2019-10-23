import unittest

from robot_challenge.command_parser import RobotDirection, CommandParser
from robot_challenge.location import Location
from robot_challenge.warehouse import Warehouse, Crate


class WarehouseTests(unittest.TestCase):


    def test_initial_robot_position_0_0(self):
        robot_start_x = 0
        robot_start_y = 0
        robot_location = Location(robot_start_x, robot_start_y)
        self.assertEqual(robot_start_x, robot_location.x)
        self.assertEqual(robot_start_y, robot_location.y)

    def test_initial_robot_position_2_2(self):
        robot_start_x = 2
        robot_start_y = 2
        robot_location = Location(robot_start_x, robot_start_y)
        self.assertEqual(robot_start_x, robot_location.x)
        self.assertEqual(robot_start_y, robot_location.y)

    def test_move_north(self):
        robot_start_x = 2
        robot_start_y = 2

        move_command = RobotDirection.NORTH
        expected_y_result = 3

        robot_location = Location(robot_start_x, robot_start_y)

        warehouse = Warehouse(robot_location)
        warehouse.issue_command_to_robot(move_command)

        self.assertEqual(robot_start_x, robot_location.x)
        self.assertEqual(expected_y_result, robot_location.y)

    def test_move_east(self):
        robot_start_x = 2
        robot_start_y = 2

        move_command = RobotDirection.EAST
        expected_x_result = 3

        robot_location = Location(robot_start_x, robot_start_y)

        warehouse = Warehouse(robot_location)
        warehouse.issue_command_to_robot(move_command)

        self.assertEqual(expected_x_result, robot_location.x)
        self.assertEqual(robot_start_y, robot_location.y)

    def test_move_outside_warehouse_south_is_stopped(self):
        robot_start_x = 0
        robot_start_y = 0

        move_command = RobotDirection.SOUTH
        robot_end_y = 0

        robot_location = Location(robot_start_x, robot_start_y)

        warehouse = Warehouse(robot_location)
        warehouse.issue_command_to_robot(move_command)

        self.assertEqual(robot_end_y, robot_location.y)

    def test_move_outside_warehouse_north_boundary_is_stopped(self):
        robot_start_y = 9
        robot_end_y = 9

        move_command = RobotDirection.NORTH
        robot_start_x = 0
        robot_location = Location(robot_start_x, robot_start_y)

        warehouse = Warehouse(robot_location)
        warehouse.issue_command_to_robot(move_command)

        self.assertEqual(robot_end_y, robot_location.y)

    def test_move_outside_warehouse_east_boundary_is_stopped(self):
        robot_start_x = 9
        robot_end_x = 9

        move_command = RobotDirection.EAST
        robot_start_y = 0
        robot_location = Location(robot_start_x, robot_start_y)

        warehouse = Warehouse(robot_location)
        warehouse.issue_command_to_robot(move_command)

        self.assertEqual(robot_end_x, robot_location.x)


class CrateTests(unittest.TestCase):

    def setUp(self) :
        robot_start_x = 0
        robot_start_y = 0
        robot_location = Location(robot_start_x, robot_start_y)

        self.warehouse = Warehouse(robot_location)
        self.warehouse.spawn_crate(Crate(Location(4, 4)))
        self.warehouse.spawn_crate(Crate(Location(9, 9)))

    def tearDown(self) :
        return

    def test_crate_not_at_location_returns_false(self):

        result = self.warehouse.check_crate_at_location(Location(1,1))
        self.assertFalse(result)

    def test_crate_at_location_returns_true(self):

        result = self.warehouse.check_crate_at_location(Location(4,4))
        self.assertTrue(result)

    def test_drop_crate_at_location_creates_crate(self):
        location = Location(1,1)
        crate_at_location_before = self.warehouse.check_crate_at_location(location)
        self.assertFalse(crate_at_location_before)

        self.warehouse.robot.process_direction(RobotDirection.GRAB)

        self.assertTrue(self.warehouse.robot.has_crate)
        self.assertFalse(self.warehouse.check_crate_at_location(location))

        self.warehouse.robot.process_direction(RobotDirection.DROP)
        self.assertTrue(self.warehouse.check_crate_at_location(location))

    def test_drop_crate_at_location_with_crate_does_nothing(self):
        pass

if __name__ == '__main__':
    unittest.main()
