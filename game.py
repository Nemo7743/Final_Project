# game.py
import pygame
import random
from settings import * # 匯入常數
from snake import Snake # 匯入蛇的類別

class Game:
    def __init__(self):
        # 這裡其實可以直接讀取 settings 的 WIDTH/HEIGHT，不需要透過參數傳入
        self.snake = Snake()
        self.score = 0
        self.food = None
        self._place_food()
        
        if not pygame.font.get_init():
            pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 20)

    def _place_food(self):
        while True:
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)
            if (x, y) not in self.snake.body:
                self.food = (x, y)
                break

    def update(self):
        self.snake.move()
        head = self.snake.get_head_position()
        
        # 檢查撞牆
        if (head[0] < 0 or head[0] >= WIDTH or 
            head[1] < 0 or head[1] >= HEIGHT):
            return True # Game Over

        # 檢查撞到自己
        if head in self.snake.body[1:]:
            return True # Game Over

        # 檢查是否吃到食物
        if head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.shrink()
            
        return False

    def draw(self, screen):
        # 繪製食物
        fx, fy = self.food
        food_rect = pygame.Rect(fx * BLOCK_SIZE, fy * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, RED, food_rect)
        
        # 繪製蛇
        self.snake.draw(screen)
        
        # 繪製分數
        text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(text, (5, 5))
