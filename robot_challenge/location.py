class Location:

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
