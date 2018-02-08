import ball
import json

class traCalc:
    def __init__(self):
        ballList = []
        lineList = [[]]
        
    def run(self):
        read()
        motion(ballList[0])
        write()

    def read():
        data = json.loads(open('data.json').read())
        Ball.width = data['width'] 
        Ball.height = data['height'] 
        Ball.radius = data['radius']
        balls = data['balls']

        for id in range(len(balls)):
            ball = balls[id]
            position = Pos(ball[0], ball[1])
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
        lines = dict()
        for id in range(nBalls):
            lines.update(id, lineList[id]) 
        a = json.dumps(lines)
        print(a)

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
    
