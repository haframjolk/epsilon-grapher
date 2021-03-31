#!/usr/bin/env python3

import json
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def init():
    """Initializes the required data"""
    global data
    with open("votes.json") as f:
        data = json.load(f)


def draw():
    """Draws a bar graph showing the results"""
    fig = plt.figure(dpi=150)
    bars = plt.bar(data.keys(), data.values())
    # Make empty votes bar red
    bars[-1].set_color("r")
    # Set labels
    plt.title("Election Results")
    plt.xlabel("Candidates")
    plt.ylabel("Votes")
    # Show only integers on y-axis
    fig.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    # Show graph
    plt.show()


init()
draw()
