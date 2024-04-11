import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
window_width = 800
window_height = 600

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Размер блока змеи и скорость
block_size = 20
snake_speed = 15

# Создание окна
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Змейка")

# Функция отображения счета
def show_score(score):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Счет: " + str(score), True, black)
    window.blit(text, (10, 10))

# Функция отображения уровня
def show_level(level):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Уровень: " + str(level), True, black)
    window.blit(text, (window_width - 150, 10))

# Функция отображения змеи
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(window, black, [block[0], block[1], block_size, block_size])

# Функция генерации случайной позиции для еды
def generate_food():
    food_x = random.randint(0, window_width - block_size)
    food_y = random.randint(0, window_height - block_size)
    return food_x // block_size * block_size, food_y // block_size * block_size

# Функция для создания нового блока змеи
def grow_snake(snake_list, direction):
    head = list(snake_list[-1])
    if direction == "left":
        head[0] += block_size
    elif direction == "right":
        head[0] += block_size
    elif direction == "up":
        head[1] += block_size
    elif direction == "down":
        head[1] += block_size
    snake_list.append(head)

# Основная функция игры
def game_loop():
    global snake_speed
    game_over = False
    game_quit = False

    snake_list = [[window_width / 2, window_height / 2]]
    snake_length = 1
    food_x, food_y = generate_food()

    # Начальное направление змеи
    direction = "right"
    change_to = direction

    score = 0
    level = 1

    clock = pygame.time.Clock()

    while not game_over:
        while game_quit:
            window.fill(black)
            show_score(score)
            show_level(level)
            message_font = pygame.font.SysFont(None, 50)
            game_over_message = message_font.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            window.blit(game_over_message, (window_width / 6, window_height / 3))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_quit = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_quit = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "right":
                    change_to = "left"
                elif event.key == pygame.K_RIGHT and direction != "left":
                    change_to = "right"
                elif event.key == pygame.K_UP and direction != "down":
                    change_to = "up"
                elif event.key == pygame.K_DOWN and direction != "up":
                    change_to = "down"

        # Проверка на столкновение с границей
        if snake_list[-1][0] >= window_width or snake_list[-1][0] < 0 or snake_list[-1][1] >= window_height or snake_list[-1][1] < 0:
            game_quit = True

        # Перемещение змеи
        if change_to == "left":
            direction = "left"
        elif change_to == "right":
            direction = "right"
        elif change_to == "up":
            direction = "up"
        elif change_to == "down":
            direction = "down"

        if direction == "left":
            snake_list[-1][0] -= block_size
        elif direction == "right":
            snake_list[-1][0] += block_size
        elif direction == "up":
            snake_list[-1][1] -= block_size
        elif direction == "down":
            snake_list[-1][1] += block_size

        # Проверка на столкновение с едой
        if snake_list[-1][0] == food_x and snake_list[-1][1] == food_y:
            food_x, food_y = generate_food()
            score += 1
            snake_length += 1
            if score % 3 == 0:
                level += 1
                snake_speed += 5

        # Удаление первого блока змеи, если ее длина увеличилась
        #if len(snake_list) > snake_length:
            #del snake_list[0]

        window.fill(white)
        pygame.draw.rect(window, red, [food_x, food_y, block_size, block_size])
        draw_snake(snake_list)
        show_score(score)
        show_level(level)

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
