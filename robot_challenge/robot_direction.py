from enum import Enum


class RobotDirection(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"
    GRAB = "G"
    DROP = "D"

    NORTH_EAST = "NorthEast"
    SOUTH_EAST = "SouthEast"
    SOUTH_WEST = "SouthWest"
    NORTH_West = "NorthWest"


