# snake.py
import pygame
from settings import * # 匯入剛剛定義的所有常數

class Snake:
    def __init__(self):
        # 初始化蛇的位置：從畫面中間開始
        start_x = WIDTH // 2
        start_y = HEIGHT // 2
        self.body = [(start_x, start_y), (start_x, start_y + 1)] 
        self.direction = UP # 初始往上走

    def change_direction(self, new_direction):
        # 處理方向輸入，避免反轉
        if new_direction == LEFT and self.direction != RIGHT:
            self.direction = new_direction
        elif new_direction == RIGHT and self.direction != LEFT:
            self.direction = new_direction
        elif new_direction == UP and self.direction != DOWN:
            self.direction = new_direction
        elif new_direction == DOWN and self.direction != UP:
            self.direction = new_direction

    def get_head_position(self):
        return self.body[0]

    def move(self):
        cur_x, cur_y = self.get_head_position()
        
        if self.direction == UP:
            cur_y -= 1
        elif self.direction == DOWN:
            cur_y += 1
        elif self.direction == LEFT:
            cur_x -= 1
        elif self.direction == RIGHT:
            cur_x += 1
            
        new_head = (cur_x, cur_y)
        self.body.insert(0, new_head)
    
    def shrink(self):
        self.body.pop()
    
    def draw(self, surface):
        for x, y in self.body:
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(surface, GREEN, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)
