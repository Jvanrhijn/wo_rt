from math import sqrt
from src.raytracing import propagate_to_flat, snell 
from src.ray import Ray


class Window:
    def __init__(self, position, diameter, thickness, n):
        self._position = position
        self._diameter = diameter
        self._thickness = thickness
        self._refractive_index = n

    def interact_with(self, ray):
        distance = self._position - ray.start

        height_intersect, angle_normal_intersect, angle_oa_intersect = propagate_to_flat(
                ray.height, 
                ray.angle, 
                distance, 
                self._diameter)[1:]
        ray.extent = sqrt(distance**2 + (height_intersect - ray.height)**2)

        angle_out = snell(
                angle_normal_intersect, 
                angle_oa_intersect, 
                1, 
                self._refractive_index)

        ray_first = Ray(self._position, angle_out, height_intersect)

        height_intersect, angle_normal_intersect, angle_oa_intersect = propagate_to_flat(
                ray_first.height,
                ray_first.angle,
                self._thickness,
                self._diameter)[1:]

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

        

