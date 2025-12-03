# main.py
import pygame
import sys
from settings import * 
from game import Game 

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(f"Python Snake - {GAME_MODE} Mode")
    
    clock = pygame.time.Clock()
    game = Game()
    
    running = True 
    
    while running:
        # --- 事件處理 ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                # --- Player 1 Controls (Arrow Keys) ---
                # Always exists at index 0
                if event.key == pygame.K_LEFT:
                    game.snakes[0].change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    game.snakes[0].change_direction(RIGHT)
                elif event.key == pygame.K_UP:
                    game.snakes[0].change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    game.snakes[0].change_direction(DOWN)
                
                # --- Player 2 Controls (WASD) ---
                # Only active in DUAL mode, exists at index 1
                if GAME_MODE == 'DUAL':
                    if event.key == pygame.K_a:
                        game.snakes[1].change_direction(LEFT)
                    elif event.key == pygame.K_d:
                        game.snakes[1].change_direction(RIGHT)
                    elif event.key == pygame.K_w:
                        game.snakes[1].change_direction(UP)
                    elif event.key == pygame.K_s:
                        game.snakes[1].change_direction(DOWN)
        
        # --- 邏輯更新 ---
        game_over = game.update() 
        
        if game_over:
            # 簡單結算顯示
            final_msg = "Game Over!"
            print(final_msg)
            print(f"Scores: {game.scores}")
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
