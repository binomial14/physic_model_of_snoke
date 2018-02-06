import ball
import json


def trajectoryCalc():
    t = traClac()
    t.read()
    t.motion(t.ballList[0])
    t.write()

class traCalc:
    def __init__(self):
        ballList = []
        

    def read:
        data = json.loads(open('data.json').read())
        width = data['width'] 
        height = data['height'] 
        radius = data['radius']
        heading = Pos(data[''])
        balls = data['balls']
        for i in range(len(balls)):
            ball = balls[i]
            id = ball['id']
            position = Pos(ball['x'], ball['y'])
            ballList.append(Ball(id, position))

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
        for id in range(nBalls):
            if id == ball.id:
                continue
            #if more than one ball collides, need to compare distance of projection
            distance = ball.checkCollision(ballList[id])
            if distance != -1 & distance < nearest[1]:
                nearest = [id, distance]
        return nearest[0]
    
