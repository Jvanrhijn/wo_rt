from math import sqrt
from src.raytracing import propagate_to_flat, snell 
from src.ray import Ray
from src.component import SymmetricComponent
from src.drawable import Drawable


class Window(SymmetricComponent, Drawable):
    def __init__(self, position, diameter, thickness, n):
        def propagator(ray, distance):
            return propagate_to_flat(ray.height, ray.angle, distance, diameter)
        super().__init__(position, diameter, n, propagator, propagator)
        self._thickness = thickness


    def draw(self, axis, color, fill=False):
        radius = self._diameter/2
        points = [
                (self._position, -radius),
                (self._position + self._thickness, -radius),
                (self._position + self._thickness, radius),
                (self._position, radius),
                (self._position, -radius),
        ]
        if fill:
            axis.fill(*zip(*points), color=color)
        else:
            axis.plot(*zip(*points), color=color)

        

