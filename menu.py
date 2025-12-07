import pygame
import sys
from settings import *
from main import run_game

def draw_text_centered(surface, text, font, color, y_offset):
    """Helper to draw centered text"""
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
    surface.blit(text_obj, text_rect)

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Python Snake - Main Menu")
    
    clock = pygame.time.Clock()
    
    # Fonts
    title_font = pygame.font.SysFont('Arial', 40, bold=True)
    info_font = pygame.font.SysFont('Arial', 24)
    inst_font = pygame.font.SysFont('Arial', 18)

    # Menu State
    current_mode = 'CLASSIC' # Default mode
    last_result = None
    
    running = True
    
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    # Toggle Mode
                    current_mode = 'DUAL' if current_mode == 'CLASSIC' else 'CLASSIC'
                
                elif event.key == pygame.K_RETURN:
                    # --- START GAME ---
                    # Call the function from main.py
                    result = run_game(current_mode)
                    
                    # Handle return values
                    if result is None:
                        # If run_game returns None, the user closed the window during the game
                        running = False
                    else:
                        # Game finished naturally, store results
                        last_result = result
                        # Reset caption to Menu (since game changed it)
                        pygame.display.set_caption("Python Snake - Main Menu")
        
        # --- Drawing ---
        screen.fill(BLACK)
        
        # 1. Title
        draw_text_centered(screen, "PYTHON SNAKE", title_font, GREEN, SCREEN_HEIGHT // 6)
        
        # 2. Current Mode
        mode_text = f"Current Mode: < {current_mode} >"
        draw_text_centered(screen, mode_text, info_font, WHITE, SCREEN_HEIGHT // 3)
        draw_text_centered(screen, "(Press 'M' to toggle)", inst_font, (150, 150, 150), SCREEN_HEIGHT // 3 + 30)

        # 3. Last Game Info
        if last_result:
            scores = last_result['scores']
            winner = last_result['winner']
            
            draw_text_centered(screen, "--- Last Game ---", inst_font, WHITE, SCREEN_HEIGHT // 2)
            
            if current_mode == 'DUAL' or len(scores) > 1:
                # Dual Mode Result Display
                score_str = f"P1: {scores[0]}  -  P2: {scores[1]}"
                if winner == 0:
                    win_msg = "Winner: Player 1 (Green)"
                    win_col = GREEN
                elif winner == 1:
                    win_msg = "Winner: Player 2 (Yellow)"
                    win_col = YELLOW
                else:
                    win_msg = "Draw / Game Over"
                    win_col = RED
                
                draw_text_centered(screen, win_msg, info_font, win_col, SCREEN_HEIGHT // 2 + 30)
                draw_text_centered(screen, score_str, info_font, WHITE, SCREEN_HEIGHT // 2 + 60)
            else:
                # Classic Mode Result Display
                score_str = f"Final Score: {scores[0]}"
                draw_text_centered(screen, score_str, info_font, GREEN, SCREEN_HEIGHT // 2 + 30)
        else:
            # Placeholder if no game played yet
            draw_text_centered(screen, "No Previous Game", inst_font, (100, 100, 100), SCREEN_HEIGHT // 2 + 30)

        # 4. Instructions
        draw_text_centered(screen, "Press ENTER to Start", title_font, RED, SCREEN_HEIGHT * 3 // 4)

        pygame.display.update()
        clock.tick(15) # Low FPS is fine for menu

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main_menu()
