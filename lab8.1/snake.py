# Imports
import pygame
import time
import random
import sys

# Initializing
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 500))

# Setting FPS
FPS = 60
clock = pygame.time.Clock()

# Program global vars
GREEN = (100, 200, 100)
BLACK = (0, 0, 0)
score = 0
score_apple_check = 0
apple_collected = 0
new_apple = 1
score_apple = 0
apple_difficulty = 0
level = 1
snake_length = 1
all_snake = []
direction = 0
previous_key = 0
speed = 3
running = True
x = 100
y = 80

# Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("GAME OVER", True, BLACK)


# Class for apples
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\akim0\Desktop\pygame\lab8.1\apple.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25))

    def move(self):
        global new_apple
        global apple_collected
        if not new_apple:
            apple_collected = 0
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25))
            new_apple = 1


# Class for snake parts
class SnakePart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def move(self, all_snake):
        for part in all_snake:
            pygame.draw.rect(screen, GREEN, [part[0], part[1], 20, 20])
        self.rect = pygame.Rect(x, y, 20, 20)


# Function for quitting after game over
def game_over():
    time.sleep(1/3)
    screen.fill((240, 80, 90))
    screen.blit(game_over_text, (235, 200))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Creating objects of sprites
apple_sprite = Apple()
apples = pygame.sprite.Group()
apples.add(apple_sprite)
snake_head = SnakePart()
snake_parts = pygame.sprite.Group()
snake_parts.add(snake_head)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and previous_key != pygame.K_s:
                y -= 20
                previous_key = pygame.K_w
                direction = "up"
            elif event.key == pygame.K_a and previous_key != pygame.K_d:
                x -= 20
                previous_key = pygame.K_a
                direction = "left"
            elif event.key == pygame.K_s and previous_key != pygame.K_w:
                y += 20
                previous_key = pygame.K_s
                direction = "down"
            elif event.key == pygame.K_d and previous_key != pygame.K_a:
                x += 20
                previous_key = pygame.K_d
                direction = "right"

    screen.fill((255, 255, 100))

    score_text = font_small.render("Score: " + str(score_apple), True, BLACK)
    screen.blit(score_text, (800 - 110, 10))
    level_text = font_small.render("Level: " + str(level), True, BLACK)
    screen.blit(level_text, (10, 10))

    snake_head.move(all_snake)
    apple_sprite.move()

    if direction == "down":
        y += speed
    elif direction == "up":
        y -= speed
    elif direction == "left":
        x -= speed
    elif direction == "right":
        x += speed

    if y >= 480 or y <= 0 or x >= 780 or x <= 0:
        game_over()
    for part in all_snake[:-1]:
        if x == part[0] and y == part[1]:
            game_over()

    current_head = [x, y]
    all_snake.append(current_head)

    if len(all_snake) > snake_length:
        del all_snake[0]

    if pygame.sprite.spritecollideany(snake_head, apples):
        apple_collected = 1
        snake_length += 1

    if score_apple % 4 == 0 and score_apple - apple_difficulty != 0:
        FPS += 10
        level += 1
        apple_difficulty += 4

    if not apple_collected:
        for entity in apples:
            screen.blit(entity.image, entity.rect)
    else:
        if new_apple == 1:
            score_apple += 1
            new_apple = 0

    clock.tick(FPS)
    pygame.display.update()
