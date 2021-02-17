# Created by Vishal Reddy Mandadi (started working on Feb 12 at 11:35pm)
# Used to generate game display frames
import config
import paddle
from colorama import Fore
from time import time
class Frame:
    def __init__(self, width, height):
        self.width = config.FRAME_WIDTH
        self.height = config.FRAME_HEIGHT
        self.score_height = config.SCORE_BOX_HEIGHT
        self.matrix = [[' ' for i in range(self.width)] for j in range(self.height)] # printing gamebox
        self.score_matrix = [[' ' for i in range(self.width)] for j in range(self.height)] # for printing score and player info
        # setting broder of the frame
        for i in range(self.width):
            self.matrix[0][i] = '-'
            self.matrix[self.height-1][i] = '-'
        for i in range(self.height):
            self.matrix[i][0] = '|'
            self.matrix[i][self.width-1] = '|'

    def setScoreBox(self, ball1):
        config.FRAME_COUNT += 1
        current_time = time()
        time_elapsed = current_time - config.START_TIME
        for i in range(config.SCORE_BOX_HEIGHT):
            for j in range(config.FRAME_WIDTH):
                if j == 0 or j==config.FRAME_WIDTH - 1:
                    self.score_matrix[i][j] = '|'
                elif i==0 or i==config.SCORE_BOX_HEIGHT-1:
                    self.score_matrix[i][j] = '-'
                else:
                    self.score_matrix[i][j] = ' '
        scoreString = 'Score: ' + str(ball1.score)
        penaltyString = 'Penalty: ' + str(int(ball1.penalty))
        totalScoreString = 'Total Score: ' + str(ball1.score - int(ball1.penalty))
        lifeCountString = 'Available Lives: ' + str(ball1.life)
        velXString = 'Velocity of ball (Horizontal): ' + str(ball1.velX)
        velYString = 'Velocity of ball (Vertical): ' + str(ball1.velY)
        frameCountString = 'Frame count: ' + str(config.FRAME_COUNT)
        timeElapsedString = 'Time elapsed(in S): ' + str(round(time_elapsed, 2))
        for i in range(len(config.GAME_NAME)):
            self.score_matrix[1][(config.FRAME_WIDTH - len(config.GAME_NAME))//2 + i] = config.GAME_NAME[i]
        for i in range(len(scoreString)):
            self.score_matrix[2][i+1] = scoreString[i]
        for i in range(len(lifeCountString)):
            self.score_matrix[2][config.FRAME_WIDTH - 2 - len(lifeCountString) + i] = lifeCountString[i]
        for i in range(len(penaltyString)):
            self.score_matrix[3][i+1] = penaltyString[i]
        for i in range(len(totalScoreString)):
            self.score_matrix[3][config.FRAME_WIDTH - 2 - len(totalScoreString) + i] = totalScoreString[i]
        for i in range(len(velXString)):
            self.score_matrix[4][i+1] = velXString[i]
        for i in range(len(frameCountString)):
            self.score_matrix[4][config.FRAME_WIDTH - 2 - len(frameCountString) + i] = frameCountString[i]
        for i in range(len(velYString)):
            self.score_matrix[5][i+1] = velYString[i]
        for i in range(len(timeElapsedString)):
            self.score_matrix[5][config.FRAME_WIDTH - 2 - len(timeElapsedString) + i] = timeElapsedString[i]

    def setBoard(self, ball1):
        for i in range(1, self.width-1):
            self.matrix[config.FRAME_HEIGHT - config.BOTTOM_EMPTY_SPACE][i] = ' '
        for i in range(config.BALL_WIDTH):
            if ball1.y < 1 or ball1.x > config.FRAME_WIDTH - 2:
                print("Invalid ball position 1")
                exit(1)
            self.matrix[ball1.y][ball1.x + i] = ' '
        #for i in range(self.width):
        #    self.matrix[0][i] = '-'
        #    self.matrix[self.height-1][i] = '-'
        #for i in range(self.height):
        #    self.matrix[i][0] = '|'
        #    self.matrix[i][self.width-1] = '|'

    def setPaddle(self, paddle1):
        #self.setBoard()
        for i in range(paddle1.width):
            self.matrix[config.FRAME_HEIGHT - config.BOTTOM_EMPTY_SPACE][paddle1.x + i] = paddle1.shape[i]

    def setBall(self, ball1):
        #self.setBoard()
        for i in range(ball1.width):
            if ball1.y < 1 or ball1.x + i > config.FRAME_WIDTH - 2:
                print("Invalid ball position 2")
                exit(1)
            self.matrix[ball1.y][ball1.x + i] = ball1.shape[i]

    def printFrame(self, brick_array, ball1):
        # time elapsed and frame count will be set by setScoreBox function

        # Printing Score Box
        self.setScoreBox(ball1)
        for i in range(config.SCORE_BOX_HEIGHT):
            for j in range(config.FRAME_WIDTH):
                print(self.score_matrix[i][j], end='')
            print('')
        # Printing Game Box
        brick_iterator = 0 # implies the iterator is at first brick
        for i in range(self.height):
            count = 0
            for j in range(self.width):
                if j < count:
                    continue
                if brick_iterator < len(brick_array):
                    if i == brick_array[brick_iterator].y:
                        if j == brick_array[brick_iterator].x:
                            for k in range(config.BRICK_WIDTH):
                                if brick_array[brick_iterator].color == "RED":
                                    print(Fore.RED + brick_array[brick_iterator].shape[k], end="")
                                elif brick_array[brick_iterator].color == "BLUE":
                                    print(Fore.BLUE + brick_array[brick_iterator].shape[k], end="")
                                elif brick_array[brick_iterator].color == "GREEN":
                                    print(Fore.GREEN + brick_array[brick_iterator].shape[k], end="")
                                elif brick_array[brick_iterator].color == "WHITE":
                                    print(Fore.WHITE + brick_array[brick_iterator].shape[k], end="")
                                elif brick_array[brick_iterator].color == "NONE":  # Indicates broken brick
                                    print(Fore.WHITE + self.matrix[i][j+k], end ="")
                            count = j + config.BRICK_WIDTH
                            brick_iterator += 1
                        else:
                            print(Fore.WHITE + self.matrix[i][j], end ="")
                    else:
                        print(Fore.WHITE + self.matrix[i][j], end ="")
                else:
                    print(Fore.WHITE + self.matrix[i][j], end ="")
            print('')
            
            


'''
import curses
from curses import textpad
import random

def create_food(snake, box):
    food = None
    while food is None:
        food = [random.randint(box[0][0] + 1, box[1][0] - 1), 
                random.randint(box[0][1] + 1, box[1][1] - 1)]
        if food in snake:
            food = None
    return food

def print_score(stdscr, score):
    sh, sw = stdscr.getmaxyx()
    score_text = "Score: {}".format(score)
    stdscr.addstr(0, sw//2 - len(score_text)//2, score_text)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(150)


    sh, sw = stdscr.getmaxyx()
    box = [[3, 3], [sh-3, sw-3]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    snake = [[sh//2, sw//2 + 1], [sh//2, sw//2], [sh//2, sw//2 - 1], [sh//2, sw//2 - 2], [sh//2, sw//2 - 3], [sh//2, sw//2 - 4]]
    direction = curses.KEY_RIGHT

    for y, x in snake:
        stdscr.addstr(y, x, '>')
    
    food = create_food(snake, box)
    stdscr.addstr(food[0], food[1], '+')

    score = 0
    print_score(stdscr, score)
    
    while 1:
        key = stdscr.getch()
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            direction = key
        new_head = head = snake[0]
        #new_head = head
        if direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1]+1]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1]-1]
        elif direction == curses.KEY_UP:
            new_head = [head[0]-1, head[1]]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0]+1, head[1]]
            

        snake.insert(0, new_head)
        stdscr.addstr(new_head[0], new_head[1], '>')

        #stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
        #snake.pop()

        if snake[0]==food:
            food = create_food(snake, box)
            stdscr.addstr(food[0], food[1], '+')
            score += 1
            print_score(stdscr, score)
        else:
            stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
            snake.pop()

        if (snake[0][0] in [box[0][0], box[1][0]] or 
            snake[0][1] in [box[0][1], box[1][1]] or
            snake[0] in snake[1:]):
            msg = "GAME OVER!"
            stdscr.addstr(sh//2, sw//2 - len(msg)//2, msg)
            stdscr.nodelay(0)
            stdscr.getch()
            break

        stdscr.refresh()


curses.wrapper(main)
'''