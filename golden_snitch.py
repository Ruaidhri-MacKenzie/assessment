import random
from ball import Ball

class GoldenSnitch(Ball):
	def __init__(self, group, image, x, y, tile_size):
		super().__init__(group, image, x, y, tile_size)

	def getRandomDirection(self):
		x = self.x
		y = self.y

		direction = random.randint(0, 3)
		if direction == 0:
			x -= 1
		elif direction == 1:
			x += 1
		elif direction == 2:
			y -= 1
		else:
			y += 1
		
		return (x, y)
