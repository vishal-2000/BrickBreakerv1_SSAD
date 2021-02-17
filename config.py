# General
GAME_NAME = "The Brick Breaker Game"
START_TIME = 0.0 # this will be set by main.py and will be updated by the Frame class
FRAME_COUNT = 0 # this will be updated by the Frame class

# Frame
FRAME_HEIGHT = 30
FRAME_WIDTH = 80
SCORE_BOX_HEIGHT = 7
BOTTOM_EMPTY_SPACE = 3
FRAME_RATE = 24.0 # 24 frames per second

# Paddle
PADDLE_WIDTH = 7
PADDLE_HEIGHT = 1
PADDLE_SHAPE = '|-----|' 
PADDLE_INITIAL_POS = [(FRAME_WIDTH-PADDLE_WIDTH)//2, FRAME_HEIGHT - BOTTOM_EMPTY_SPACE] # (X, Y) COORDINATES LEFT END OF PADDLE 

# Ball
NO_OF_LIVES = 3
BALL_WIDTH = 3 
BALL_SHAPE = '(O)' # SHAPE = '(O)'
BALL_INIT_VEL = [0, -1 * FRAME_RATE//2]  # (direction - north west wrt the screen (keyboard - south)) (vel_x, vel_y) No of frames per move
BALL_INITIAL_POS = [PADDLE_INITIAL_POS[0] + (PADDLE_WIDTH - BALL_WIDTH)//2, PADDLE_INITIAL_POS[1] - 1] # (X, Y) LEFT END OF BALL

# Brick Width
BRICK_WIDTH = 5
BRICK_SHAPE = '{|||}'
