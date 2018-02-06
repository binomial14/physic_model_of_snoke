import ball
import json

ballList = []

def trajectoryCalc():
    t = traClac()
    t.read()
    t.motion(ballList[0])
    t.write()

class traCalc:
    def __init__(self)
        width = 100
        height = 50
        radius = 5
        nballs = 16

    def read:
        for id in range(nballs):
            position = 
            heading = 
            ballList.append(Ball(id, position, heading))

    def motion(ball):
        id = checkCollision(ball) 
        #collide
        if id != -1:
            ball.collide(ballList[id])
            motion(ball)
            motion(ballList[id])
        #bounce
        else:
            ball.bounce()

    def write():
        return


    def checkCollision(ball):
        nearest = [-1, 10000] 
        for id in range(nballs):
            if id == ball.id:
                continue
            #if more than one ball collides, need to compare distance of projection
            distance = ball.checkCollision(ballList[id])
            if distance != -1 && distance < nearest[1]:
                nearest = [id, distance]
        return nearest[0]
    
