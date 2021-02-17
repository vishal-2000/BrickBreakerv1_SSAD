import config

class Ball:
    def __init__(self):
        self.life = config.NO_OF_LIVES # Life count
        self.score = 0 # score counter
        self.penalty = 0 # The current frame in terms of multiples of frame_rate
        self.shape = config.BALL_SHAPE
        self.width = config.BALL_WIDTH
        self.velX = 0 # velocity (direction included) of ball in terms no of frames per move in x dir
        self.velY = 0 # velocity of ball in terms no of frames per move in y dir
        self.x = config.BALL_INITIAL_POS[0]
        self.y = config.BALL_INITIAL_POS[1]
        self.__frameCount = 0 # frame count (a private variable) used for speed calculation and control
        self.ballGrabbed = True # (Turns true when the ball is released)
        # frame count will be set to zero every time the paddle grabs the ball (grab implies the ball rests on the paddle until we choose to release it)

    def releaseBall(self):
        if self.ballGrabbed == False:
            return
        self.velX = config.BALL_INIT_VEL[0]
        self.velY = config.BALL_INIT_VEL[1]
        #self.__frameCount = 0 # to ensure that the ball moves immediately after release
        self.ballGrabbed = False

    def checkBrickCollision(self, brick_array):
        horizontal_collision = False
        vertical_collision = False
        for brick in brick_array:
            if brick.color != "NONE":
                if brick.y == self.y and ((brick.x - config.BALL_WIDTH ==  self.x and self.velX > 0) or (brick.x + config.BRICK_WIDTH ==self.x and self.velX < 0)): # horizontal collision with the brick
                    horizontal_collision = True
                    # self.velX = -1 * self.velX
                    brick.handleCollision() 
                    if brick.color != "WHITE":
                        self.score += 10
                if ((brick.y - 1 == self.y and self.velY > 0) or (brick.y + 1 == self.y and self.velY < 0)) and (brick.x - config.BALL_WIDTH  <= self.x and brick.x + config.BRICK_WIDTH >= self.x): # the brick is above/below the ball
                    vertical_collision = True
                    #self.velY = -1 * self.velY
                    brick.handleCollision() 
                    if brick.color != "WHITE":
                        self.score += 10
            else:
                continue
        if horizontal_collision == True:
            self.velX = -1 * self.velX
        if vertical_collision == True:
            self.velY = -1 * self.velY

    def checkPaddleCollision(self, paddle1):
        if self.y == paddle1.y: # a case where the ball intersects the paddle (error case)
            if (self.x < (paddle1.x + config.PADDLE_WIDTH)) and self.x > paddle1.x-config.BALL_WIDTH:
                #print('Invalid Collision')
                return True # implies game over
        if self.y == paddle1.y-1: # ball collides the upside of the paddle
            if (self.x < (paddle1.x + config.PADDLE_WIDTH)) and self.x > paddle1.x-config.BALL_WIDTH and self.velY > 0:
                #self.y = self.y - 1
                self.velY = -1 * self.velY
                # VelX depends on position where it hits the paddle
                if self.ballGrabbed==False:
                    if abs(self.velX) <= config.FRAME_RATE:
                        if abs(self.velX + (self.x - paddle1.x)*1 - (config.PADDLE_WIDTH-config.BALL_WIDTH)//2) <= config.FRAME_RATE:
                            self.velX = self.velX + (self.x - paddle1.x)*1 - (config.PADDLE_WIDTH-config.BALL_WIDTH)//2
        return False # implies game not over

    def checkCollision(self, paddle1, brick_array): # checks and handles collision
        game_over = False
        # check paddle collision
        game_over = self.checkPaddleCollision(paddle1)
        # check brick collision
        self.checkBrickCollision(brick_array)
        # check frame collision
        if self.y >= config.FRAME_HEIGHT - 1:
            game_over = True # implies game over
        if self.y == 1 and self.velY < 0:
            #self.y = 2
            print("Hi man is gameover=", game_over)
            self.velY = -1 * self.velY
        if self.x == 1 and self.velX < 0:
            #self.x = 2
            self.velX = -1 * self.velX
        if self.x == config.FRAME_WIDTH - 4 and self.velX > 0:
            #self.x = config.FRAME_WIDTH - 4
            self.velX = -1 * self.velX
        
        return game_over
        
    def moveBall(self, c):
        self.penalty = self.__frameCount/config.FRAME_RATE
        self.__frameCount += 1

        if self.ballGrabbed == True:
            if c=='d' and self.x < config.FRAME_WIDTH - 1 - config.BALL_WIDTH:
                self.x += 1
            if c=='a' and self.x > 1:
                self.x -= 1
        else:
            if self.velX !=0:
                #print('VelX = ',self.velX)
                if int(abs(config.FRAME_RATE//self.velX))==0:
                    print("Invalid velocity please check1 :", self.velX)
                    exit(1)
                if self.__frameCount%abs(int(config.FRAME_RATE//self.velX)) == 0:
                    self.x = self.x + int(1*(abs(self.velX)//self.velX))
            if self.velY !=0:
                if abs(config.FRAME_RATE//self.velY)==0:
                    print("Invalid velocity please check2 :", self.velY)
                    exit(1)
                if self.__frameCount%abs(config.FRAME_RATE//self.velY) == 0:
                    self.y = self.y + int(1*(abs(self.velY)//self.velY))
        