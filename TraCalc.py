import Ball
import json
import numpy as np

def calc_run():
    calc_read()

    head = np.array([310,110])
    end = np.array([330,130])


    cue = Ball.Ball(-1, head, head-end)
    calc_motion(cue)

    calc_write()

def calc_read():
    global balls
    Ball.Ball.width = WIDTH 
    Ball.Ball.height = HEIGHT
    Ball.Ball.radius = RADIUS
    Ball.Ball.corner_width = CORNER_WIDTH

    for id in range(balls.shape[0]):
        ballList.append(Ball.Ball(id, balls[id]))
        lineList.append({'id': id, 'lines': [balls[id]]})

def calc_motion(ball):
    if len(lineList[ball.id]['lines']) == 4:
        return
    id = calc_checkCollision(ball) 
    #collide
    if id != -1:
        ball.collide(ballList[id])

        calc_motion(ball)
        calc_motion(ballList[id])

        lineList[ball.id]['lines'].append(ball.position)
        lineList[id]['lines'].append(ballList[id].position)
    #bounce
    else:
        ball.bounce()

        lineList[ball.id]['lines'].append(ball.position)

        calc_motion(ball)

def calc_write():
    print(lineList)
    json.dumps(lineList)

def calc_checkCollision(ball):
    global balls
    nearest = -1, 10000
    for id in range(balls.shape[0]):
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
balls = np.array([[300,100],[200,200]])

ballList = [] 
lineList = []

calc_run()
print(bslls.shape[0])
