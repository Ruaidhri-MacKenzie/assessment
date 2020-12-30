import sys
import pygame
from pitch import Pitch
from player import Player
from golden_snitch import GoldenSnitch

# Top Level Class
class Game:
	def __init__(self):
		self.title = "Quidditch"
		self.width = 800
		self.height = 600
		self.tile_size = 32
		self.fps = 60
		self.background = (0, 0, 0)

		self.level = 1
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
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		]

		pygame.init()
		pygame.display.set_caption(self.title)
		self.screen = pygame.display.set_mode((self.width, self.height))

		self.player1_image = pygame.image.load("./assets/player1.png")
		self.player2_image = pygame.image.load("./assets/player2.png")
		self.golden_snitch_image = pygame.image.load("./assets/golden_snitch.png")
		self.wall_image = pygame.image.load("./assets/wall.png")

		self.sprites = pygame.sprite.Group()

		self.pitch = Pitch(self.wall_image, 0, 0, self.tile_size, self.level1_layout)
		self.player1 = Player(self.sprites, self.player1_image, 1, 2, self.tile_size)
		self.player2 = Player(self.sprites, self.player2_image, 6, 5, self.tile_size)
		self.golden_snitch = GoldenSnitch(self.sprites, self.golden_snitch_image, 4, 3, self.tile_size)

		self.clock = pygame.time.Clock()
		while True:
			self.clock.tick(self.fps)	# Set frame rate
			self.eventHandler()				# Check for events
			self.draw()								# Draw to screen

	def eventHandler(self):
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
		self.screen.fill(self.background)
		self.pitch.draw(self.screen)
		self.sprites.draw(self.screen)
		pygame.display.flip()

	def quit(self):
		pygame.quit()
		sys.exit()

	def isSnitch(self, x, y):
		return self.golden_snitch.x == x and self.golden_snitch.y == y

	def isPlayer(self, x, y):
		return (self.player1.x == x and self.player1.y == y) or (self.player2.x == x and self.player2.y == y)

	def movePlayerLeft(self, player):
		player.turnLeft()
		if self.pitch.isFloor(player.x - 1, player.y):
			player.moveLeft()
			self.checkForSnitch(player)

	def movePlayerRight(self, player):
		player.turnRight()
		if self.pitch.isFloor(player.x + 1, player.y):
			player.moveRight()
			self.checkForSnitch(player)

	def movePlayerUp(self, player):
		if self.pitch.isFloor(player.x, player.y - 1):
			player.moveUp()
			self.checkForSnitch(player)

	def movePlayerDown(self, player):
		if self.pitch.isFloor(player.x, player.y + 1):
			player.moveDown()
			self.checkForSnitch(player)
	
	def moveSnitch(self):
		x, y = self.golden_snitch.getRandomDirection()
		if self.pitch.isFloor(x, y) and not self.isPlayer(x, y):
			self.golden_snitch.setPosition(x, y)

	def checkForSnitch(self, player):
		if self.isSnitch(player.x, player.y):
			self.loadNextLevel()
		else:
			if self.level > 1:
				self.moveSnitch()

	def loadNextLevel(self):
		self.level += 1
		if self.level == 2:
			self.pitch.loadTiles(self.level2_layout)
			self.player1.setPosition(1, 2)
			self.player2.setPosition(8, 7)
			self.golden_snitch.setPosition(5, 4)
		else:
			self.quit()


def main():
	game = Game()

if __name__ == "__main__":
	main()
