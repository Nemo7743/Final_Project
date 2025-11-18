!pip install pygame
import pygame
import random
import sys
import os
import numpy as np
from IPython.display import Image, display, clear_output
import pygame
import random
import os
import numpy as np
from IPython.display import Image, display, clear_output

pygame.init()

BLOCK_SIZE = 20
WIDTH = 20
HEIGHT = 15
SCREEN_WIDTH = (WIDTH + 2) * BLOCK_SIZE
SCREEN_HEIGHT = (HEIGHT + 2) * BLOCK_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

STOP, LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3, 4

class SnakeGameEnv:
    def __init__(self):
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.SysFont(None, 35)
        self.reset()

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.direction = STOP
        self.score = 0
        self.tail = []
        self.n_tail = 0
        self.game_over = False
        self.place_coin()
        return self.get_state()

    def place_coin(self):
        while True:
            self.coin_x = random.randint(1, WIDTH - 2)
            self.coin_y = random.randint(1, HEIGHT - 2)
            if (self.coin_x, self.coin_y) not in self.tail and (self.coin_x != self.x or self.coin_y != self.y):
                break

    def get_state(self):
        # 你可以根據這裡設計自己的狀態表示方式
        return (self.x, self.y, self.coin_x, self.coin_y)

    def step(self, action):
        if self.game_over:
            return self.get_state(), 0, True

        # 不能反向
        if action == LEFT and self.direction != RIGHT:
            self.direction = LEFT
        elif action == RIGHT and self.direction != LEFT:
            self.direction = RIGHT
        elif action == UP and self.direction != DOWN:
            self.direction = UP
        elif action == DOWN and self.direction != UP:
            self.direction = DOWN

        # 更新尾巴
        if self.n_tail > 0:
            self.tail.insert(0, (self.x, self.y))
            self.tail = self.tail[:self.n_tail]

        # 移動
        if self.direction == LEFT:
            self.x -= 1
        elif self.direction == RIGHT:
            self.x += 1
        elif self.direction == UP:
            self.y -= 1
        elif self.direction == DOWN:
            self.y += 1

        # 檢查撞牆
        if self.x < 0 or self.x >= WIDTH or self.y < 0 or self.y >= HEIGHT:
            self.game_over = True
            return self.get_state(), -100, True

        # 撞自己
        if (self.x, self.y) in self.tail:
            self.game_over = True
            return self.get_state(), -100, True

        # 吃到 coin
        reward = 0
        if self.x == self.coin_x and self.y == self.coin_y:
            self.score += 20
            self.n_tail += 1
            self.place_coin()
            reward = 20

        return self.get_state(), reward, self.game_over

    def render(self):
        self.surface.fill(BLACK)

        for i in range(WIDTH + 2):
            pygame.draw.rect(self.surface, WHITE, (i * BLOCK_SIZE, 0, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.surface, WHITE, (i * BLOCK_SIZE, (HEIGHT + 1) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        for i in range(HEIGHT + 2):
            pygame.draw.rect(self.surface, WHITE, (0, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.surface, WHITE, ((WIDTH + 1) * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        pygame.draw.rect(self.surface, GREEN, ((self.x + 1) * BLOCK_SIZE, (self.y + 1) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        for tx, ty in self.tail:
            pygame.draw.rect(self.surface, GREEN, ((tx + 1) * BLOCK_SIZE, (ty + 1) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        pygame.draw.rect(self.surface, YELLOW, ((self.coin_x + 1) * BLOCK_SIZE, (self.coin_y + 1) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        pygame.image.save(self.surface, "frame.png")
        clear_output(wait=True)
        display(Image("frame.png"))