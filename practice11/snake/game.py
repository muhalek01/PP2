from random import choice, randint

import pygame


WIDTH, HEIGHT = 600, 640
TOP = 40
CELL = 20
GRID_W = WIDTH // CELL
GRID_H = (HEIGHT - TOP) // CELL
FOOD_LIFETIME_MS = 5000


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Practice 11 Snake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 24)
        self.reset()

    def reset(self):
        self.snake = [(8, 8), (7, 8), (6, 8)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.score = 0
        self.level = 1
        self.food_eaten = 0
        self.game_over = False
        self.spawn_food()

    def spawn_food(self):
        """Practice 11: food has a random weight and disappears by timer."""
        while True:
            self.food = (randint(0, GRID_W - 1), randint(0, GRID_H - 1))
            if self.food not in self.snake:
                break
        self.food_weight = choice([1, 2, 3])
        self.food_until = pygame.time.get_ticks() + FOOD_LIFETIME_MS

    def current_fps(self):
        return 7 + self.level

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                self.handle_event(event)

            if not self.game_over:
                self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.current_fps())

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and self.game_over and event.key == pygame.K_SPACE:
            self.reset()
        if event.type != pygame.KEYDOWN:
            return
        keys = {
            pygame.K_UP: (0, -1),
            pygame.K_DOWN: (0, 1),
            pygame.K_LEFT: (-1, 0),
            pygame.K_RIGHT: (1, 0),
        }
        if event.key in keys:
            new_direction = keys[event.key]
            if (new_direction[0] + self.direction[0], new_direction[1] + self.direction[1]) != (0, 0):
                self.next_direction = new_direction

    def update(self):
        if pygame.time.get_ticks() > self.food_until:
            self.spawn_food()

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        x, y = new_head
        if x < 0 or x >= GRID_W or y < 0 or y >= GRID_H or new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 10 * self.food_weight
            self.food_eaten += 1
            if self.food_eaten % 4 == 0:
                self.level += 1
            # Weight also controls growth: heavier food leaves more body cells.
            for _ in range(self.food_weight - 1):
                self.snake.append(self.snake[-1])
            self.spawn_food()
        else:
            self.snake.pop()

    def draw(self):
        self.screen.fill((238, 241, 244))
        pygame.draw.rect(self.screen, (25, 35, 40), (0, 0, WIDTH, TOP))
        hud = self.font.render(f"Score: {self.score}   Level: {self.level}   Food x{self.food_weight}", True, (255, 255, 255))
        self.screen.blit(hud, (12, 8))

        food_color = {1: (230, 80, 70), 2: (230, 170, 55), 3: (90, 160, 230)}[self.food_weight]
        pygame.draw.rect(self.screen, food_color, self.cell_rect(self.food))
        for index, cell in enumerate(self.snake):
            color = (40, 140, 90) if index == 0 else (70, 175, 110)
            pygame.draw.rect(self.screen, color, self.cell_rect(cell))

        if self.game_over:
            label = self.font.render("Game over. Press Space", True, (25, 35, 40))
            self.screen.blit(label, label.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    def cell_rect(self, cell):
        return pygame.Rect(cell[0] * CELL, TOP + cell[1] * CELL, CELL - 1, CELL - 1)
