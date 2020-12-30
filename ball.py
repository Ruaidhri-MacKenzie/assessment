import pygame

class Ball:
	def __init__(self, group, image, x, y, tile_size):
		self.x = x
		self.y = y
		self.sprite = pygame.sprite.Sprite(group)
		self.sprite.image = image
		self.sprite.rect = image.get_rect(x = x * tile_size, y = y * tile_size)
		self.tile_size = tile_size

	def setPosition(self, x, y):
		self.x = x
		self.y = y
		self.sprite.rect = self.sprite.image.get_rect(x = x * self.tile_size, y = y * self.tile_size)
	
	def moveLeft(self):
		self.setPosition(self.x - 1, self.y)
	
	def moveRight(self):
		self.setPosition(self.x + 1, self.y)
	
	def moveUp(self):
		self.setPosition(self.x, self.y - 1)
	
	def moveDown(self):
		self.setPosition(self.x, self.y + 1)

	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
	