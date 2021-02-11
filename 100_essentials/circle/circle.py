from math import pi


class Circle:
    # **Write your solution below**

    def __init__(self, radius=1):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        # self.radius(radius)
        self._radius = radius
        self._diameter = radius * 2
        self._calculate_area()

    def __repr__(self):
        return f"Circle({self.radius})"

    def __str__(self):
        return f"Circle({self.radius})"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            raise ValueError("Radius cannot be negative")

        self._radius = new_radius
        self._diameter = new_radius * 2
        self._calculate_area()

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, new_diameter):
        if new_diameter < 0:
            raise ValueError("Diameter cannot be negative")

        else:
            self._radius = new_diameter / 2
            self._diameter = new_diameter
            self._calculate_area()

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, new_area):
        raise AttributeError("can't set attribute")

    def _calculate_area(self):
        self._area = (self._radius ** 2) * pi
