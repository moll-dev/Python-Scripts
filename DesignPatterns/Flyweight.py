'''
Flyweight. A design pattern used solely for efficiency with
large arrays of nearly indentical objects.
 
A simple world generator
 
Written in python for simplicity sake.
 
For more info >> http://gameprogrammingpatterns.com/command.html
'''
from random import *
 
class World:
def __init__(self, width, height):
self.grass = Terrain(1, False, "grass.png")
self.hill = Terrain(3, False, "hill.png")
self.water = Terrain(2, True, "water.png")
 
self.WIDTH, self.HEIGHT = width, height
self.grid = [[None for i in range(height)] for j in range(width)]
 
def __str__(self):
output = ""
for x in xrange(0, self.WIDTH):
for y in xrange(0, self.HEIGHT):
output+= "["+str(self.grid[x][y].get_movement_cost())+"]"
output+= "\n"
return output
 
def paint_terrain(self):
for x in range(self.WIDTH):
for y in range(self.HEIGHT):
if randint(1,10) == 10:
self.grid[x][y] = self.hill
else:
self.grid[x][y] = self.grass
 
def get_movement_cost(self,x,y):
return self.grid[x][x].get_movement_cost()
 
class Terrain:
 
def __init__(self, movement_cost, is_water, texture):
self.movement_cost, self.is_water, self.texture = movement_cost , is_water, texture
 
def get_movement_cost(self):
return self.movement_cost
 
def is_water(self):
return is_water
 
 
new_world = World(20, 15)
new_world.paint_terrain()
 
print new_world
 
'''
Output:
 
[1][1][3][1][3][1][1][3][1][3][1][1][3][1][1]
[1][1][1][1][1][1][1][1][1][1][1][1][1][1][1]
[1][1][1][1][3][1][1][1][1][1][3][1][1][1][1]
[1][3][3][1][3][1][1][1][1][1][1][1][1][3][1]
[1][1][1][1][1][1][1][3][1][1][1][1][1][1][1]
[1][1][1][1][3][1][3][1][1][1][1][3][1][1][1]
[1][1][1][1][1][1][1][1][1][1][1][1][1][1][3]
[1][1][1][3][1][1][1][1][1][1][1][3][1][1][1]
[1][1][1][1][1][1][1][1][1][1][1][1][1][1][1]
[3][1][1][1][1][1][1][1][1][1][1][1][1][1][1]
[1][1][1][1][1][1][1][1][1][1][1][1][1][1][1]
[1][1][1][1][1][1][1][1][1][1][1][1][1][1][1]
[3][1][3][1][1][3][1][1][1][1][1][1][1][1][1]
[1][3][3][1][3][3][1][1][1][1][1][1][1][1][1]
[1][1][1][1][1][1][1][1][1][1][1][1][1][1][1]
[1][1][1][3][3][3][1][1][1][1][1][1][1][1][1]
[1][1][1][3][1][3][1][1][3][1][1][1][1][1][1]
[1][1][1][1][1][1][1][1][1][1][1][1][1][1][1]
[1][1][1][1][1][1][1][3][1][1][1][1][1][1][1]
[1][1][1][3][1][1][1][1][1][3][1][1][1][1][1]
 
'''
