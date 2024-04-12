import pygame
import time
import random
import sys

# Initialize pygame
pygame.init()

# Create the game screen
screen = pygame.display.set_mode((800, 500))

# Set the Frames Per Second
FPS = 60
clock = pygame.time.Clock()

# Colors
GREEN = (100, 200, 100)
BLACK = (0, 0, 0)

# Game variables
score_fruits = 0
apple_collected = 0
new_apple = 1
score_pear_check = 0
pear_collected = 0
new_pear = 1
score_banana_check = 0
banana_collected = 0
new_banana = 1
banana_time = 0
no_banana_time = 0
score_for_levelup = 4
next_level_score = 8
current_level = 1
snake_length = 1
snake_positions = []
snake_direction = 0
last_key = 0
music_played = 0
snake_speed = 3
running = True
snake_x = 100
snake_y = 80

# Load fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("GAME OVER", True, BLACK)


# Class for apples
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\akim0\Desktop\pygame\lab8.1\apple.png')
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


# Class for pears
class Pear(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\akim0\Desktop\pygame\lab9\pear.png')
        self.image = pygame.transform.scale(self.image, (30, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25))

    def move(self):
        global new_pear
        global pear_collected
        if not new_pear:
            pear_collected = 0
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25))
            new_pear = 1


# Class for bananas
class Banana(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\akim0\Desktop\pygame\lab9\Banana.png')
        self.image = pygame.transform.scale(self.image, (20, 25))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25))

    def move(self):
        global new_banana
        global banana_collected
        if not new_banana:
            banana_collected = 0
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25))
            new_banana = 1


# Class for snake parts
class SnakePart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

    def move(self, snake_positions):
        for position in snake_positions:
            pygame.draw.rect(screen, GREEN, [position[0], position[1], 20, 20])
        self.rect = pygame.Rect(snake_x, snake_y, 20, 20)


# Function to quit the game after game over
def quit_game():
    time.sleep(1/3)
    screen.fill((240, 80, 90))
    screen.blit(game_over_text, (235, 200))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Play music
def play_music():
    pygame.mixer.music.load(r'C:\Users\akim0\Desktop\pygame\lab8.1\lab8_snake_resources_background.wav')
    pygame.mixer.music.play(-1)


# Stop music
def stop_music():
    pygame.mixer.music.stop()


# Create objects
apple_obj = Apple()
apples = pygame.sprite.Group()
apples.add(apple_obj)

pear_obj = Pear()
pears = pygame.sprite.Group()
pears.add(pear_obj)

banana_obj = Banana()
bananas = pygame.sprite.Group()
bananas.add(banana_obj)

snake_head = SnakePart()
snake_parts = pygame.sprite.Group()
snake_parts.add(snake_head)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and last_key != pygame.K_DOWN:
                snake_y -= 20
                last_key = pygame.K_UP
                snake_direction = "up"
            elif event.key == pygame.K_DOWN and last_key != pygame.K_UP:
                snake_y += 20
                last_key = pygame.K_DOWN
                snake_direction = "down"
            elif event.key == pygame.K_LEFT and last_key != pygame.K_RIGHT:
                snake_x -= 20
                last_key = pygame.K_LEFT
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT and last_key != pygame.K_LEFT:
                snake_x += 20
                last_key = pygame.K_RIGHT
                snake_direction = "right"

    if not music_played:
        play_music()
        music_played = 1

    screen.fill((255, 255, 100))

    score_text = font_small.render("Score: " + str(score_fruits), True, BLACK)
    screen.blit(score_text, (800 - 110, 10))
    level_text = font_small.render("Level: " + str(current_level), True, BLACK)
    screen.blit(level_text, (10, 10))

    snake_head.move(snake_positions)
    apple_obj.move()
    pear_obj.move()
    banana_obj.move()

    if snake_direction == "down":
        snake_y += snake_speed
    elif snake_direction == "up":
        snake_y -= snake_speed
    elif snake_direction == "left":
        snake_x -= snake_speed
    elif snake_direction == "right":
        snake_x += snake_speed

    if snake_y >= 480 or snake_y <= 0 or snake_x >= 780 or snake_x <= 0:
        quit_game()
    for pos in snake_positions[:-1]:
        if [snake_x, snake_y] == pos:
            quit_game()

    current_head = [snake_x, snake_y]
    snake_positions.append(current_head)

    if len(snake_positions) > snake_length:
        del snake_positions[0]

    if pygame.sprite.spritecollideany(snake_head, apples):
        apple_collected = 1
        snake_length += 1

    if pygame.sprite.spritecollideany(snake_head, pears):
        pear_collected = 1
        snake_length += 1

    if pygame.sprite.spritecollideany(snake_head, bananas):
        if no_banana_time < 240:
            banana_collected = 1
            snake_length += 1

    if score_fruits >= score_for_levelup and score_fruits < next_level_score:
        FPS += 10
        current_level += 1
        score_for_levelup += 4
        next_level_score += 4

    if not apple_collected:
        for entity in apples:
            screen.blit(entity.image, entity.rect)
    else:
        if new_apple == 1:
            score_fruits += 1
            new_apple = 0

    if not pear_collected:
        for entity in pears:
            screen.blit(entity.image, entity.rect)
    else:
        if new_pear == 1:
            score_fruits += 4
            new_pear = 0

    if not banana_collected:
        if no_banana_time < 240:
            for entity in bananas:
                screen.blit(entity.image, entity.rect)
                no_banana_time += 1
        else:
            if no_banana_time < 600:
                no_banana_time += 1
            else:
                no_banana_time = 0

    else:
        no_banana_time = 240
        if new_banana == 1:
            score_fruits += 2
            new_banana = 0

    pygame.display.update()
    clock.tick(FPS)
