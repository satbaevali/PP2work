import pygame
from pygame.locals import *
import random

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car")

gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

speed = 2
score = 0
coin_collected = 0  # Fixed variable name

marker_width = 10
marker_height = 50

road = (100, 0, 300, height)
left_edge_markers = (95, 0, marker_width, height)
right_edge_markers = (395, 0, marker_width, height)

left_lane = 150
right_lane = 350
centr_lane = 250
lanes = [left_lane, centr_lane, right_lane]

lane_marker_move_y = 0

class vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class Playervvehicle(vehicle):
    def __init__(self, x, y):
        image = pygame.image.load('car.png')
        super().__init__(image, x, y)

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):  # Add x and y arguments
        super().__init__() 
        self.image = pygame.image.load('lab8/coin.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//40, self.image.get_height()//40))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Initialize position using x and y arguments

player_x = 250
player_y = 400

player_group = pygame.sprite.Group()
player = Playervvehicle(player_x, player_y)
player_group.add(player)

image_filenames = ['lab8/pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
Vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load(image_filename)
    Vehicle_images.append(image)

vehicle_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

# load the crash image
crash = pygame.image.load('crash.png')
crash_rect = crash.get_rect()
clock = pygame.time.Clock()
fps = 120
running = True
gameover = False

def spawn_coins():
    global coin_collected  # Use the correct variable name
    if random.randint(0, 100) < 20:  # Increase the chance of spawning coins
        coin_x = random.randint(left_lane + 45, right_lane - 45)
        coin_y = random.randint(-100, -50)
        coin = Coin(coin_x, coin_y)
        coin_group.add(coin)  # Add the coin to the coin_group

while running:
    clock.tick(fps)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == KEYDOWN:
            if e.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif e.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100

            # check if there's a side swipe collision
            for Vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, Vehicle):
                    gameover = True

                    if e.key == K_LEFT:
                        player.rect.left = Vehicle.rect.right
                        crash_rect.center = [player.rect.left, (player.rect.center[1] + Vehicle.rect.center[1]) / 2]
                    if e.key == K_RIGHT:
                        player.rect.left = Vehicle.rect.left
                        crash_rect.center = [player.rect.right, (player.rect.center[1] + Vehicle.rect.center[1]) / 2]

    screen.fill(green)
    pygame.draw.rect(screen, gray, road)
    pygame.draw.rect(screen, yellow, left_edge_markers)
    pygame.draw.rect(screen, yellow, right_edge_markers)

    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (centr_lane + 45, y + lane_marker_move_y, marker_width, marker_height))

    player_group.draw(screen)

    if len(vehicle_group) < 2:
        lane = random.choice(lanes)
        image = random.choice(Vehicle_images)
        Vehicle = vehicle(image, lane, height / -2)
        vehicle_group.add(Vehicle)
    spawn_coins()

    for Vehicle in vehicle_group:
        Vehicle.rect.y += speed

        if Vehicle.rect.top >= height:
            Vehicle.kill()
            score += 1
            if score > 0 and score % 5 == 0:
                speed += 1
    # display the score
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (50, 450)
    screen.blit(text, text_rect)

    coin_text = font.render('Coins: ' + str(coin_collected), True, white)  # Use the correct variable name
    coins_text_rect = coin_text.get_rect()
    coins_text_rect.topright = (width - 10, 10)
    screen.blit(coin_text, coins_text_rect)
    coin_group.update()
    coin_group.draw(screen)

    collected_coins = pygame.sprite.spritecollide(player, coin_group, True)
    coin_collected += len(collected_coins)
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]
    if gameover:
        screen.blit(crash, crash_rect)
        pygame.draw.rect(screen, red, (0, 50, width, 100))
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Game over. Play again? (Enter Y or N)', True, white)
        text_rect.center = (width / 4, 100)
        screen.blit(text, text_rect)

    vehicle_group.draw(screen)
    coin_group.draw(screen)
    pygame.display.update()

    while gameover:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                gameover = False
                running = False
            # get the player's input (y or n)
            if event.type == KEYDOWN:
                if event.key == K_y:
                    # reset the game
                    gameover = False
                    speed = 2
                    score = 0
                    coin_collected = 0  # Reset coins collected
                    vehicle_group.empty()
                    player.rect.center = [player_x, player_y]
                elif event.key == K_n:
                    # exit the game
                    gameover = False
                    running = False

pygame.quit()
