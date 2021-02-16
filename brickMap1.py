# Level 1 brick map
# This map creates and returns brick object array
from config import BRICK_WIDTH, FRAME_HEIGHT, FRAME_WIDTH, BOTTOM_EMPTY_SPACE
from brick import RedBrick, BlueBrick, GreenBrick, WhiteBrick
# Organization 
# layer 4 b g r b b r g b
# layer 3   r b g g b r
# layer 2     r w g b 
# layer 1       b g
def createMapLevel1(brick_array):
    # layer 4
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 4*BRICK_WIDTH, 4))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 4))
    brick_array.append(RedBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 4))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 4))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 4))
    brick_array.append(RedBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 4))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 4))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) + 3*BRICK_WIDTH, 4))
    # layer 3
    brick_array.append(RedBrick((FRAME_WIDTH//2) - 3*BRICK_WIDTH, 5))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 5))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 5))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) + 0*BRICK_WIDTH, 5))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 5))
    brick_array.append(RedBrick((FRAME_WIDTH//2) + 2*BRICK_WIDTH, 5))
    # layer 2
    brick_array.append(RedBrick((FRAME_WIDTH//2) - 2*BRICK_WIDTH, 6))
    brick_array.append(WhiteBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 6))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 6))
    brick_array.append(BlueBrick((FRAME_WIDTH//2) + 1*BRICK_WIDTH, 6))
    # layer 1
    brick_array.append(BlueBrick((FRAME_WIDTH//2) - 1*BRICK_WIDTH, 7))
    brick_array.append(GreenBrick((FRAME_WIDTH//2) - 0*BRICK_WIDTH, 7))