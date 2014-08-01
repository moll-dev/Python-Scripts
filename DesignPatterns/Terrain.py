#!/usr/bin/env python
import random, copy

height = 20
width = 40
terrain = [[0 for x in xrange(width)] for x in xrange(height)]

class Terrain:
	def __init__(self):
		self.grass_template = Grass()
		self.mountain_template = Mountain()
		self.marsh_template = Marsh()
		self.river_template = River()
		self.grid = [[self.grass_template for x in xrange(width)] for x in xrange(height)]

	def __str__(self):
		string = ''
		for row in self.grid:
			for col in row:
				string += str(col)
			string += '\n'
		return string

	def gen_marsh(self):
		marshes = [{'vec':Vector2(random.randint(0,height-1), random.randint(0,width-1)),
					'size':random.randint(0,3)} for x in range(5)]

		for marsh in marshes:
			self.grid[marsh['vec'].x][marsh['vec'].y] = self.marsh_template
			for x in range(marsh['size']):
				self.paint_circle(marsh['vec'].x, marsh['vec'].y, x-1, self.marsh_template)

	def gen_mountain(self):
		seed = Vector2(random.randint(0,height-1), random.randint(0,width-1))
		cursor = copy.copy(seed)
		dist = random.randint(0,40)

		self.grid[seed.x][seed.y] = self.mountain_template

		for x in range(dist):
			direction = random.randint(0,8)
			cursor.move(direction)
			self.paint_pixel(cursor.x, cursor.y, self.mountain_template)

	def gen_mountain_range(self, freq):
		for x in range(freq):
			self.gen_mountain()

	def gen_river(self):
		seed = Vector2(random.randint(0,height-1), random.randint(0,width-1))
		cursor = copy.copy(seed)
		dist = random.randint(0,40)

		self.grid[seed.x][seed.y] = self.river_template

		for x in range(dist):
			if x % 3:
				cursor.move(direction)

			direction = random.randint(0,8)
			self.paint_circle(cursor.x, cursor.y, 2, self.river_template)

	def paint_pixel(self, x, y, tile):
		try:
			self.grid[x][y] = tile
		except:
			#Meaning we hit a boundary, ignore it.
			pass

	def paint_circle(self, x0, y0, radius, tile):
		f = 1 - radius
		ddf_x = 1
		ddf_y = -2 * radius
		x = 0
		y = radius
		self.paint_pixel(x0, y0 + radius, tile)
		self.paint_pixel(x0, y0 - radius, tile)
		self.paint_pixel(x0 + radius, y0, tile)
		self.paint_pixel(x0 - radius, y0, tile)

		while x < y:
			if f >= 0:
				y -= 1
				ddf_y += 2
				f += ddf_y
			x += 1
			ddf_x += 2
			f += ddf_x
			self.paint_pixel(x0 + x, y0 + y, tile)
			self.paint_pixel(x0 - x, y0 + y, tile)
			self.paint_pixel(x0 + x, y0 - y, tile)
			self.paint_pixel(x0 - x, y0 - y, tile)
			self.paint_pixel(x0 + y, y0 + x, tile)
			self.paint_pixel(x0 - y, y0 + x, tile)
			self.paint_pixel(x0 + y, y0 - x, tile)
			self.paint_pixel(x0 - y, y0 - x, tile)


class Vector2:
	def __init__(self, x, y):
		self.x, self.y = x, y

	def move(self, direction):
		if direction == 1:
			self.y+=1
		if direction == 2:
			self.y+=1
			self.x+=1
		if direction == 3:
			self.x+=1
		if direction == 4:
			self.y-=1
			self.x+-1
		if direction == 5:
			self.y-=1
		if direction == 6:
			self.y-=1
			self.x-=1
		if direction == 7:
			self.x-=1
		if direction == 8:
			self.x-=1
			self.y+=1

class Tile:
	def __str__(self):
		return self.symbol

class Grass(Tile):
	def __init__(self):
		self.name = 'Grass'
		self.symbol = ','

class Mountain(Tile):
	def __init__(self):
		self.name = 'Mountain'
		self.symbol = '^'

class Marsh(Tile):
	def __init__(self):
		self.name = 'Marsh'
		self.symbol = '#'

class River(Tile):
	def __init__(self):
		self.name = 'River'
		self.symbol = '~'


world = Terrain()

world.gen_marsh()
world.gen_mountain_range(10)
world.gen_river()

print world

#world.gen_marsh()
