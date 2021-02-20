# Assignment2_SSAD
The Brick Breaker Game using python3 and OOPS concepts (DASS course assignment (14th to 17th Feb))
## Creator information
- Created by Vishal Reddy Mandadi 
- DASS Course assignment 2

## How to run the game
### Dependencies
- Python 3
- Numpy
### Run instructions
- Download the zip file from github or moodle
- Extract all files
- Enter 'python3 main.py' command in the terminal (or in simple terms just execute the main.py file)

## Controls
- 'a' to move the paddle left
- 'd' to move the paddle right
- ' ' or spacebar to release the ball from the paddle
## Score
- Each collision with a breakable brick awards 10 points
- A penalty of 1 point is incurred after every 24 frames
- The total score = (no of breakable brick collisions) - (no of frames until end of the game / 24) 

## Lives
- You will be given 3 lives
- No penalty incurred if you lose a life
- When you lose your life, all the active powerups will be deactivated

## Bricks
- White bricks are unbreakable
- Red bricks will break after 3 collisions
- Blue bricks will break after 2 collisions
- Green bricks will break after 1 collision
- Yellow bricks called exploding bricks break after 1 collision and break all the bricks adjacent or diagonal to them

## Powerups
Catch the powerups with the paddle to activate them (they are hidden in the breaks and start falling down once the corresponding bricks are broken)
- '$EP$' - expands the paddle
- '$SP$' - Shrinks the paddle
- '$PG$' - Paddle grab (The ball will be grabbed by the paddle on collision with it, it can be released by clicking the spacebar)
- '$BM$' - Ball multiplier (Introduces an extraball into the game which starts from a certain initial position)
- '$FB$' - Fast Ball (Increases the speed of the ball)
- '$TB$' - Through Ball (The ball can go undeflected by the bricks and all those bricks which come into contact will be smashed (including the unbreakable type))

## Bonus Implemented!
- The yellow colored bricks are called exploding bricks
- They appear in packs of size more than 6
- On collision all the adjacent and diagonal bricks break
- The exploding bricks even break the unbreakable ones

