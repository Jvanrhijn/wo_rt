import matplotlib.pyplot as plt
import numpy as np
from math import pi, atan
from src.ray import Ray
from src.window import Window
from src.lens import Lens
from src.visualizer import Visualizer


def produce_beam(width, start, nrays, focal_length):
    return [Ray(start, 0, height) for height in np.linspace(-width/2, width/2, nrays)]


if __name__ == "__main__":
    lens = Lens(0.5, 1, 1, 1.5)
    window = Window(1, 1, 0.001, 1.5)

    ray = Ray(0, 0, 0.1)

    beam = produce_beam(0.5, 0, 10, 0.2)

    lens_rays = lens.interact_with_bundle(beam)
    window_rays = window.interact_with_bundle(lens_rays)

    all_rays = beam + lens_rays + window_rays


    visualizer = Visualizer(all_rays, [lens, window], (2, 2))
    visualizer.draw_all('r')
    plt.show()
