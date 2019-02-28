import matplotlib.pyplot as plt
import numpy as np
from math import pi, atan
from src.ray import Ray
from src.window import Window
from src.lens import Lens
from src.visualizer import Visualizer


def produce_beam(width, start, nrays, focal_length):
    rays = []
    for ray_height in np.linspace(-width/2, width/2, nrays):
        angle = 0 #-atan(ray_height/(focal_length - start))
        rays.append(Ray(start, angle, ray_height))
    return rays


if __name__ == "__main__":
    lens = Lens(0.5, 1, 1, 1.5)
    ray = Ray(0, 0, 0.1)

    #window = Window(0.1, 1, 0.001, 1.5)
    all_rays = []
    beam = produce_beam(0.5, 0, 10, 0.2)

    for ray in beam:
        produced_rays = lens.interact_with(ray)
        for r in [ray, *produced_rays]:
            all_rays.append(r)

    visualizer = Visualizer(all_rays, [lens], (2, 2))
    visualizer.draw_all('r')
    plt.show()
