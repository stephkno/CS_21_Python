#!/usr/local/bin/python3
from . import disjointSet
import random
import os
import sys

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
        self.units_total = len(self.maze)
        self.units_touched = 0

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

    def print_stats(self):
        bar_width = os.get_terminal_size().columns
        print(int(100*(self.units_touched/self.units_total)),end="% ")
        for x in range(3,int(bar_width*(self.units_touched/self.units_total))):
            print("X",end="")
        sys.stdout.write('\r')
        sys.stdout.flush()

    # generate maze
    def generate(self, n):
        self.initMaze(n)

        # while maze is not one unit
        while self.mazeSet.numSets > 1:

            # need to choose from list of units
            unit = random.choice(self.unvisitedSpaces)
            #unit = random.choice(range(len(self.maze)))

            direction = random.choice(list(self.DIRECTIONS.keys()))
            neighbor = self.getNeighbor(unit, direction)

            if neighbor == False:
                continue
            if self.mazeSet.same_set(unit, neighbor):
                continue
            if not self.mazeSet.union(unit, neighbor):
                continue

            if self.maze[unit] == 0:
                self.unvisitedSpaces.remove(unit)

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

            if self.maze[unit]==0:
                self.unvisitedSpaces.remove(unit)
            if self.maze[neighbor]==0:
                self.unvisitedSpaces.remove(neighbor)

            #self.print_stats()

#        print()


    # return maze as string
    def getMazeRender(self):
        output = ""
        for i,unit in enumerate(self.maze):
            # output += hex[unit]
            #if(i == self.entry):
            #    output += "S"
            #elif(i == self.exit):
            #    output += "E"
        #    else:
            output += self.MAZEWALLS[unit]
            if i % self.n == self.n-1:
                output += "\n"

        return output

    # return maze as hex
    def toString(self):
        output = ""
        for i,unit in enumerate(self.maze):
            if unit > 9:
                output += hex[unit]
            else:
                output += str(unit)
        return output

    # maze unit, direction
    def knockWall(self, unit, neighbor, direction, neighborDirection):
        # knock wall only if in bounds
        if self.maze[unit] - self.DIRECTIONS[direction] < 0 or self.maze[neighbor] - self.DIRECTIONS[neighborDirection] < 0:
            return False

        # knock wall and neighbor wall
        self.maze[unit] -= self.DIRECTIONS[direction]
        self.maze[neighbor] -= self.DIRECTIONS[neighborDirection]

        # update maze progress stats
        if(self.maze[unit] < 15 or self.maze[neighbor] < 15):
            self.units_touched += 1
        return True
# F =
# E = ╺
# D = ╻
# C = ╔
# B = ╸
# A = ═
# 9 = ╗
# 8 = ╦
# 7 = ╹
# 6 = ╚
# 5 = ║
# 4 = ╠
# 3 = ╝
# 2 = ╩
# 1 = ╣
# 0 = ╬
