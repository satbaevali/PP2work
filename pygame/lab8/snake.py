import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])  # Tuple for direction
        self.color = GREEN
        self.score = 0
        self.level = 1
        self.speed = 10
        self.apple_counter = 0  # Counter for apples eaten

    def head_position(self):
        return self.positions[0]

    def move(self):
        current = self.head_position()
        x, y = self.direction
        new = (((current[0] + (x * CELL_SIZE)) % WIDTH), (current[1] + (y * CELL_SIZE)) % HEIGHT)

        # Check for collision with itself
        if new in self.positions[1:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
        if new[0] < 0 or new[0] >= WIDTH or new[1] < 0 or new[1] >= HEIGHT:
            self.reset()

    def reset(self):
        self.length = 1
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        self.score = 0
        self.level = 1
        self.speed = 10
        self.apple_counter = 0  # Reset apple counter

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_UP:
                    self.direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    self.direction = (0, 1)
                elif event.key == pygame.K_RIGHT:
                    self.direction = (1, 0)
                elif event.key == pygame.K_LEFT:
                    self.direction = (-1, 0)

    def draw_level(self, surface):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Level: {self.level}", True, BLACK)
        surface.blit(text, (10, 10))

    def draw_apple_counter(self, surface):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Apples: {self.apple_counter}", True, BLACK)
        surface.blit(text, (10, 50))

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * CELL_SIZE, random.randint(0, GRID_HEIGHT-1) * CELL_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)

# Main function
def main():
    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()
    running = True

    while running:
        # Event handling
        snake.handle_keys()

        # Logic
        snake.move()

        # Check if snake goes out of bounds
        if snake.head_position()[0] < 0 or snake.head_position()[0] >= WIDTH \
                or snake.head_position()[1] < 0 or snake.head_position()[1] >= HEIGHT:
            snake.reset()  # Reset game if snake goes out of bounds

        if snake.head_position() == food.position:
            snake.length += 1
            snake.score += 1
            snake.apple_counter += 1 
            if snake.score % 6 == 0:  
                snake.level += 1
                snake.speed += 1  
            food.randomize_position()

        # Draw
        SCREEN.fill(WHITE)
        snake.draw(SCREEN)
        food.draw(SCREEN)
        snake.draw_level(SCREEN)
        snake.draw_apple_counter(SCREEN)
        pygame.display.flip()

        # Level up condition
        if snake.score >= 100:
            snake.level_up()

        # Clock tick
        clock.tick(snake.speed)

# Start the game
if __name__ == "__main__":
    main()
