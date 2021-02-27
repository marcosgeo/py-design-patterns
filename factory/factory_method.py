from enum import Enum
from math import sin, cos


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    # standard constructor, who might get more complicated due 
    # coordinate system
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)

    # a method to be used by the factories methods
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.coord_sys = s

    def __str__(self):
        return f"{self.coord_sys}: x: {self.x} y: {self.y}"

    class PointFactory:
        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta), CoordinateSystem.POLAR)

        def new_cartesian_point(self, x, y):
            return Point(x, y, CoordinateSystem.CARTESIAN)

    factory = PointFactory()



if __name__ == "__main__":
    # p1 = Point(2, 3)
    # p2 = Point.new_polar_point(3, 4)
    # print(p1, p2, end="\n")

    p1 = Point.factory.new_cartesian_point(2, 3)
    p2 = Point.factory.new_polar_point(3, 4)
    print(p1, p2, end="\n\n")