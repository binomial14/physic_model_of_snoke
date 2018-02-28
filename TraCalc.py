import Ball
import numpy as np

global WIDTH
global HEIGHT
global RADIUS
global CORNER_WIDTH
global BALLS_LIST
global STOKE

ballList = []
lineList = [[]]
nBalls = 0
COUNT = 0

def run():
    read()

    heading = (STOKE[0][0]-STOKE[1][0], STOKE[0][1]-STOKE[1][1])
    stoke = Ball.Ball(-1, STOKE[0], heading)
    motion(stoke)

    write()

def read():
    Ball.width = WIDTH 
    Ball.height = HEIGHT
    Ball.radius = RADIUS
    Ball.corner_width = CORNER_WIDTH
    nBalls = len(BALLS_LIST)


    for id in range(nBalls):
        ballList.append(Ball.Ball(id, BALLS_LIST[id]))
        lineList[id].append(BALLS_LIST[id])

def motion(ball):
    global COUNT
    if COUNT >= 4:
        return
    id = checkCollision(ball) 
    #collide
    if id != -1:
        ball.collide(self.ballList[id])
        motion(ball)
        motion(ballList[id])
        lineList[ball.id].append(ball.position)
        lineList[id].append(ballList[id].position)
    #bounce
    else:
        ball.bounce()
        lineList[ball.id].append(ball.position)
        motion(ball)

    COUNT += 1

def write():
    print(lineList)

def checkCollision(ball):
    nearest = -1, 10000
    for id in range(nBalls):
        if id == ball.id:
            continue
        #if more than one ball collides, need to compare distance of projection
        distance = ball.checkCollision(ballList[id])
        if distance != -1 and distance < nearest[1]:
            nearest = id, distance
    return nearest[0]
    
WIDTH = 1000
HEIGHT = 500
RADIUS = 12
CORNER_WIDTH = 20
BALLS_LIST = [(300,100)]
STOKE = [(300, 310), (320, 330)]
run()
print(a.nBalls)
