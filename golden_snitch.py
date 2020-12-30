"""random package allows us to use a random number generator."""
import random

"""Ball is an abstract class which this class will extend with the ability to move in a random direction."""
from ball import Ball

class GoldenSnitch(Ball):
	"""Creates a ball which can move around the pitch randomly."""

	def __init__(self, group, image, x, y, tile_size):
		"""Constructor method for GoldenSnitch class. Calls the constructor method for the parent class."""
		super().__init__(group, image, x, y, tile_size)

	def getRandomDirection(self):
		"""Return a co-ordinate which is either left, right, up, or down of the Golden Snitch."""
		x = self.x
		y = self.y

		# Get a random number between 0 and 3 inclusive: (0, 1, 2, 3)
		direction = random.randint(0, 3)
		if direction == 0:
			x -= 1							# Move Left
		elif direction == 1:
			x += 1							# Move Right
		elif direction == 2:
			y -= 1							# Move Up
		else:
			y += 1							# Move Down
		
		# Return the co-ordinates as a tuple.
		return (x, y)
