import pygame
from ball import Ball

sprite_group = pygame.sprite.Group()
ball_image = pygame.image.load("./assets/golden_snitch.png")
x = 5
y = 5
tile_size = 32

ball = Ball(sprite_group, ball_image, x, y, tile_size)

test1 = "Pass" if ball.x == x else "Fail"
print(f"1. ball.x initialises correctly: {test1}")

test2 = "Pass" if ball.y == y else "Fail"
print(f"2. ball.y initialises correctly: {test2}")

ball.moveLeft()

test3 = "Pass" if ball.x == x - 1 else "Fail"
print(f"3. ball.moveLeft(): {test3}")

ball.moveRight()

test4 = "Pass" if ball.x == x else "Fail"
print(f"4. ball.moveRight(): {test4}")

ball.moveUp()

test5 = "Pass" if ball.y == y - 1 else "Fail"
print(f"5. ball.moveUp(): {test5}")

ball.moveDown()

test6 = "Pass" if ball.y == y else "Fail"
print(f"6. ball.moveDown(): {test6}")

ball.setPosition(3, 4)

test7 = "Pass" if ball.getX() == 3 else "Fail"
print(f"7. ball.getX(): {test7}")

test8 = "Pass" if ball.getY() == 4 else "Fail"
print(f"8. ball.getY(): {test8}")
