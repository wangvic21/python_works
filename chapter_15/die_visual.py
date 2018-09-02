#!/usr/bin/env python
# -*- coding: utf-8 -*-

from die import Die
import pygal

# Create a die.
num_sides = 6
die = Die(num_sides)

# Make some rolls, and store results in a lsit.
results = []
roll_nums = 100
for roll_num in range(roll_nums):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()
hist.force_uri_protocol = 'http'
hist.title = "Result of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
hist.render_to_png('die_visual.png')