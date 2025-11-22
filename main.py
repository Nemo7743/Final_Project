# main.py
import pygame
import sys
from settings import * # 匯入設定
from game import Game  # 匯入遊戲邏輯

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("經典貪食蛇")
    
    clock = pygame.time.Clock()
    game = Game() # 不需要傳參數了，因為 Game 內部直接讀取 settings
    
    running = True 
    
    while running:
        # --- 事件處理 ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # 這裡需要用到 settings 裡面的方向常數
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    game.snake.change_direction(RIGHT)
                elif event.key == pygame.K_UP:
                    game.snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    game.snake.change_direction(DOWN)
        
        # --- 邏輯更新 ---
        game_over = game.update() 
        
        if game_over:
            print(f"Final Score: {game.score}")
            pygame.time.delay(2000)
            running = False 

        # --- 畫面繪製 ---
        screen.fill(BLACK)
        game.draw(screen)
        pygame.display.update()
        
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
