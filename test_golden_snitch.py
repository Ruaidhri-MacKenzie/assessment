import pygame
from golden_snitch import GoldenSnitch

sprite_group = pygame.sprite.Group()
golden_snitch_image = pygame.image.load("./assets/golden_snitch.png")
x = 5
y = 5
tile_size = 32

golden_snitch = GoldenSnitch(sprite_group, golden_snitch_image, x, y, tile_size)

print("==Golden Snitch Unit Test==")

test1 = "Pass" if golden_snitch.x == x else "Fail"
print(f"1. golden_snitch.x initialises correctly: {test1:>12}")

test2 = "Pass" if golden_snitch.y == y else "Fail"
print(f"2. golden_snitch.y initialises correctly: {test2:>12}")

random_x, random_y = golden_snitch.getRandomDirection()
x_distance = abs(random_x - x)
y_distance = abs(random_y - y)

test3 = "Pass" if (x_distance == 1 and y_distance == 0) or (x_distance == 0 and y_distance == 1) else "Fail"
print(f"3. Return random direction within a single move: {test3:>5}")
