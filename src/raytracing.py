from math import sin, asin, tan
from numpy import roots

out_of_bounds_msg = "Ray out of bounds for optical component"


def snell(angle_in_normal, angle_in_oa, n0, n1):
    """Compute outgoing angle with respect to optical axis after refraction
    :param: angle_in_normal Incoming ray angle with respect to normal
    :param: angle_in_oa Incoming ray angle with respect to optical axis
    :param: n0, n1 Refractive indices of incoming and outoing medium
    :return: angle with respect to optical axis
    """
    return asin(sin(angle_in_normal)*n0/n1) + angle_in_oa


def propagate_to_flat(height, ray_angle, distance, diameter):
    """Compute intersection point of ray with flat surface
    :param: ray_angle angle of ray with respect to optical axis
    :return: distance along optical axis, angle of normal, angle with respect to 
    optical axis 
    """
    height_intersect = height + tan(ray_angle)*distance
    distance_intersect = distance
    angle_normal_intersect = ray_angle
    angle_optical_axis_intersect = 0
    if diameter < 2*height_intersect:
        raise ValueError(out_of_bounds_msg)
    return distance_intersect, height_intersect, \
            angle_normal_intersect, angle_optical_axis_intersect


def propagate_to_sphere(height, ray_angle, distance, diameter, radius):
    """Compute intersection point of ray with spherical surface
    :param: distance Distance to surface midpoin along optical axis
    :param: diameter Spherical surface extent/diameter of optical component
    :param: radius Spherical radius of curvature
    """
    a = 1 + tan(ray_angle)**2
    b = 2*height*tan(ray_angle) - 2*radius - 2*distance
    c = height**2 + 2*distance*radius + distance**2

    if radius > 0:
        z1 = min(roots([a, b, c]))
    else:
        z1 = max(roots([a, b, c]))

    r1 = height + z1 * tan(ray_angle)
    angle_optical_axis_intersect = -asin(r1/radius)
    angle_normal_intersect = -angle_optical_axis_intersect + ray_angle

    if diameter < 2*r1:
        raise ValueError(out_of_bounds_msg)
    return z1, r1, angle_normal_intersect, angle_optical_axis_intersect

