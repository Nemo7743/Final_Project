# --- 視窗與遊戲設定 ---
BLOCK_SIZE = 20
WIDTH = 30    # 格子數 (寬)
HEIGHT = 20   # 格子數 (高)
SCREEN_WIDTH = WIDTH * BLOCK_SIZE
SCREEN_HEIGHT = HEIGHT * BLOCK_SIZE
FPS = 5 

# --- 遊戲模式設定 ---
# Options: 'CLASSIC' (1 Player), 'DUAL' (2 Players)
GAME_MODE = 'DUAL'

# --- 顏色定義 ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)  # New color for Player 2

# --- 方向定義 ---
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
