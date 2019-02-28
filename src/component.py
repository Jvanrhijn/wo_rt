from math import sqrt
from abc import ABC, abstractmethod
from src.raytracing import snell
from src.ray import Ray


class Component:

    def __init__(self, position, diameter, n):
        self._position = position
        self._diameter = diameter
        self._refractive_index = n

    @abstractmethod
    def interact_with(self, ray):
        pass


class SymmetricComponent(Component):

    def __init__(self, position, diameter, n, propagator_first, propagator_second):
        super().__init__(position, diameter, n)
        self._propagator_first = propagator_first
        self._propagator_second = propagator_second
    
    def interact_with(self, ray):
        distance = self._position - ray.start

        height_intersect, angle_normal_intersect, angle_oa_intersect = self._propagator_first(
                ray,
                distance)[1:]
        ray.extent = sqrt(distance**2 + (height_intersect - ray.height)**2)

        angle_out = snell(
                angle_normal_intersect, 
                angle_oa_intersect, 
                1, 
                self._refractive_index)

        ray_first = Ray(self._position, angle_out, height_intersect)

        height_intersect, angle_normal_intersect, angle_oa_intersect = self._propagator_second(
                ray_first,
                self._thickness)[1:]

        ray_first.extent = sqrt(self._thickness**2 
               + (height_intersect - ray_first.height)**2)

        angle_out = snell(
                angle_normal_intersect,
                angle_oa_intersect,
                self._refractive_index,
                1)

        ray_second= Ray(
                self._position + self._thickness, 
                angle_out, 
                height_intersect)

        return ray_first, ray_second

