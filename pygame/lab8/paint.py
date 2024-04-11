import pygame
import random
import math

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class ShapeDrawer:
    def __init__(self):
        self.color = BLACK
        self.shape = None

    def set_color(self, color):
        self.color = color

    def draw_shape(self, shape, x, y, size):
        if shape == "square":
            pygame.draw.rect(SCREEN, self.color, (x, y, size, size))
        elif shape == "right_triangle":
            points = [(x, y), (x + size, y), (x, y + size)]
            pygame.draw.polygon(SCREEN, self.color, points)
        elif shape == "equilateral_triangle":
            height = size * math.sqrt(3) / 2
            points = [(x, y + height), (x + size, y + height), (x + size / 2, y)]
            pygame.draw.polygon(SCREEN, self.color, points)
        elif shape == "rhombus":
            points = [(x + size / 2, y), (x + size, y + size / 2),
                      (x + size / 2, y + size), (x, y + size / 2)]
            pygame.draw.polygon(SCREEN, self.color, points)

def draw_menu(drawer, font):
    menu_text = font.render("1 - Квадрат, 2 - Прямоугольный треугольник, 3 - Равносторонний треугольник, 4 - Ромб", True, BLACK)
    color_text = font.render("Выбранный цвет:", True, BLACK)
    color_display = pygame.Surface((50, 50))
    color_display.fill(drawer.color)

    SCREEN.blit(menu_text, (10, 10))
    SCREEN.blit(color_text, (10, 70))
    SCREEN.blit(color_display, (160, 70))

def main():
    drawer = ShapeDrawer()
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 24)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_1:
                    drawer.shape = "square"
                elif event.key == pygame.K_2:
                    drawer.shape = "right_triangle"
                elif event.key == pygame.K_3:
                    drawer.shape = "equilateral_triangle"
                elif event.key == pygame.K_4:
                    drawer.shape = "rhombus"
                elif event.key == pygame.K_r:
                    drawer.set_color(RED)
                elif event.key == pygame.K_g:
                    drawer.set_color(GREEN)
                elif event.key == pygame.K_b:
                    drawer.set_color(BLUE)

        SCREEN.fill(WHITE)

        # Отрисовка меню
        draw_menu(drawer, font)

        # Рисование фигуры
        if drawer.shape:
            drawer.draw_shape(drawer.shape, 200, 150, 200)

        pygame.display.flip()
        clock.tick(30)

# Запуск программы
if __name__ == "__main__":
    main()
