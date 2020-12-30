import pygame

class Player:
	def __init__(self, group, image, x, y, tile_size):
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
		self.x = x
		self.y = y
		self.sprite.rect = self.sprite.image.get_rect(x = x * self.tile_size, y = y * self.tile_size)
	
	def moveLeft(self):
		self.setPosition(self.x - 1, self.y)
		self.move_counter += 1
	
	def moveRight(self):
		self.setPosition(self.x + 1, self.y)
		self.move_counter += 1
	
	def moveUp(self):
		self.setPosition(self.x, self.y - 1)
		self.move_counter += 1
	
	def moveDown(self):
		self.setPosition(self.x, self.y + 1)
		self.move_counter += 1

	def turnLeft(self):
		self.sprite.image = self.image_left

	def turnRight(self):
		self.sprite.image = self.image_right
	