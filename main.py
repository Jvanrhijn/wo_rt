import matplotlib.pyplot as plt
import numpy as np
from math import pi, atan
from src.ray import Ray
from src.window import Window
from src.visualizer import Visualizer


def produce_beam(width, start, nrays, focal_length):
    rays = []
    for ray_height in np.linspace(-width/2, width/2, nrays):
        angle = -atan(ray_height/(focal_length - start))
        rays.append(Ray(start, angle, ray_height))
    return rays



if __name__ == "__main__":
    window = Window(1, 1, 0.001, 1.5)
    all_rays = []
    beam = produce_beam(0.5, 0, 10, 1.02)

    for ray in beam:
        produced_rays = window.interact_with(ray)
        for r in [ray, *produced_rays]:
            all_rays.append(r)

    visualizer = Visualizer(all_rays, [window], (2, 2))
    visualizer.draw_all('r')

    plt.show()
