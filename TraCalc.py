import ball
import json

class TraCalc:

    global WIDTH
    global HEIGHT
    global RADIUS
    global CORNER_WIDTH
    global BALLS_LIST
    global STOKE


    def __init__(self):
        ballList = []
        lineList = [[]]
        nBalls = 0
        
    def run(self):
        read()
        target = checkTarget()
        motion(target)
        write()

    def read(self):
        #data = json.loads(open('data.json').read())
        Ball.width = WIDTH 
        Ball.height = HEIGHT
        Ball.radius = RADIUS
        Ball.corner_width = CORNER_WIDTH
        nBalls = len(BALLS_LIST)

        for id in range(nBalls):
            ballList.append(Ball(id, BALLS_LIST[id]))

    def checkTarget(self):
        for id in range(nBalls):
            print('a')


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
        print(lineList)

    def checkCollision(ball):
        nearest = -1, 10000
        for id in range(nBalls):
            if id == ball.id:
                continue
            #if more than one ball collides, need to compare distance of projection
            distance = ball.checkCollision(ballList[id])
            if distance != -1 & distance < nearest[1]:
                nearest = id, distance
        return nearest[0]
    
