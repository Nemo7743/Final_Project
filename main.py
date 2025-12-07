import pygame
import sys
from settings import *
from game import Game 

def run_game(game_mode):
    """
    Runs the game loop.
    :param game_mode: 'CLASSIC' or 'DUAL'
    :return: Dictionary containing scores and winner info.
    """
    # Check if screen is already initialized (for Menu integration)
    screen = pygame.display.get_surface()
    if screen is None:
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(f"Python Snake - {game_mode} Mode")
    
    clock = pygame.time.Clock()
    
    # Pass game_mode to the Game class
    game = Game(game_mode)
    
    running = True 
    game_result = None

    while running:
        # --- 事件處理 ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If window is closed, we return None or a specific flag
                # to let the main menu handle the shutdown
                return None 
            
            if event.type == pygame.KEYDOWN:
                # --- Player 1 Controls (Arrow Keys) ---
                if event.key == pygame.K_LEFT:
                    game.snakes[0].change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    game.snakes[0].change_direction(RIGHT)
                elif event.key == pygame.K_UP:
                    game.snakes[0].change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    game.snakes[0].change_direction(DOWN)
                
                # --- Player 2 Controls (WASD) ---
                # Use local game_mode argument
                if game_mode == 'DUAL':
                    if event.key == pygame.K_a:
                        game.snakes[1].change_direction(LEFT)
                    elif event.key == pygame.K_d:
                        game.snakes[1].change_direction(RIGHT)
                    elif event.key == pygame.K_w:
                        game.snakes[1].change_direction(UP)
                    elif event.key == pygame.K_s:
                        game.snakes[1].change_direction(DOWN)
        
        # --- 邏輯更新 ---
        # update() returns None if game continues, or a dict if game over
        result = game.update() 
        
        if result is not None:
            game_result = result
            
            # 簡單結算顯示
            final_msg = "Game Over!"
            print(final_msg)
            print(f"Result: {game_result}")
            
            # Small delay to see the crash
            pygame.time.delay(1000)
            running = False 

        # --- 畫面繪製 ---
        screen.fill(BLACK)
        game.draw(screen)
        pygame.display.update()
        
        clock.tick(FPS)

    # Return the stats to the caller (Menu)
    return game_result

if __name__ == '__main__':
    # Standalone testing block
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Test")
    
    # Force a mode for testing
    mode = GAME_MODE # From settings.py
    
    result = run_game(mode)
    print(f"Final Return Data: {result}")
    
    pygame.quit()
    sys.exit()
