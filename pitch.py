import pygame

class Pitch:
	def __init__(self, floor_image, wall_image, x, y, tile_size, tiles):
		self.x = x
		self.y = y
		self.tile_images = [floor_image, wall_image]
		self.tile_size = tile_size
		self.tiles = tiles
		self.render()

	def getWidth(self):
		return len(self.tiles[0])
	
	def getHeight(self):
		return len(self.tiles)
	
	def isInBounds(self, x, y):
		return (x >= 0 and x < self.getWidth()) and (y >= 0 and y < self.getHeight())
	
	def isWall(self, x, y):
		return self.tiles[y][x] == 1
	
	def isFloor(self, x, y):
		return self.isInBounds(x, y) and not self.isWall(x, y)

	def loadTiles(self, tiles):
		self.tiles = tiles
		self.render()
		
	def render(self):
		columns = len(self.tiles[0])
		rows = len(self.tiles)

		self.image = pygame.Surface((columns * self.tile_size, rows * self.tile_size), pygame.SRCALPHA, 32).convert_alpha()
		for y in range(rows):
			for x in range(columns):
				self.image.blit(self.tile_images[self.tiles[y][x]], (x * self.tile_size, y * self.tile_size))

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))
