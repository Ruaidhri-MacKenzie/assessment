"""
Quidditch game prototype v1.0
By Ruaidhri MacKenzie 2020
For Weasleys’ Wizard Wheezes
OOP All Outcomes Assessment
"""

"""sys package allows for clean exit with sys.exit()."""
import sys

"""pygame package will handle events and rendering."""
import pygame

"""Pitch is a class which creates a playing field for the game to take place."""
from pitch import Pitch

"""Player is a class which creates Seekers that the players will control."""
from player import Player

"""GoldenSnitch is a class which extends the Ball class, it creates a Golden Snitch that can move around the level."""
from golden_snitch import GoldenSnitch

class Game:
	"""Top Level Class."""

	def __init__(self):
		"""Constructor method for the top level class. Initialises pygame and loads sprites and text."""
		self.title = "Quidditch"
		self.width = 400
		self.height = 400
		self.tile_size = 32
		self.fps = 60
		self.background = (0, 0, 0)
		self.text_colour = (255, 255, 255)

		self.level = 1

		# Each level is defined with a 2d array of values. 0 is a floor, 1 is a wall
		self.level1_layout = [
			[1, 1, 1, 1, 1, 1, 1, 1, 1],
			[1, 1, 0, 0, 0, 0, 0, 1, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 1, 0, 0, 0, 0, 0, 1, 1],
			[1, 1, 1, 1, 1, 1, 1, 1, 1],
		]
		self.level2_layout = [
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
			[1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
			[1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		]
		self.player1_score = 10
		self.player2_score = 10

		# Initialise pygame and setup the screen to display
		pygame.init()
		pygame.display.set_caption(self.title)
		self.screen = pygame.display.set_mode((self.width, self.height))

		# Define standard font
		try:
			self.font = pygame.font.SysFont("Verdana", 30)
		except:
			self.font = pygame.font.SysFont(None, 30)
		
		# Load images
		self.player1_image = pygame.image.load("./assets/player1.png")
		self.player2_image = pygame.image.load("./assets/player2.png")
		self.golden_snitch_image = pygame.image.load("./assets/golden_snitch.png")
		self.wall_image = pygame.image.load("./assets/wall.png")
		self.floor_image = self.createBlankImage(self.tile_size)

		# Create a sprite group which will be responsible for rendering the sprites
		self.sprites = pygame.sprite.Group()

		# Create game objects - A pitch, 2 players and a golden snitch
		self.pitch = Pitch(self.floor_image, self.wall_image, 0, 0, self.tile_size, self.level1_layout)
		self.pitch.render()
		self.player1 = Player(self.sprites, self.player1_image, 1, 2, self.tile_size)
		self.player2 = Player(self.sprites, self.player2_image, 6, 5, self.tile_size)
		self.golden_snitch = GoldenSnitch(self.sprites, self.golden_snitch_image, 4, 3, self.tile_size)

		# Start the game loop. Check for events and draw to screen
		self.clock = pygame.time.Clock()
		while True:
			self.clock.tick(self.fps)	# Set frame rate
			self.eventHandler()				# Check for events
			self.draw()								# Draw to screen

	def createBlankImage(self, tile_size):
		"""Create a transparent image of a given tile size."""
		return pygame.Surface((tile_size, tile_size), pygame.SRCALPHA, 32).convert_alpha()
	
	def eventHandler(self):
		"""Checks for system events such as keyboard presses."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.quit()
				elif event.key == pygame.K_a:					# Player 1 Left
					self.movePlayerLeft(self.player1)
				elif event.key == pygame.K_d:					# Player 1 Right
					self.movePlayerRight(self.player1)
				elif event.key == pygame.K_w:					# Player 1 Up
					self.movePlayerUp(self.player1)
				elif event.key == pygame.K_s:					# Player 1 Down
					self.movePlayerDown(self.player1)
				elif event.key == pygame.K_j:					# Player 2 Left
					self.movePlayerLeft(self.player2)
				elif event.key == pygame.K_l:					# Player 2 Right
					self.movePlayerRight(self.player2)
				elif event.key == pygame.K_i:					# Player 2 Up
					self.movePlayerUp(self.player2)
				elif event.key == pygame.K_k:					# Player 2 Down
					self.movePlayerDown(self.player2)
	
	def draw(self):
		"""Redraws the screen with the updated sprite positions and text."""
		# Clear the screen
		self.screen.fill(self.background)

		# Draw the Pitch and Sprites
		self.pitch.draw(self.screen)
		self.sprites.draw(self.screen)

		# Draw Text
		self.player1_score_text = self.font.render(f"Player 1: {self.player1_score - self.player1.getMoveCounter()}", True, self.text_colour)
		self.player2_score_text = self.font.render(f"Player 2: {self.player2_score - self.player2.getMoveCounter()}", True, self.text_colour)
		self.screen.blit(self.player1_score_text, (20, 300))
		self.screen.blit(self.player2_score_text, (20, 350))

		# Update the display to show the changes
		pygame.display.flip()

	def quit(self):
		"""Clean shutdown of the game."""
		pygame.quit()
		sys.exit()

	def isSnitch(self, x, y):
		"""Check whether a co-ordinate contains a Golden Snitch."""
		return self.golden_snitch.getX() == x and self.golden_snitch.getY() == y

	def isPlayer(self, x, y):
		"""Check whether a co-ordinate contains a Player."""
		return (self.player1.getX() == x and self.player1.getY() == y) or (self.player2.getX() == x and self.player2.getY() == y)

	def movePlayerLeft(self, player):
		"""Move a player left, checking for walls, the world bounds, and the Golden Snitch."""
		player.turnLeft()
		if self.pitch.isFloor(player.getX() - 1, player.getY()):
			player.moveLeft()
			self.checkForSnitch(player)

	def movePlayerRight(self, player):
		"""Move a player right, checking for walls, the world bounds, and the Golden Snitch."""
		player.turnRight()
		if self.pitch.isFloor(player.getX() + 1, player.getY()):
			player.moveRight()
			self.checkForSnitch(player)

	def movePlayerUp(self, player):
		"""Move a player up, checking for walls, the world bounds, and the Golden Snitch."""
		if self.pitch.isFloor(player.getX(), player.getY() - 1):
			player.moveUp()
			self.checkForSnitch(player)

	def movePlayerDown(self, player):
		"""Move a player down, checking for walls, the world bounds, and the Golden Snitch."""
		if self.pitch.isFloor(player.getX(), player.getY() + 1):
			player.moveDown()
			self.checkForSnitch(player)
	
	def moveSnitch(self):
		"""Move the Golden Snitch in a random direction, checking for walls, the world bounds, and Players."""
		x, y = self.golden_snitch.getRandomDirection()
		if self.pitch.isFloor(x, y) and not self.isPlayer(x, y):
			self.golden_snitch.setPosition(x, y)

	def checkForSnitch(self, player):
		"""Check if a player has moved onto the Golden Snitch, catching it. Add 150 to their team's score and load the next level."""
		if self.isSnitch(player.getX(), player.getY()):
			if self.player1 == player:
				self.player1_score += 150
			else:
				self.player2_score += 150
			self.loadNextLevel()
		else:
			if self.level > 1:
				self.moveSnitch()

	def loadNextLevel(self):
		"""Load the layout for the next level and reposition the Players and Golden Snitch. If all levels have been played then exit the game."""
		self.level += 1
		if self.level == 2:
			self.pitch.loadTiles(self.level2_layout)
			self.player1.setPosition(1, 2)
			self.player2.setPosition(8, 7)
			self.golden_snitch.setPosition(5, 4)
		else:
			self.quit()


def main():
	"""Main driver function for this module. Creates an instance of the Game class."""
	game = Game()

if __name__ == "__main__":
	main()
