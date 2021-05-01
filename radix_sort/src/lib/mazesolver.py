import math
import sys
import time
import os
import re

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(0,item)

    def pop(self):
        return self.stack.pop(0)

    def clear(self):
        self.stack = []

    def contains(self, item):
        return item in self.stack

    def length(self):
        return len(self.stack)

class MazeSolver():
    def __init__(self):
        self.unit = 0
        self.n = 0
        self.maze = []
        self.directions = {
            "E":["RIGHT"],
            "D":["DOWN"],
            "C":["RIGHT","DOWN"],
            "B":["LEFT"],
            "A":["RIGHT","LEFT"],
            "9":["DOWN","LEFT"],
            "8":["RIGHT","DOWN","LEFT"],
            "7":["UP"],
            "6":["UP","RIGHT"],
            "5":["UP","DOWN"],
            "4":["UP","RIGHT","DOWN"],
            "3":["UP","LEFT"],
            "2":["UP","RIGHT","LEFT"],
            "1":["UP","DOWN","LEFT"],
            "0":["UP","RIGHT","DOWN","LEFT"]
        }
        self.directionOpposites = {
            "UP":"DOWN",
            "DOWN":"UP",
            "RIGHT":"LEFT",
            "LEFT":"RIGHT"
        }
        self.MAZEWALLS_BOLD = {
            "F": " ",
            "E": "╺",
            "D": "╻",
            "C": "╔",
            "B": "╸",
            "A": "═",
            "9": "╗",
            "8": "╦",
            "7": "╹",
            "6": "╚",
            "5": "║",
            "4": "╠",
            "3": "╝",
            "2": "╩",
            "1": "╣",
            "0": "╬"
        }
        self.MAZEWALLS = {
            "F": " ",
            "E": "╺",
            "D": "╻",
            "C": "┌",
            "B": "╸",
            "A": "─",
            "9": "┐",
            "8": "┬",
            "7": "╹",
            "6": "└",
            "5": "│",
            "4": "├",
            "3": "┘",
            "2": "┴",
            "1": "┤",
            "0": "┼"
        }

    # solve maze as a string of hex code
    def solve(self, maze):
        print("BEGIN SEARCH")
        # clean maze input string
        self.maze = list(maze.replace('\n',''))

        # init vars
        self.n = math.floor(math.sqrt(len(maze)))
        self.x = 0
        self.y = 0
        self.backtrack_stack = Stack()
        self.entry = 0
        self.exit = len(maze)
        current_unit = self.entry

        # push initial unit to backtrack_stack
        # initialize depth first search
        self.backtrack_stack.push(current_unit)
        visited = []
        step = 0

        # start timer
        start = time.time()

        # main loop
        while self.backtrack_stack.length() > 0:
            self.render_maze(current_unit)
            step+=1
            # current unit has been visited
            visited.append(current_unit)
            # get valid directions from current unit
            neighbors,directions = self.getNeighbors(current_unit)

            # for each direction
            # if direction valid and not previously visited
            for i,direction in enumerate(["UP", "RIGHT", "DOWN", "LEFT"]):
                if direction in directions and neighbors[i] not in visited:
                    # add unit to backtrack backtrack stack
                    # move to unit
                    self.backtrack_stack.push(current_unit)
                    current_unit = neighbors[i]
                    # exit loop
                    break
            else:
                # found dead end - backtrack
                current_unit = self.backtrack_stack.pop()

            # test for win case
            if(len(self.maze)-1 == current_unit):
                # end timer
                seconds = round(time.time() - start, 4)
                # humorous message
                if(len(self.maze) < 2):
                    print("☹")
                    print("SOMEBODY LET ME OUT OF HERE!!")
                # output stats
                else:
                    self.render_maze(current_unit)
                    print("MAZE SOLVED IN {} SECONDS AFTER {} STEPS".format(seconds, step))

                    # clear stack to end loop
                    self.backtrack_stack.clear()
                    ###################
                    ### end program ###
                    ###################

    # render maze as graphical ascii
    def render_maze(self, current_unit):
        # return maze as string
        os.system("clear")
        # for each unit
        for i,unit in enumerate(self.maze):
            # print agent
            if i == current_unit:
                print("☺",end="")
            # print
            elif self.backtrack_stack.contains(i):
                print(self.MAZEWALLS_BOLD[unit],end="")
            else:
                print(self.MAZEWALLS[unit],end="")
            if i % self.n == self.n-1:
                print("")

    def getNeighbors(self, unit):
        if unit > len(self.maze)-1:
            quit()
        if self.maze[unit] not in self.MAZEWALLS.keys():
            print("Error - invalid maze character: {}".format(self.maze[unit]))
            quit()
        neighbors = []
        directions = []
        for direction in ["UP", "RIGHT","DOWN","LEFT"]:
            neighbor = self.getNeighbor(unit,direction)
            if neighbor != None and direction in self.directions[self.maze[unit]]:
                neighbors.append(neighbor)
                directions.append(direction)
            else:
                neighbors.append(None)
        return neighbors,directions

    def getNeighbor(self, unit, direction):
        if direction == "UP" and unit - self.n > 0:
            self.y -= 1
            return unit - self.n
        if direction == "DOWN" and unit + self.n < self.n**2:
            self.y += 1
            return unit + self.n
        if direction == "RIGHT" and unit % self.n != self.n-1:
            self.x += 1
            return unit + 1
        if direction == "LEFT" and unit % self.n != 0:
            self.x -= 1
            return unit - 1
