class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x & self.y == other.y
        
    def __ne__(self, other):
        return self.x != other.x | self.y != other.y
        
    def __add__(self, other):
        return Pos(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Pos(self.x-other.x, self.y-other.y)

    def dist(self, other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)




class Ball:
    def __init__(self, id, position, heading = Pos(0, 0)):
        self.id = id
        self.position = position
        self.endpoint = 

    #after collision, position will be the collision point, re-calculate the endpoints
    def collide(self, other):
        return 0 

    #check distance from point to line using area
    #return the projection distance
    def checkCollision(self):
        tmp1 = 
        return 0

    def bounce(self):
        return 0
