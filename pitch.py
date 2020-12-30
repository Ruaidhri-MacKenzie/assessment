"""pygame package will allow access to the Surface class."""
import pygame

class Pitch:
	"""Creates a playing field for the game to take place. Defines walls and world bounds."""

	def __init__(self, floor_image, wall_image, x, y, tile_size, tiles):
		"""Constructor method for Pitch class. Loads a 2d array of tile values and renders and image from these values."""
		self.x = x
		self.y = y
		self.tile_images = [floor_image, wall_image]
		self.tile_size = tile_size
		self.tiles = tiles
		self.render()

	def getWidth(self):
		"""Return the number of tiles that the pitch is wide."""
		return len(self.tiles[0])
	
	def getHeight(self):
		"""Return the number of tiles that the pitch is tall."""
		return len(self.tiles)
	
	def isInBounds(self, x, y):
		"""Return whether a co-ordinate is within the world bounds."""
		return (x >= 0 and x < self.getWidth()) and (y >= 0 and y < self.getHeight())
	
	def isWall(self, x, y):
		"""Return whether a co-ordinate is a wall tile."""
		return self.tiles[y][x] == 1
	
	def isFloor(self, x, y):
		"""Return whether a co-ordinate is a floor tile."""
		return self.isInBounds(x, y) and not self.isWall(x, y)

	def loadTiles(self, tiles):
		"""Load a new tile layout and re-render the pitch image."""
		self.tiles = tiles
		self.render()
		
	def render(self):
		"""Create an image of the pitch from the floor_image, wall_image, and tile values"""
		columns = self.getWidth()
		rows = self.getHeight()

		# Create a blank image the full size of the pitch.
		self.image = pygame.Surface((columns * self.tile_size, rows * self.tile_size), pygame.SRCALPHA, 32).convert_alpha()

		# Loop for sections of the blank image, pasting on floor or wall images depending on the tile value for that co-ordinate.
		for y in range(rows):
			for x in range(columns):
				self.image.blit(self.tile_images[self.tiles[y][x]], (x * self.tile_size, y * self.tile_size))

	def draw(self, screen):
		"""Draw the pitch image to the screen."""
		screen.blit(self.image, (self.x, self.y))
