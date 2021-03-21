import pygame
from pitch import Pitch

x = 0
y = 0
tile_size = 32
level_layout = [
	[1, 1],
	[0, 0],
]

floor_image = pygame.image.load("./assets/wall.png")
wall_image = pygame.image.load("./assets/wall.png")

pitch = Pitch(floor_image, wall_image, x, y, tile_size, level_layout)

test1 = "Pass" if pitch.x == x else "Fail"
print(f"1. pitch.x initialises correctly: {test1}")

test2 = "Pass" if pitch.y == y else "Fail"
print(f"2. pitch.y initialises correctly: {test2}")

test3 = "Pass" if pitch.getWidth() == 2 else "Fail"
print(f"3. pitch.getWidth(): {test3}")

test4 = "Pass" if pitch.getHeight() == 2 else "Fail"
print(f"4. pitch.getHeight(): {test4}")

test5 = "Pass" if pitch.isInBounds(1, 1) else "Fail"
print(f"5. pitch.isInBounds(): {test5}")

test6 = "Pass" if pitch.isWall(1, 0) else "Fail"
print(f"6. pitch.isWall(): {test6}")

test7 = "Pass" if pitch.isFloor(0, 1) else "Fail"
print(f"7. pitch.isFloor(): {test7}")
