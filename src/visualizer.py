from math import sqrt
import matplotlib.pyplot as plt
from src.window import Window


class Visualizer:
    def __init__(self, rays, components, dims):
        self._width, self._height = dims
        self._rays = rays
        self._components = components

    def draw_all(self, ray_color, figscale=1):
        figsize = (figscale*self._width, figscale*self._height)
        self._fig, self._ax = plt.subplots(1, figsize=figsize)
        self._draw_components('#92f3ff')
        self._draw_rays(ray_color, 0)
        self._ax.grid(True)
        self._ax.set_ylim(-self._height/2, self._height/2)
        self._ax.set_xlim(0, self._width)

    def _draw_components(self, color):
        for component in self._components:
            component.draw(self._ax, color, fill=True)

    def _draw_rays(self, color, thickness):
        cutoff = sqrt(self._width**2 + self._height**2)
        for ray in self._rays:
            ray.draw(self._ax, color, cutoff)

    
