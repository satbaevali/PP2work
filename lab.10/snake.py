# Imports
import pygame
import time
import random
import sys
import psycopg2

# Initializg
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 500))

# Setting FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Program global vars
GREEN = (100, 200, 100)
BLACK = (0, 0, 0)
SCORE = 0
SCOREAPPLECHECK = 0
APPLECOLLECTED = 0
NEWAPPLE = 1
SCOREFRUITS = 0
SCOREPEARCHECK = 0
PEARCOLLECTED = 0
NEWPEAR = 1
SCOREBANANACHECK = 0
BANANACOLLECTED = 0
NEWBANANA = 1
NOBANANATIME = 0
SCORE4 = 4
SCOREUNDER4 = 8
LEVEL = 1
LENGTH = 1
ALLSNAKE = []
DIR = 0
KEYBEFORE = 0
MUSICPLAYG = 0
SPEED = 3
check = 1
walls_num = 0
NEWSTAGE = 1
STAGE = 1
NEWSTAGETIME = 0
coords = []
PAUSE = 0
x = 100
y = 80


cur = None
conn = None
print("Enter your user name: ")
name = input()

# Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("GAME OVER", True, BLACK)

try:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Alisatbai99")
    cur = conn.cursor()

    create_script = ''' CREATE TABLE IF NOT EXISTS snakeusers (
                            name varchar,
                            stage varchar) '''
    cur.execute(create_script)

    try:
        search_script = ''' SELECT stage FROM snakeusers
                            WHERE name = %s '''
        search_cond = (name,)
        cur.execute(search_script, search_cond)
        STAGE = int(cur.fetchone()[0])
        if STAGE > 1:
            walls_num = (STAGE - 1) * 2
    except:
        STAGE = 1
        insert_script = ''' INSERT INTO snakeusers (name, stage) VALUES (%s, %s) '''
        insert_value = (name, STAGE)
        cur.execute(insert_script, insert_value)
        print(STAGE)       

    conn.commit()

except:
    print("Error")

finally:
    if conn is not None:
        cur.close()
    if cur is not None:
        conn.close()

# Class for apples
class apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"lab8.1\apple.png") #loading apple image
        self.image = pygame.transform.scale(self.image, (20, 20)) 
        self.rect = self.image.get_rect() #creating a reactangle around apple
        self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25)) #random spawn

    def move(self):
        global NEWAPPLE
        global APPLECOLLECTED
        if not NEWAPPLE: #when there is no apple on the screen, then it means we've collected it
            APPLECOLLECTED = 0
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25)) #random spawn
            NEWAPPLE = 1 #this value has to 1 since there is already one apple on the screen


class pear(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"lab9\pear.png") #loading pear image
        self.image = pygame.transform.scale(self.image, (30, 20))
        self.rect = self.image.get_rect() #creating a rectangle around pear image
        self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25)) #random spawn

    def move(self):
        global NEWPEAR
        global PEARCOLLECTED
        if not NEWPEAR: #when there is no pear on the screen, then it means we've collected it
            PEARCOLLECTED = 0
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25)) #random spawn
            NEWPEAR = 1 #this value has to 1 since there is already one apple on the screen


class banana(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"lab9\Banana.png") #loading banana image
        self.image = pygame.transform.scale(self.image, (20, 25))
        self.rect = self.image.get_rect() #creating rectangle around banana image
        self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25)) #random spawn

    def move(self):
        global NEWBANANA
        global BANANACOLLECTED
        if not NEWBANANA:
            BANANACOLLECTED = 0
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25))
            NEWBANANA = 1


# Class for snake parts
class snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.draw.rect(screen, GREEN, [x, y, 20, 20]) #creating a rectangle - part of snake
        self.rect = pygame.Rect(x, y, 20, 20) #rectangle around a snake

    def move(self, all_snake):
        for i in all_snake:
            pygame.draw.rect(screen, GREEN, [i[0], i[1], 20, 20]) #all_snake is list which contains all of the rectangles of snake, so this loop will display these rectangles
        self.rect = pygame.Rect(x, y, 20, 20)

class wall(pygame.sprite.Sprite):
    def __init__(self):
        global coords
        super().__init__()
        coords = [random.randint(25, 800-25), random.randint(25, 500-25), 20, random.randint(10, 30)]
        self.image = pygame.draw.rect(screen, BLACK, [coords[0], coords[1], coords[2], coords[3]])
        self.rect = pygame.Rect(coords[0], coords[1], coords[2], coords[3])

    def move(self, walls_num):
        global NEWSTAGE
        global coords
        if NEWSTAGE:
            coords = []
            for i in range(walls_num):
                coords.append([random.randint(25, 800-25), random.randint(25, 500-25), 20, random.randint(30, 100)])
            NEWSTAGE = 0
        for i in range(walls_num):
            pygame.draw.rect(screen, BLACK, [coords[i][0], coords[i][1], coords[i][2], coords[i][3]])

# Function for quitting after game over
def quit():
    global STAGE
    global name
    stop_music()
    time.sleep(1/3) #delay after snake hits wall or itself
    screen.fill((240, 80, 90))
    screen.blit(game_over, (235, 200)) #game over text
    pygame.display.update()
    time.sleep(3) #delay after game over text is shown on the screen
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="Alisatbai99")
        cur = conn.cursor()

        change_script2 = ''' UPDATE snakeusers 
                                    SET stage = %s 
                                    WHERE name = %s'''
        change_cond2 = (STAGE, name)
        cur.execute(change_script2, change_cond2)

        conn.commit()

    except:
        print("Error")

    finally:
        if conn is not None:
            cur.close()
        if cur is not None:
            conn.close()
    pygame.quit()
    sys.exit()
    
# Play music
def play_music():
    pygame.mixer.music.load("lab8.1\lab8_snake_resources_background.wav")
    pygame.mixer.music.play(-1)


# Stop music
def stop_music():
    pygame.mixer.music.stop()


# Objects from our classes
A1 = apple()
apples = pygame.sprite.Group()
apples.add(A1)
P1 = pear()
pears = pygame.sprite.Group()
pears.add(P1)
B1 = banana()
bananas = pygame.sprite.Group()
bananas.add(B1)
H1 = snake()
heads = pygame.sprite.Group()
heads.add(H1)
W1 = wall()
walls = pygame.sprite.Group()
walls.add(W1)

while check:
    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = 0

        # Choosing direction
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            if KEYBEFORE != pygame.K_w and KEYBEFORE != pygame.K_s: #if we didn't click w or s before, we will be allowed to move in the up direction
                y -= 20
                KEYBEFORE = pygame.K_w
                DIR = "up" #direction's value
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a: 
            if KEYBEFORE != pygame.K_a and KEYBEFORE != pygame.K_d: #if we didn't click a or d before, we will be allowed to move in the left direction
                x -= 20
                KEYBEFORE = pygame.K_a
                DIR = "left" #direction's value
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            if KEYBEFORE != pygame.K_s and KEYBEFORE != pygame.K_w: #if we didn't click w or s before, we will be allowed to move in the down direction
                y += 20
                KEYBEFORE = pygame.K_s
                DIR = "down" #direction's value
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            if KEYBEFORE != pygame.K_d and KEYBEFORE != pygame.K_a: #if we didn't click a or d before, we will be allowed to move in the right direction
                x += 20
                KEYBEFORE = pygame.K_d
                DIR = "right" #direction's value
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            PAUSE = not PAUSE
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            if PAUSE:
                conn = None
                cur = None
                try:
                    conn = psycopg2.connect(
                        host="localhost",
                        database="postgres",
                        user="postgres",
                        password="Alisatbai99")
                    cur = conn.cursor()

                    change_script2 = ''' UPDATE snakeusers 
                                                    SET stage = %s 
                                                    WHERE name = %s'''
                    change_cond2 = (STAGE, name)
                    cur.execute(change_script2, change_cond2)

                    conn.commit()

                except:
                    print("Error")

                finally:
                    if conn is not None:
                        cur.close()
                    if cur is not None:
                        conn.close()

    # Play music at the beginning
    if not MUSICPLAYG:
        play_music()
        MUSICPLAYG = 1

    # Yellow background
    screen.fill((255, 255, 100))

    # Showing score and level
    score = font_small.render("Score: " + str(SCOREFRUITS), True, BLACK)
    screen.blit(score, (800 - 110, 10))
    stage = font_small.render("Stage: " + str(STAGE), True, BLACK)
    screen.blit(stage, (10, 10))

    if not PAUSE:
        # Moving objects
        H1.move(ALLSNAKE)
        NEWSTAGETIME += 1
        A1.move()
        P1.move()
        B1.move()
        W1.move(walls_num)

        # Continue moving in chosen direction
        if DIR == "down":
            y += SPEED
        elif DIR == "up":
            y -= SPEED
        elif DIR == "left":
            x -= SPEED
        elif DIR == "right":
            x += SPEED

        # Append current coordinates of head to coordinates of all snake
        current_head = []
        current_head.append(x)
        current_head.append(y)
        ALLSNAKE.append(current_head)

        # Delete the end of a snake if length didn't grow
        if len(ALLSNAKE) > LENGTH:
            del ALLSNAKE[0]

        # Game over if hit wall or self
        if y >= 480 or y <= 0 or x >= 780 or x <= 0:
            quit()
        for i in ALLSNAKE[:-1]:
            if i == current_head:
                quit()

        for u in coords:
            if (current_head[0] >= u[0] and current_head[0] <= u[0] + u[2]) and (current_head[1] >= u[1] and current_head[1] <= u[1] + u[3]):
                if NEWSTAGETIME >= 3:
                    quit()

        # If collected apple: +length, +score
        if pygame.sprite.spritecollideany(H1, apples):
            APPLECOLLECTED = 1
            LENGTH += 1

        if pygame.sprite.spritecollideany(H1, pears):
            PEARCOLLECTED = 1
            LENGTH += 1

        if pygame.sprite.spritecollideany(H1, bananas):
            if NOBANANATIME < 240: #if 
                BANANACOLLECTED = 1
                LENGTH += 1

        # Level up if score += 4. Speed up
        if SCOREFRUITS >= SCORE4 and SCOREFRUITS < SCOREUNDER4: #borders of values when we move to the next level
            FPS += 10
            LEVEL += 1
            SCORE4 += 4
            SCOREUNDER4 += 4
        if SCOREFRUITS >= 20:
            SCOREFRUITS = 0
            LEVEL = 1
            SCORE4 = 4
            SCOREUNDER4 = 8
            FPS = 60
            NEWSTAGE = 1
            STAGE += 1
            NEWSTAGETIME = 0
            walls_num += 2

        # Continue displaying apple if not collected
        if not APPLECOLLECTED:
            for entity in apples:
                screen.blit(entity.image, entity.rect)
        
        else:
            if NEWAPPLE == 1:
                SCOREFRUITS += 1
                NEWAPPLE = 0

        if not PEARCOLLECTED:
            for entity in pears:
                screen.blit(entity.image, entity.rect)

        else:
            if NEWPEAR == 1:
                SCOREFRUITS += 4
                NEWPEAR = 0

        if not BANANACOLLECTED:
            if NOBANANATIME < 240: #if value is lower than 240 then image of banana will be displayed
                for entity in bananas:
                    screen.blit(entity.image, entity.rect)
                    NOBANANATIME += 1 #it has to increase in value since, if we didn't collected banana then it has to disappear after some time
            else:
                if NOBANANATIME < 600: #in the range from 240 until 600 there will be no banana on the screen
                    NOBANANATIME += 1
                else:
                    NOBANANATIME = 0 #if value is equal or bigger than 600, then we need to display banana again

        
        else:
            NOBANANATIME = 240 #if banana is collected then we need to wait until 600, so it will appear again on the screen
            if NEWBANANA == 1: #if we got one banana then score will increase for 2
                SCOREFRUITS += 2
                NEWBANANA = 0
    else:
        screen.fill((255, 255, 100))
        pause = font.render("PAUSE", True, BLACK)
        screen.blit(pause, (280, 200))
        save = font_small.render("Press R to save your progress", True, BLACK)
        screen.blit(save, (280, 270))

    pygame.display.update()
    FramePerSec.tick(FPS)