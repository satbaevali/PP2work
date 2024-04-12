import pygame
import sys
from pygame.locals import *
import random
import time

# Initializing
pygame.init()

# Setting up FPS
fps = 60
clock = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 100, 100)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
screen_width = 400
screen_height = 600
speed = 5
score_enemy_passed = 0
score_coins = 0
coin_collected = 0
new_coin = 1
coin_score_check = 0
heavy_coin_collected = 0
new_heavy_coin = 1
heavy_coin_score_check = 0
music_played = 0
coin_visible = 1
heavy_coin_visible = 1

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Background
background = pygame.image.load(r"C:\Users\akim0\Desktop\pygame\lab8.1\AnimatedStreet.png")

# Create a white screen
screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)
pygame.display.set_caption("Game")

#creating enemy sprite 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\akim0\Desktop\pygame\lab8.1\Enemy.png") 
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(40, screen_width - 40), 0) 

    def move(self):
        global score_enemy_passed
        self.rect.move_ip(0, speed)
        if self.rect.bottom > 600:
            score_enemy_passed += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), 0) 

#creating player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\akim0\Desktop\pygame\lab8.1\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width:        
            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\akim0\Desktop\pygame\lab8.1\coin.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, screen_width - 30), 0)

    def move(self):
        global score_coins
        global coin_collected
        coin_collected = 0
        self.rect.move_ip(0, speed)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), 0)
            global coin_score_check
            coin_score_check = 0 
        if self.rect.bottom < 100:
            global new_coin
            new_coin = 1

class HeavyCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\akim0\Desktop\pygame\lab9\hev_coin.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, screen_width - 30), 0)

    def move(self):
        global score_coins
        global heavy_coin_collected
        self.rect.move_ip(0, speed)
        if self.rect.bottom > 650:
            self.rect.top = 0
            heavy_coin_collected = 0
            self.rect.center = (random.randint(30, screen_width - 30), 0) 
            global heavy_coin_score_check
            heavy_coin_score_check = 0
        if self.rect.bottom < 100:
            global new_heavy_coin
            new_heavy_coin = 1

def play_music():
    pygame.mixer.music.load(r"C:\Users\akim0\Desktop\pygame\lab8.1\lab8_racer_resources_background.wav")
    pygame.mixer.music.play(-1)


def stop_music():
    pygame.mixer.music.stop()

# Creating objects of sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()
HC1 = HeavyCoin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
heavy_coins = pygame.sprite.Group()
heavy_coins.add(HC1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 500) 

# Game Loop
while True:
    # Play music at the beginning
    if not music_played:
        play_music()
        music_played = 1

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.2
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Print background and scores
    screen.blit(background, (0, 0))
    score_enemy_display = font_small.render(str(score_enemy_passed), True, BLACK)
    screen.blit(score_enemy_display, (10, 10))
    score_coin_display = font_small.render("Coins: " + str(score_coins), True, BLACK)
    screen.blit(score_coin_display, (screen_width - 100, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect) 

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        stop_music()
        time.sleep(1/3) 
        pygame.mixer.Sound(r'C:\Users\akim0\Desktop\pygame\lab8.1\lab8_racer_resources_crash.wav').play() 
        time.sleep(1) 
        screen.fill(RED)
        screen.blit(game_over, (30, 250)) 
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Move coins
    C1.move()
    HC1.move()

    if pygame.sprite.spritecollideany(P1, coins):
        if coin_visible: 
            coin_score_check = 1 
            coin_collected = 1 

    if pygame.sprite.spritecollideany(P1, heavy_coins):
        if heavy_coin_visible: 
            heavy_coin_score_check = 1 
            heavy_coin_collected = 1 

    # Continue displaying coin if not
    if not coin_collected:
        if not pygame.sprite.spritecollideany(E1, coins):
            for entity in coins:
                screen.blit(entity.image, entity.rect)
                coin_visible = 1
        else:
            coin_visible = 0
    else:
        if coin_score_check == 1 and new_coin == 1:
            score_coins += 1
            new_coin = 0

    # Continue displaying coin if not
    if not heavy_coin_collected:
        if not pygame.sprite.spritecollideany(E1, heavy_coins):
            if not pygame.sprite.spritecollideany(C1, heavy_coins):
                for entity in heavy_coins:
                    screen.blit(entity.image, entity.rect)
                    heavy_coin_visible = 1
            else:
                heavy_coin_visible = 0
        else:
            heavy_coin_visible = 0
    else:
        if heavy_coin_score_check == 1 and new_heavy_coin == 1:
            score_coins += 3
            new_heavy_coin = 0
        
    pygame.display.update()
    clock.tick(fps)
