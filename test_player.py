import pygame
from player import Player

sprite_group = pygame.sprite.Group()
player1_image = pygame.image.load("./assets/player1.png")
x = 5
y = 5
tile_size = 32

player = Player(sprite_group, player1_image, x, y, tile_size)

test1 = "Pass" if player.x == x else "Fail"
print(f"1. player.x initialises correctly: {test1}")

test2 = "Pass" if player.y == y else "Fail"
print(f"2. player.y initialises correctly: {test2}")

player.moveLeft()

test3 = "Pass" if player.x == x - 1 else "Fail"
print(f"3. player.moveLeft(): {test3}")

player.moveRight()

test4 = "Pass" if player.x == x else "Fail"
print(f"4. player.moveRight(): {test4}")

player.moveUp()

test5 = "Pass" if player.y == y - 1 else "Fail"
print(f"5. player.moveUp(): {test5}")

player.moveDown()

test6 = "Pass" if player.y == y else "Fail"
print(f"6. player.moveDown(): {test6}")

player.turnLeft()

test7 = "Pass" if player.sprite.image == player.image_left else "Fail"
print(f"7. player.turnLeft(): {test7}")

player.turnRight()

test8 = "Pass" if player.sprite.image == player.image_right else "Fail"
print(f"8. player.turnRight(): {test8}")

player.setPosition(3, 4)

test9 = "Pass" if player.getX() == 3 else "Fail"
print(f"9. player.getX(): {test9}")

test10 = "Pass" if player.getY() == 4 else "Fail"
print(f"10. player.getY(): {test10}")

test11 = "Pass" if player.getMoveCounter() == 4 else "Fail"
print(f"11. player.getMoveCounter(): {test11}")
