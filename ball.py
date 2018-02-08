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
    width = 1440
    height = 900
    radius = 15
    
    def __init__(self, id, position = Pos(0,0), heading = Pos(0,0)):
        width = 1440.0
        height = 900.0
        radius = 15.0
        self.id = id
        self.position = position
        #determine the end point
        if heading.x == 0:
            if heading.y == 0:
                self.endpoint = position
            elif heading.y > 0:
                self.endpoint = Pos(self.position.x,height)
            elif heading.y < 0:
                self.endpoint = Pos(self.position.x,0.0)
    
        elif heading.x > 0:
            if heading.y == 0:
                self.endpoint = Pos(width,self.position.y)
            elif heading.y > 0:
                if (width-self.position.x)/heading.x > (height-self.position.y)/heading.y:
                    self.endpoint = Pos(self.position.x+(heading.x)*((height-self.position.y)/heading.y),height)
                elif (width-self.position.x)/heading.x < (height-self.position.y)/heading.y:
                    self.endpoint = Pos(width,self.position.y+(heading.y)*((width-self.position.x)/heading.x))
                else:
                    self.endpoint = Pos(width,height)
            else:
                if (width-self.position.x)/heading.x > self.position.y/(-heading.y):
                    self.endpoint = Pos(self.position.x+(heading.x)*(self.position.y/(-heading.y)),0.0)
                elif (width-self.position.x)/heading.x < self.position.y/(-heading.y):
                    self.endpoint = Pos(width,self.position.y+(heading.y)*((width-self.position.x)/heading.x))
                else:
                    self.endpoint = Pos(width,0.0)


        elif heading.x < 0:
            if heading.y == 0:
                self.endpoint = Pos(0.0,self.position.y)
            elif heading.y > 0:
                if (self.position.x)/(-heading.x) > (height-self.position.y)/heading.y:
                    self.endpoint = Pos(self.position.x+(heading.x)*((height-self.position.y)/heading.y),height)
                elif (self.position.x)/(-heading.x) < (height-self.position.y)/heading.y:
                    self.endpoint = Pos(0.0,self.position.y+(heading.y)*((self.position.x)/(-heading.x)))
                else:
                    self.endpoint = Pos(0.0,height)
            else:
                if (self.position.x)/(-heading.x) > self.position.y/(-heading.y):
                    self.endpoint = Pos(self.position.x+(heading.x)*(self.position.y/(-heading.y)),0.0)
                elif (self.position.x)/(-heading.x) < self.position.y/(-heading.y):
                    self.endpoint = Pos(0.0,self.position.y+(heading.y)*((width-self.position.x)/heading.x))
                else:
                    self.endpoint = Pos(0.0,0.0)
        self.heading = heading



    #after collision, position will be the collision point, re-calculate the endpoints
    def collide(self, other):
        p_move = self.position
        v_move_x = self.endpoint.x-self.position.x
        v_move_y = self.endpoint.y-self.position.y
        p_hit = other.position
        
        self.position = other.position
        self.endpoint.x = v_move_x - ((v_move_x*(p_move.y-p_hit.y))+(v_move_y*(p_move.x-p_hit.x)))*(p_move.x-p_hit.x)/(dist(p_move,p_hit)**2)
        self.endpoint.y = - ((v_move_x*(p_move.y-p_hit.y))+(v_move_y*(p_move.x-p_hit.x)))*(p_move.x-p_hit.x)/(dist(p_move,p_hit)**2)
        return  

    #check distance from point to line using area
    #return the projection distance
    def checkCollision(self, other):
        p1 = self.position
        p2 = self.endpoint
        p3 = other.position
        distance = area(p1,p2,p3)/dist(p1,p2)
        if distance < 2*radius:
            return ((p3.x-p1.x)*(p2.y-p1.y)+(p3.y-p1.y)*(p2.x-p1.x))/dist(p1,p2)
        else:
            return -1
    
    def area(p1,p2,p3):
        return p1.x*p2.y+p2.x*p3.y+p3.x*p1.y-p1.x*p3.y-p2.x*p1.y-p3.x*p2.y
    
    def bounce(self):
        width = 1440.0
        height = 900.0
        radius = 15.0
        self.position = self.endpoint
        if self.endpoint.x == 0 or self.endpoint.x == width:
            self.heading = Pos(-self.heading.x,self.heading.y)
        elif self.endpoint.y == 0 or self.endpoint.y == height:
            self.heading = Pos(self.heading.x,-self.heading.y)

