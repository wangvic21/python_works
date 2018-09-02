#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    num_points = 5000
    rw = RandomWalk(num_points)
    rw.fill_walk()
    # Set the size of plotting window.
    plt.figure(dpi = 120, figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues,edgecolors='none', s=5)
    # Enphasize the first and last points.
    plt.scatter(0, 0, c='green', s=40)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=40)

    # Hide the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break