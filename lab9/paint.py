import pygame
from sys import exit
import math
import random

pygame.init()

#standard values
width = 800
height = 600
active_color = 'white' #initial value of color
radius = 1
draw_on = False #checker for drawing or not
start_pos = (0, 0)


screen = pygame.display.set_mode((width, height))
screen.fill('white')
pygame.display.set_caption("Paint")
work_surf = pygame.Surface((width, height)) #surface that contains all of the figures

points = list() #list for coordinates

#images
eraser = pygame.image.load(r'C:\Users\akim0\Desktop\pygame\lab8.1\eraser.png')
eraser = pygame.transform.rotozoom(eraser, 0, 0.3)
eraser_rect = eraser.get_rect(center = (35, 40))

pencil = pygame.image.load(r'C:\Users\akim0\Desktop\pygame\lab8.1\pencil.png')
pencil = pygame.transform.rotozoom(pencil, 0, 0.05)
pencil_rect = pencil.get_rect(center = (215, 35))

circle = pygame.image.load(r'C:\Users\akim0\Desktop\pygame\lab8.1\circle.png').convert_alpha()
circle = pygame.transform.rotozoom(circle, 0, 0.05)
circle_rect = circle.get_rect(center = (95, 35))

rectangle = pygame.image.load(r'C:\Users\akim0\Desktop\pygame\lab8.1\rectangle.png').convert_alpha()
rectangle = pygame.transform.rotozoom(rectangle, 0, 0.09)
rectangle_rect = rectangle.get_rect(center = (155, 37))

square = pygame.image.load(r'C:\Users\akim0\Desktop\pygame\lab9\square.png').convert_alpha()
square = pygame.transform.rotozoom(square, 0, 0.1)
square_rect = square.get_rect(center = (275, 37))

r_tr = pygame.image.load(r'C:\Users\akim0\Desktop\pygame\lab9\r_tr.png').convert_alpha()
r_tr = pygame.transform.rotozoom(r_tr, 0, 0.09)
r_tr_rect = r_tr.get_rect(center = (335, 37))

eq_tr = pygame.image.load(r'C:\Users\akim0\Desktop\pygame\lab9\eq_tr.png').convert_alpha()
eq_tr = pygame.transform.rotozoom(eq_tr, 0, 0.04)
eq_tr_rect = eq_tr.get_rect(center = (395, 37))

rhomb = pygame.image.load(r'C:\Users\akim0\Desktop\pygame\lab9\rhomb.png').convert_alpha()
rhomb = pygame.transform.rotozoom(rhomb, 0, 0.09)
rhomb_rect = rhomb.get_rect(center = (455, 37))


active_tool = 1 #tool's value which will be used for checking further

def draw_menu(): #function for displaying menu
    pygame.draw.rect(screen, 'gray', [0, 0, width, 70 ])
    
    #creating "buttons" for icons of tools
    eraser_but = pygame.draw.rect(screen, '#E9DCDE', [10, 10, 50, 50])
    circle_but = pygame.draw.rect(screen, '#E9DCDE', [70, 10, 50, 50])
    rectangle_but = pygame.draw.rect(screen, '#E9DCDE', [130, 10, 50, 50])
    pencil_but = pygame.draw.rect(screen, '#E9DCDE', [190, 10, 50, 50])
    square_but = pygame.draw.rect(screen, '#E9DCDE', [250, 10, 50, 50])
    r_tr_but = pygame.draw.rect(screen, '#E9DCDE', [310, 10, 50, 50])
    eq_tr_but = pygame.draw.rect(screen, '#E9DCDE', [370, 10, 50, 50])
    rhomb_but = pygame.draw.rect(screen, '#E9DCDE', [430, 10, 50, 50])
    screen.blit(eraser, eraser_rect)
    screen.blit(circle, circle_rect)
    screen.blit(rectangle, rectangle_rect)
    screen.blit(pencil, pencil_rect)
    screen.blit(square, square_rect)
    screen.blit(r_tr, r_tr_rect)
    screen.blit(eq_tr, eq_tr_rect)
    screen.blit(rhomb, rhomb_rect)
    

    #colors
    blue = pygame.draw.rect(screen, (0, 0, 255), [width - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [width - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [width - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [width - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [width - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [width - 85, 35, 25, 25])
    white = pygame.draw.rect(screen, (0, 0, 0), [width - 110, 10, 25, 25])
    black = pygame.draw.rect(screen, (255, 255, 255), [width - 110, 35, 25, 25])

    color_rect = [blue, red, green, yellow, teal, purple, white, black] #list of names of colors
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)] #list of actual colors

    return color_rect, rgb_list #sending lists

def Rect_pos(x1, y1, x2, y2): 
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2)) #formula for coordinates of rectangle

def Square_pos(x1, y1, x2, y2): 
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(x1 - x2)) #formula for coordinates of square

def Equilateral_Triangle_pos(x1, y1, x2, y2): 
        points.append((x1, y1)) #formula for coordinates of eq_triangle
        points.append((x2, y2))
        points.append((x2+x2-x1, y1)) 
        return points

def Right_Triangle_pos(x1, y1, x2, y2): # 
        points.append((x1, y1)) #formula for coordinates of right_triangle, y1 are equal since for right_triangle one side has to be located on one y coordinate with one point and on one x coordinate with other point
        points.append((x2, y2))
        points.append((x1, y2))
        return points

def Rhombus_pos(x1, y1, x2, y2): # 
        points.append((x1, y1)) #formula for coordinates of rhomb
        points.append((x2, y2))
        points.append((x2-x1+x2, y1))
        points.append((x2, y1+y1-y2))
        return points

while True:
    colors, rgbs = draw_menu() #getting values from function's list
    
    #events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(colors)): #creating a loop in order to get color
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i] #if user clicked to one of the colors, active_color got the value from rgbs list
            if eraser_rect.collidepoint(event.pos):
                active_tool = 0 #checking if user clicked to eraser instrument
            if pencil_rect.collidepoint(event.pos):
                active_tool = 1 #checking if user clicked to pencil instrument
            if rectangle_rect.collidepoint(event.pos):
                active_tool = 2 #checking if user clicked to rectangle instrument
            if circle_rect.collidepoint(event.pos):
                active_tool = 3 #checking if user clicked to circle instrument
            if square_rect.collidepoint(event.pos):
                active_tool = 4 #checking if user clicked to square instrument
            if r_tr_rect.collidepoint(event.pos):
                active_tool = 5 #checking if user clicked to r_triangle instrument
            if eq_tr_rect.collidepoint(event.pos):
                active_tool = 6 #checking if user clicked to eq_triangle instrument
            if rhomb_rect.collidepoint(event.pos):
                active_tool = 7 #checking if user clicked to rhomb instrument
            
            draw_on = True #when we hold mouse button draw_on is alwats True
            start_pos = event.pos #getting initial postion of mouse

        if event.type == pygame.MOUSEBUTTONUP:
            work_surf.blit(screen, (0, 0)) #when we fully pressed mouse button, work_surf will display on the screen 
            draw_on = False #it changes value to False, since we finished our drawings

        if event.type == pygame.MOUSEMOTION:
            if draw_on: #checking if we drawing or not
                if active_tool == 0: #if tool is eraser then we draw white circle with coordinates of mouse
                    pygame.draw.circle(screen, 'white', (event.pos[0], event.pos[1]), 6)
                if active_tool == 1: #if tool is pencil then we draw line with all of the parameters below
                    pygame.draw.line(screen, active_color, start_pos, event.pos, radius)
                    start_pos = event.pos
                if active_tool == 2: #if tool is rectangle then we send our start and final coordinates to the function, so we will get appropriate coordinates 
                    temp = Rect_pos(start_pos[0], start_pos[1], event.pos[0], event.pos[1])
                    screen.blit(work_surf, (0, 0))
                    pygame.draw.rect(screen, active_color, pygame.Rect(temp))
                if active_tool == 3: #if tool is circle then we draw a circle with center of start position and radius by special formula of distance between two points
                    screen.blit(work_surf, (0, 0))
                    pygame.draw.circle(screen, active_color, (start_pos[0], start_pos[1]), int(math.sqrt((event.pos[0]-start_pos[0])**2 + (event.pos[1]-start_pos[1])**2)))
                if active_tool == 4:
                    temp = Square_pos(start_pos[0], start_pos[1], event.pos[0], event.pos[1]) #sending coordinates to function
                    screen.blit(work_surf, (0, 0))
                    pygame.draw.rect(screen, active_color, pygame.Rect(temp))
                if active_tool == 5:
                    temp = Right_Triangle_pos(start_pos[0], start_pos[1], event.pos[0], event.pos[1]) #sending coordinates to function
                    screen.blit(work_surf, (0, 0))
                    pygame.draw.polygon(screen, active_color, temp)
                    points = [] #clearing points list
                if active_tool == 6:
                    temp = Equilateral_Triangle_pos(start_pos[0], start_pos[1], event.pos[0], event.pos[1]) #sending coordinates to function
                    screen.blit(work_surf, (0, 0))
                    pygame.draw.polygon(screen, active_color, temp)
                    points = [] #clearing points list
                if active_tool == 7:
                    temp = Rhombus_pos(start_pos[0], start_pos[1], event.pos[0], event.pos[1]) #sending coordinates to function
                    screen.blit(work_surf, (0, 0))
                    pygame.draw.polygon(screen, active_color, temp)
                    points = [] #clearing points list

        
    pygame.display.flip()