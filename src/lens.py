import numpy as np
from math import sqrt, asin
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
            distance = self._position - ray.start + thickness
            return propagate_to_sphere(ray.height, ray.angle, distance, diameter, -curvature_radius) 

        super().__init__(position, diameter, n, propagator_first, propagator_second)
        self._focal_length = ((n-1)*(2/curvature_radius 
            + (n-1)*self._thickness/(n*curvature_radius**2)))**-1
        self._focal_plane = self._position + self._thickness/2 + self._focal_length
        self._curvature_radius = curvature_radius

    @property
    def focal_length(self):
        return self._focal_length

    @property
    def thickness(self):
        return self._thickness

    @property
    def focal_plane(self):
        return self._focal_plane

    def draw(self, axis, color, fill=False):
        theta = asin(self._diameter/(2*self._curvature_radius))
        theta = np.linspace(-theta, theta, 100)
        xs = self._curvature_radius*np.cos(theta)
        xs -= min(xs)
        ys = self._curvature_radius*np.sin(theta) 
        distance = self._position + self._thickness/2
        if fill:
            axis.fill(xs + distance, ys, color=color)
            axis.fill(-xs + distance, ys, color=color)
        else:
            axis.plot(xs + distance, ys, color=color)
            axis.plot(-xs + distance, ys, color=color)

