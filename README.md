# Epsilon Grapher

A simple Python program that draws a bar graph based on the results of an election conducted with [Epsilon](https://github.com/haframjolk/epsilon).

## Prerequisites

Epsilon Grapher requires Python 3.9 or later and [Poetry](https://python-poetry.org/).

## Setup

```sh
git clone https://github.com/haframjolk/epsilon-grapher.git
cd epsilon-grapher
poetry install
```

## Usage

Place an Epsilon election results JSON file in the `epsilon-grapher` directory, called `results.json`. Then, run the following commands:

```sh
poetry run ./graph.py
```

An image called `results.png` will be created, showing the election results in a bar graph. The bar for empty ballots will be colored red.
