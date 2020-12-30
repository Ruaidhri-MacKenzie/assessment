"""pygame package will allow access to the Sprite class."""
import pygame

class Ball:
	"""Abstract class from which different balls will be created."""

	def __init__(self, group, image, x, y, tile_size):
		"""Constructor method for Ball class. Defines a sprite and position."""
		self.x = x
		self.y = y
		self.sprite = pygame.sprite.Sprite(group)
		self.sprite.image = image
		self.sprite.rect = image.get_rect(x = x * tile_size, y = y * tile_size)
		self.tile_size = tile_size

	def setPosition(self, x, y):
		"""Set the ball's co-ordinates."""
		self.x = x
		self.y = y
		self.sprite.rect = self.sprite.image.get_rect(x = x * self.tile_size, y = y * self.tile_size)
	
	def moveLeft(self):
		"""Move the ball to the left."""
		self.setPosition(self.x - 1, self.y)
	
	def moveRight(self):
		"""Move the ball to the right."""
		self.setPosition(self.x + 1, self.y)
	
	def moveUp(self):
		"""Move the ball up."""
		self.setPosition(self.x, self.y - 1)
	
	def moveDown(self):
		"""Move the ball down."""
		self.setPosition(self.x, self.y + 1)

	def getX(self):
		"""Returns the balls's X co-ordinate."""
		return self.x
	
	def getY(self):
		"""Returns the balls's Y co-ordinate."""
		return self.y
	