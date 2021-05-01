import sys
import math

if sys.stdin.isatty():
    quit()

maze = sys.stdin
MAZEWALLS = {
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

output = ""
maze = maze.read().replace('\n','')
n = math.sqrt(len(maze))

for i,unit in enumerate(maze):
    # output += hex[unit]
    output += MAZEWALLS[unit]
    if i % n == n-1:
        output += "\n"

print(output)
