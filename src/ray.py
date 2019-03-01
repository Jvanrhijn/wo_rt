from math import sin, cos, tan


class Ray:

    def __init__(self, start, angle, height):
        self._start = start
        self._angle = angle
        self._height = height
        self._extent = float('inf')

    @property
    def start(self):
        return self._start

    @property
    def angle(self):
        return self._angle

    @property
    def height(self):
        return self._height

    @property
    def extent(self):
        return self._extent

    @extent.setter
    def extent(self, value):
        self._extent = value

    def as_coordinate_array(self, xcoords):
        return self._height + tan(self._angle)*(xcoords - self._start)

    def draw(self, axis, color, cutoff):
        extent = self._extent if self._extent < float('inf') else cutoff
        points = [
                (self._start, self._height),
                (self._start + extent*cos(self._angle),
                    self._height + extent*sin(self._angle))
        ]
        axis.plot(*zip(*points), color=color)




