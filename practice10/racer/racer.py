from random import choice, randint, random

import pygame


WIDTH, HEIGHT = 480, 700
ROAD = pygame.Rect(80, 0, 320, HEIGHT)
LANES = [120, 200, 280, 360]


class RacerApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Practice 10 Racer")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 24)
        self.reset()

    def reset(self):
        self.player = pygame.Rect(LANES[1] - 18, HEIGHT - 80, 36, 56)
        self.enemy = pygame.Rect(choice(LANES) - 18, -70, 36, 56)
        self.coins = []
        self.coins_collected = 0
        self.speed = 5
        self.spawn_timer = 0
        self.game_over = False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN and self.game_over and event.key == pygame.K_SPACE:
                    self.reset()

            if not self.game_over:
                self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.x -= 6
        if keys[pygame.K_RIGHT]:
            self.player.x += 6
        self.player.clamp_ip(ROAD)

        self.enemy.y += self.speed
        if self.enemy.top > HEIGHT:
            self.enemy.centerx = choice(LANES)
            self.enemy.y = -70

        # Practice 10: coins randomly appear on the road.
        self.spawn_timer += 1
        if self.spawn_timer > 45:
            self.spawn_timer = 0
            if random() < 0.7:
                self.coins.append(pygame.Rect(choice(LANES) - 10, -20, 20, 20))

        for coin in self.coins[:]:
            coin.y += self.speed
            if coin.top > HEIGHT:
                self.coins.remove(coin)
            elif self.player.colliderect(coin):
                self.coins.remove(coin)
                self.coins_collected += 1

        if self.player.colliderect(self.enemy):
            self.game_over = True

    def draw(self):
        self.screen.fill((70, 150, 90))
        pygame.draw.rect(self.screen, (55, 58, 64), ROAD)
        for x in LANES:
            pygame.draw.line(self.screen, (230, 230, 230), (x + 40, 0), (x + 40, HEIGHT), 2)
        pygame.draw.rect(self.screen, (40, 120, 220), self.player)
        pygame.draw.rect(self.screen, (190, 60, 70), self.enemy)
        for coin in self.coins:
            pygame.draw.ellipse(self.screen, (235, 190, 55), coin)

        # Practice 10: show collected coins in the top-right corner.
        text = self.font.render(f"Coins: {self.coins_collected}", True, (255, 255, 255))
        self.screen.blit(text, text.get_rect(topright=(WIDTH - 12, 12)))
        if self.game_over:
            label = self.font.render("Game over. Press Space", True, (255, 255, 255))
            self.screen.blit(label, label.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
