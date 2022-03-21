#!/usr/bin/env python3

import json
import matplotlib.pyplot as plt


def init():
    """Initializes the required data"""
    global data
    with open("results.json") as f:
        data = json.load(f)


def draw():
    """Draws a bar graph showing the results"""
    # Create figure
    plt.figure(dpi=150)

    # Sort names by number of votes in descending order
    names = sorted(data.keys(), key=data.get, reverse=True)
    # Move empty ballot group to end of list
    names.remove("empty")
    names.append("empty")
    # Get votes for each candidate
    votes = [data[name] for name in names]

    # Plot results
    y_pos = range(len(data))  # y range
    bars = plt.barh(y_pos, votes, align="center")

    # Hide ticks
    plt.tick_params(axis="both", length=0)
    # Set tick labels to candidate names
    plt.yticks(y_pos, names)

    # Get current axes
    ax = plt.gca()
    # Only show integers on x axis ticks
    ax.xaxis.get_major_locator().set_params(integer=True)
    # Invert y axis
    ax.invert_yaxis()

    # Set empty ballot bar color to red
    bars[-1].set_color("r")

    # Set labels
    plt.xlabel("Votes")
    plt.title("Election Results")

    # Get maximum number of votes to find the graph's width
    M = max(votes)
    # Write number of votes next to each bar
    for rect, val in zip(bars.patches, votes):
        # Offset text to the right by 2% of the graph's width
        # That way, the pixel value of the offset is always the same
        plt.text(rect.get_width() + M * 0.02,
                 rect.get_y() + rect.get_height() / 2,
                 val,
                 ha="left",
                 va="center")

    # Set margins to fit vote labels
    plt.margins(0.1, 0.05)
    # Fit everything to the current layout
    plt.tight_layout()
    # Save graph
    plt.savefig("results.png")


init()
draw()
