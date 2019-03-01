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

    @property
    def position(self):
        return self._position
    
    @property
    def diameter(self):
        return self._diameter

    def interact_with_bundle(self, rays):
        """Returns list of intermediate rays and free rays"""
        # can only interact with 'free' rays, i.e. rays that haven't stopped anywhere yet
        out = [self.interact_with(ray) for ray in rays if ray.extent == float('inf')]
        return [pair[0] for pair in out] + [pair[1] for pair in out]


class SymmetricComponent(Component):

    def __init__(self, position, diameter, n, propagator_first, propagator_second):
        super().__init__(position, diameter, n)
        self._propagator_first = propagator_first
        self._propagator_second = propagator_second
    
    def interact_with(self, ray):
        distance = self._position - ray.start

        distance_intersect, height_intersect, angle_normal_intersect, angle_oa_intersect = self.\
                _propagator_first(ray)

        ray.extent = sqrt(distance_intersect**2 
                + (height_intersect - ray.height)**2)

        angle_out = snell(angle_normal_intersect, 
                angle_oa_intersect, 
                1, 
                self._refractive_index)

        ray_first = Ray(ray.start + distance_intersect, angle_out, height_intersect)

        #distance = self._position - ray.start + distance_intersect
        distance = distance_intersect
        distance_intersect, height_intersect, angle_normal_intersect, angle_oa_intersect = self.\
                _propagator_second(ray_first)

        ray_first.extent = sqrt(distance_intersect**2 
               + (height_intersect - ray_first.height)**2)


        angle_out_second = snell(angle_normal_intersect,
                angle_oa_intersect,
                self._refractive_index,
                1)

        ray_second = Ray(ray_first.start + distance_intersect,
                angle_out_second, 
                height_intersect)

        return ray_first, ray_second
