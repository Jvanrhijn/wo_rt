import numpy as np
from math import sqrt
from src.component import SymmetricComponent
from src.drawable import Drawable
from src.raytracing import propagate_to_sphere, snell
from src.ray import Ray


class Lens(SymmetricComponent, Drawable):

    def __init__(self, position, diameter, curvature_radius, n):
        self._thickness = 2*curvature_radius*(1 - sqrt(1 - (diameter/(2*curvature_radius))**2))
        if diameter > 2*curvature_radius:
            raise ValueError("Impossible lens geometry")

        def propagator_first(ray, distance):
            return propagate_to_sphere(ray.height, ray.angle, distance, diameter, curvature_radius)

        def propagator_second(ray, distance):
            thickness = 2*curvature_radius*(1 - sqrt(1 - (diameter/(2*curvature_radius))**2))
            distance = thickness - ray.start
            return propagate_to_sphere(ray.height, ray.angle, distance, diameter, -curvature_radius) 

        super().__init__(position, diameter, n, propagator_first, propagator_second)
        self._curvature_radius = curvature_radius

    def draw(self, axis, color, fill=False):
        theta = self._diameter/(2*self._curvature_radius)
        theta = np.linspace(-theta, theta, 100)
        xs = self._curvature_radius*np.cos(theta) - self._curvature_radius + self._thickness/2
        ys = self._curvature_radius*np.sin(theta) 
        distance = self._position + self._thickness/2
        axis.plot(xs + distance, ys, color=color)
        axis.plot(-xs + distance, ys, color=color)
