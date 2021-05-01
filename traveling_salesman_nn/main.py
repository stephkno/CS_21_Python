#!/usr/local/bin/python3
#
# traveling salesman problem
#
import pygame
import random
import math


class Vertex():
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.distance = None
        self.name = name

    # return position of vertex x, y pair
    def get_position(self):
        return self.x, self.y

    def set_distance(self, vertex):
        self.distance = self.get_distance(vertex)
        return self.distance

    # get pythagorean distance between self and vertex
    def get_distance(self, vertex):
        return math.sqrt( (self.x - vertex.x) ** 2 + (self.y - vertex.y) ** 2)

def draw_world(cities):

    #for i,vertex in enumerate(vertices):
    #        print("City {},{}:{}".format(i, vertex.name, vertex.get_position()))

    font = pygame.font.Font('/Library/Fonts/InputMono-Black.ttf', 12)

    running = True
    total_distance = 0.0

    for city in cities:
        print("{}:{}".format(city.name, city.distance))
        if city.distance != None:
            total_distance += city.distance

    print("Total distance: {}".format(total_distance))

    # draw cities and route
    screen.fill((0, 0, 0))

    last_city = None

    for i, city in enumerate(cities):

        if last_city != None:
            pygame.draw.line(screen, (90, 90, 90), (city.x, city.y), (last_city.x, last_city.y), 4)

        text = font.render("{}:{}".format(i,city.name), True, (255,255,255), (0,0,255))
        screen.blit(text, (city.x, city.y))

        pygame.draw.circle(screen, (255, 255, 255), (city.x, city.y), 4)

        last_city = city

    pygame.draw.line(screen, (90, 90, 90), (cities[0].x, cities[0].y), (last_city.x, last_city.y), 4)

    pygame.display.flip()

    cities.clear()

    #while running:
    #    for e in pygame.event.get():
    #        if e.type == pygame.QUIT:
    #            running != running



file = "./data/cities"

file = open(file, 'r')
city_names = file.readlines()
city_names = [city.replace("\n","") for city in city_names]

n_cities = 32
world_size = 800

vertices = []
visited_cities = 0
current_city = None
vertices = []

def main():
    while True:
        travel_salesman(vertices=init_world())
        input()


def init_world():
    # list of cities as vertices
    vertices = [
                Vertex(
                random.random() * world_size,
                random.random() * world_size,
                random.choice(city_names)) for _ in range(n_cities)
                ]

    return vertices

def travel_salesman(visited_cities=1, cities=[], vertices=[]):

    current_city = vertices[0]
    cities.append(vertices[0])
    vertices.pop(0)

    # for each city
    while visited_cities < n_cities:

        # get nearest city
        nearest_neighbor(current_city, vertices)
        current_city = vertices[0]
        cities.append(current_city)
        visited_cities+=1
        vertices.pop(0)

    draw_world(cities)


def getKey(elem):
    # return first element - distance values
    return elem.distance

def nearest_neighbor(vertex, vertices):
    # find distances

    for v in vertices:
        v.set_distance(vertex)

    # sort distances
    vertices.sort(key=getKey)

    # print distances
    #for v in vertices:
    #       print("{},{}".format(v.name, v.distance))

pygame.init()
screen = pygame.display.set_mode((world_size, world_size))

main()
