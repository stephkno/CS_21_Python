#!/usr/bin/python3
from src import mazesolver

import sys

#u,d,l,r


if sys.stdin.isatty():
    quit()

maze = sys.stdin.read()
mazesolver = mazesolver.MazeSolver()
mazesolver.solve(maze)
