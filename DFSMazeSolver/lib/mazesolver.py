import math
import sys
import time
import os

class stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(0,item)

    def pop(self):
        return self.stack.pop(0)

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
        sys.setrecursionlimit(999999)
        self.maze = list(maze.replace('\n',''))
        self.n = math.floor(math.sqrt(len(maze)))
        self.x = 0
        self.y = 0
        self.stack = stack()

        if len(maze) < 1:
            quit()
        self.entry = 0
        self.exit = len(maze)
        prev_direction = None

        current_unit = self.entry
        self.stack.push(current_unit)
        visited = []
        step = 0

        while self.stack.length() > 0:

            self.maze_render(current_unit)
            print(step)
            step+=1
            visited.append(current_unit)
            neighbors,directions = self.getNeighbors(current_unit)

            time.sleep(0.01)
            if "UP" in directions and neighbors[0] not in visited:
                self.stack.push(current_unit)
                current_unit = neighbors[0]

            elif "RIGHT" in directions and neighbors[1] not in visited:
                self.stack.push(current_unit)
                current_unit = neighbors[1]

            elif "DOWN" in directions and neighbors[2] not in visited:
                self.stack.push(current_unit)
                current_unit = neighbors[2]
            elif "LEFT" in directions and neighbors[3] not in visited:
                self.stack.push(current_unit)
                current_unit = neighbors[3]

            else:
                current_unit = self.stack.pop()

            if(len(self.maze)-1 == current_unit):
                while self.stack.length() > 0:
                    current_unit = self.stack.pop()
                    self.maze_render(current_unit)
                    time.sleep(0.01)
                    print(step)

        #while self.stack not empty
            # visited.append(unit)
            # paths = unit.getpaths()
            # if neighbor_has_up and not visited:
            #   self.stack.push(up)
            # elif neighbor_has_right and not visited:
            #   self.stack.push(right)
            # elif neighbor_has_down and not visited:
            #   self.stack.push(down)
            # elif neighbor_has_left and not visited:
            #   self.stack.push(left)
            # else:
            #   self.stack.pop()
            #

    def maze_render(self, currentUnit):
        # return maze as string
        os.system("clear")
        for i,unit in enumerate(self.maze):
            if i == currentUnit:
                print("☺",end="")
            elif self.stack.contains(i):
                print(self.MAZEWALLS_BOLD[unit],end="")
            else:
                print(self.MAZEWALLS[unit],end="")
            if i % self.n == self.n-1:
                print("")

    def getNeighbors(self, unit):
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
