# Created by Vishal Reddy Mandadi

import config
from brickMap1 import createMapLevel1
from paddle import Paddle
from ball import Ball
from frame import Frame
from os import system
from time import sleep
import input

# initialize objects of the game
paddle1 = Paddle()
ball1 = Ball()
frame1 = Frame(config.FRAME_WIDTH, config.FRAME_HEIGHT)
get_object = input.Get()
brick_array = []
createMapLevel1(brick_array)

#paddle1.printPaddle()

# rendering at FRAME_RATE frames per second
frame1.setBoard(ball1)
frame1.setPaddle(paddle1)
frame1.setBall(ball1)
frame1.printFrame(brick_array, ball1)

# switching off the cursor
system('setterm -cursor off')

# Handling input and main game loop
while(1):
    #sleep(2/config.FRAME_RATE)
    c = input.input_to(get_object, 2/config.FRAME_RATE) # here 2nd arguement mentions timeout (waiting time untill an input is recieved)
    system('clear')
    #system('setterm -cursor off')
    if c=='\x03':
        system('setterm -cursor on')
        break
    if c==' ':
        ball1.releaseBall()
    elif c=='d':
        paddle1.moveRight()
    elif c=='a':
        paddle1.moveLeft()
    frame1.setBoard(ball1) # erase the previous positions 
    ball1.moveBall(c) # now move ball
    game_over = ball1.checkCollision(paddle1, brick_array)
    if game_over == True:
        ball1.life -= 1
        if ball1.life==0:
            system('clear')
            frame1.printFrame(brick_array, ball1)
            print('G A M E O V E R')
            sleep(1)
            system('setterm -cursor on')
            exit(1)
        else:
            frame1.printFrame(brick_array, ball1)
            sleep(1)
            frame1 = Frame(config.FRAME_WIDTH, config.FRAME_HEIGHT)
            createMapLevel1(brick_array)
            ball1.x = config.BALL_INITIAL_POS[0]
            ball1.y = config.BALL_INITIAL_POS[1]
            ball1.velY = config.BALL_INIT_VEL[0]
            ball1.velX = config.BALL_INIT_VEL[1]
            ball1.ballGrabbed = True
            paddle1.x = config.PADDLE_INITIAL_POS[0]
            paddle1.y = config.PADDLE_INITIAL_POS[1]


    frame1.setPaddle(paddle1) # set paddle
    frame1.setBall(ball1) # set ball
    frame1.printFrame(brick_array, ball1)