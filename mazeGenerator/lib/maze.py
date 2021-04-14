#!/usr/local/bin/python3
from . import disjointSet
import random

hex = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F"
]

class Maze:
    def __init__(self):
        self.maze = []
        self.n = None
        self.mazeSet = disjointSet.DisjointSet()

        self.DIRECTIONS = {
            "UP": 2, # Up
            "DOWN": 8, # Down
            "LEFT": 4, # Left
            "RIGHT": 1  # Right
        }

        self.MAZEWALLS = {
            15: " ",
            14: "╺",
            13: "╻",
            12: "╔",
            11: "╸",
            10: "═",
            9: "╗",
            8: "╦",
            7: "╹",
            6: "╚",
            5: "║",
            4: "╠",
            3: "╝",
            2: "╩",
            1: "╣",
            0: "╬"
        }

    def initMaze(self, n):
        # maze size n*n units
        self.maze = [15 for _ in range(n**2)]
        self.n = n
        self.mazeSet.new_subset(n**2)
        self.entry = 0
        self.exit = n**2-1
        self.populteUnvisitedSpaces()

    def populteUnvisitedSpaces(self):
        self.unvisitedSpaces = [x for x in range(len(self.maze))]

    # get maze unit from unit by direction
    def getNeighbor(self, unit, direction):
        if direction == "UP" and unit - self.n > 0:
            return unit - self.n
        if direction == "DOWN" and unit + self.n < self.n**2:
            return unit + self.n
        if direction == "RIGHT" and unit % self.n != self.n-1:
            return unit + 1
        if direction == "LEFT" and unit % self.n != 0:
            return unit - 1

        return False
    # generate maze
    def generate(self, n):
        self.initMaze(n)

        # while maze is not one unit
        while self.mazeSet.numSets > 1:

            unit = random.choice(range(len(self.maze)))

            direction = random.choice(list(self.DIRECTIONS.keys()))
            neighbor = self.getNeighbor(unit, direction)

            if neighbor == False:
                continue
            if self.mazeSet.same_set(unit, neighbor):
                continue

            if not self.mazeSet.union(unit, neighbor):
                continue

            # Up
            if direction == "UP":
                # unit: knock up
                # neighbor: knock down
                if not self.knockWall(unit, neighbor, "DOWN", "UP"):
                    continue
            # Down
            elif direction == "DOWN":
                # unit: knock Down
                # neighbor: knock up
                if not self.knockWall(unit, neighbor, "UP", "DOWN"):
                    continue
            # Left
            elif direction == "LEFT":
                # unit: knock Left
                # neighbor: knock right
                if not self.knockWall(unit, neighbor, "LEFT", "RIGHT"):
                    continue
            # right
            elif direction == "RIGHT":
                # unit: knock Right
                # neighbor: knock left
                if not self.knockWall(unit, neighbor, "RIGHT", "LEFT"):
                    continue

    # return maze as string
    def getMazeRender(self):
        output = ""
        for i,unit in enumerate(self.maze):
            # output += hex[unit]
            if(i == self.entry or i == self.exit):
                output += "X"
            else:
                output += self.MAZEWALLS[unit]
            if i % self.n == self.n-1:
                output += "\n"

        return output

    # maze unit, direction
    def knockWall(self, unit, neighbor, direction, neighborDirection):
        if self.maze[unit] - self.DIRECTIONS[direction] < 0 or self.maze[neighbor] - self.DIRECTIONS[neighborDirection] < 0:
            return False
        self.maze[unit] -= self.DIRECTIONS[direction]
        self.maze[neighbor] -= self.DIRECTIONS[neighborDirection]
        return True
# 0 =
# 1 = ╺
# 2 = ╻
# 3 = ╔
# 4 = ╸
# 5 = ═
# 6 = ╗
# 7 = ╦
# 8 = ╹
# 9 = ╚
# A = ║
# B = ╠
# C = ╝
# D = ╩
# E = ╣
# F = ╬
