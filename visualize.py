import pyvista as pv
import numpy as np

def visualize_neuron(points, color='aqua', point_size=8, show_axes=True):
    cloud = pv.PolyData(points)
    plotter = pv.Plotter()
    plotter.add_points(cloud, color=color, point_size=point_size, render_points_as_spheres=True)
    if show_axes:
        plotter.show_axes()
    plotter.show()
