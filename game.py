import pygame
import random
from settings import *
from snake import Snake 

class Game:
    def __init__(self, game_mode):
        self.game_mode = game_mode
        self.snakes = []
        self.scores = []
        self.food = None
        
        # 根據傳入的 game_mode 初始化蛇
        if self.game_mode == 'DUAL':
            # Player 1 (Green) - Spawns on left side
            p1 = Snake(color=GREEN, start_pos=(WIDTH // 3, HEIGHT // 2))
            self.snakes.append(p1)
            self.scores.append(0)
            
            # Player 2 (Yellow) - Spawns on right side
            p2 = Snake(color=YELLOW, start_pos=(2 * WIDTH // 3, HEIGHT // 2))
            self.snakes.append(p2)
            self.scores.append(0)
        else:
            # Classic Mode
            self.snakes.append(Snake(color=GREEN))
            self.scores.append(0)

        self._place_food()
        
        if not pygame.font.get_init():
            pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 20)

    def _place_food(self):
        while True:
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)
            
            # 檢查食物是否生成在"任何"一條蛇的身體上
            collision = False
            for snake in self.snakes:
                if (x, y) in snake.body:
                    collision = True
                    break
            
            if not collision:
                self.food = (x, y)
                break

    def update(self):
        """
        更新所有蛇的狀態。
        return: None (Continue), or Dict (Game Over Result)
        """
        for index, snake in enumerate(self.snakes):
            snake.move()
            head = snake.get_head_position()
            
            game_over = False
            
            # 1. 檢查撞牆
            if (head[0] < 0 or head[0] >= WIDTH or 
                head[1] < 0 or head[1] >= HEIGHT):
                game_over = True

            # 2. 檢查撞到自己 (Self Collision Only)
            if head in snake.body[1:]:
                game_over = True
            
            # Determine Winner and Return Result if Game Over
            if game_over:
                winner = None
                
                if self.game_mode == 'DUAL':
                    # If Player 0 crashes, Player 1 wins. 
                    # If Player 1 crashes, Player 0 wins.
                    winner = 1 if index == 0 else 0
                else:
                    # Classic mode has no winner, just game over
                    winner = None
                
                return {
                    'scores': self.scores,
                    'winner': winner
                }

            # 3. 檢查是否吃到食物
            if head == self.food:
                self.scores[index] += 1
                self._place_food()
            else:
                snake.shrink()
                
        return None # Game continues

    def draw(self, screen):
        # 繪製食物
        fx, fy = self.food
        food_rect = pygame.Rect(fx * BLOCK_SIZE, fy * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, RED, food_rect)
        
        # 繪製所有蛇
        for snake in self.snakes:
            snake.draw(screen)
        
        # 繪製分數 UI
        if self.game_mode == 'DUAL':
            score_text = f"P1 (Green): {self.scores[0]}   P2 (Yellow): {self.scores[1]}"
        else:
            score_text = f"Score: {self.scores[0]}"
            
        text = self.font.render(score_text, True, WHITE)
        screen.blit(text, (5, 5))