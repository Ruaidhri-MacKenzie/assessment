"""pygame package will allow access to the Sprite class."""
import pygame

class Player:
	"""Creates a character which is controllered by a player."""

	def __init__(self, group, image, x, y, tile_size):
		"""Constructor method for Player class. Defines an image and position."""
		self.x = x
		self.y = y
		self.sprite = pygame.sprite.Sprite(group)
		self.image_left = image
		self.image_right = pygame.transform.flip(image, True, False)

		self.sprite.image = self.image_right
		self.sprite.rect = image.get_rect(x = x * tile_size, y = y * tile_size)
		self.tile_size = tile_size

		self.move_counter = 0

	def setPosition(self, x, y):
		"""Set the player's co-ordinates."""
		self.x = x
		self.y = y
		self.sprite.rect = self.sprite.image.get_rect(x = x * self.tile_size, y = y * self.tile_size)
	
	def moveLeft(self):
		"""Move the player to the left and increase the move counter."""
		self.setPosition(self.x - 1, self.y)
		self.move_counter += 1
	
	def moveRight(self):
		"""Move the player to the right and increase the move counter."""
		self.setPosition(self.x + 1, self.y)
		self.move_counter += 1
	
	def moveUp(self):
		"""Move the player up and increase the move counter."""
		self.setPosition(self.x, self.y - 1)
		self.move_counter += 1
	
	def moveDown(self):
		"""Move the player down and increase the move counter."""
		self.setPosition(self.x, self.y + 1)
		self.move_counter += 1

	def turnLeft(self):
		"""Turn the player to the left."""
		self.sprite.image = self.image_left

	def turnRight(self):
		"""Turn the player to the right."""
		self.sprite.image = self.image_right
	
	def getX(self):
		"""Returns the player's X co-ordinate."""
		return self.x
	
	def getY(self):
		"""Returns the player's Y co-ordinate."""
		return self.y
	
	def getMoveCounter(self):
		"""Returns the player's move counter."""
		return self.move_counter
