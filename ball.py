class Ball:
    width = 1440
    height = 900
    radius = 15
    
    def __init__(self, id, position = (0,0), heading = (0,0)):
        self.id = id
        self.position = position
        #determine the end point
        self.heading = heading
        self.endpoint = self.cal_endpoint()
    
    def cal_endpoint(self):
        width = 1440.0
        height = 900.0
        radius = 15.0
        if self.heading[0] == 0:
            if self.heading[1] == 0:
                return self.position
            elif self.heading[1] > 0:
                return (self.position[0],height)
            elif self.heading[1] < 0:
                return (self.position[0],0.0)
    
        elif self.heading[0] > 0:
            if self.heading[1] == 0:
                return (width,self.position[1])
            elif self.heading[1] > 0:
                if (width-self.position[0])/self.heading[0] > (height-self.position[1])/self.heading[1]:
                    return (self.position[0]+(self.heading[0])*((height-self.position[1])/self.heading[1]),height)
                elif (width-self.position[0])/self.heading[0] < (height-self.position[1])/self.heading[1]:
                    return (width,self.position[1]+(self.heading[1])*((width-self.position[0])/self.heading[0]))
                else:
                    return (width,height)
            else:
                if (width-self.position[0])/self.heading[0] > self.position[1]/(-self.heading[1]):
                    return (self.position[0]+(self.heading[0])*(self.position[1]/(-self.heading[1])),0.0)
                elif (width-self.position[0])/self.heading[0] < self.position[1]/(-self.heading[1]):
                    return (width,self.position[1]+(self.heading[1])*((width-self.position[0])/self.heading[0]))
                else:
                    return (width,0.0)


        elif self.heading[0] < 0:
            if self.heading[1] == 0:
                return (0.0,self.position[1])
            elif self.heading[1] > 0:
                if (self.position[0])/(-self.heading[0]) > (height-self.position[1])/self.heading[1]:
                    return (self.position[0]+(self.heading[0])*((height-self.position[1])/self.heading[1]),height)
                elif (self.position[0])/(-self.heading[0]) < (height-self.position[1])/self.heading[1]:
                    return (0.0,self.position[1]+(self.heading[1])*((self.position[0])/(-self.heading[0])))
                else:
                    return (0.0,height)
            else:
                if (self.position[0])/(-self.heading[0]) > self.position[1]/(-self.heading[1]):
                    return (self.position[0]+(self.heading[0])*(self.position[1]/(-self.heading[1])),0.0)
                elif (self.position[0])/(-self.heading[0]) < self.position[1]/(-self.heading[1]):
                    return (0.0,self.position[1]+(self.heading[1])*((width-self.position[0])/self.heading[0]))
                else:
                    return (0.0,0.0)



    #after collision, position will be the collision point, re-calculate the endpoints
    def collide(self, other):
        p_move = self.position
        v_move[0] = self.endpoint[0]-self.position[0]
        v_move[1] = self.endpoint[1]-self.position[1]
        p_hit = other.position
        
        self.position = other.position
        self.endpoint[0] = v_move[0] - ((v_move[0]*(p_move[1]-p_hit[1]))+(v_move[1]*(p_move[0]-p_hit[0])))*(p_move[0]-p_hit[0])/(dist(p_move,p_hit)**2)
        self.endpoint[1] = - ((v_move[0]*(p_move[1]-p_hit[1]))+(v_move[1]*(p_move[0]-p_hit[0])))*(p_move[0]-p_hit[0])/(dist(p_move,p_hit)**2)
        return  

    #check distance from point to line using area
    #return the projection distance
    def checkCollision(self, other):
        p1 = self.position
        p2 = self.endpoint
        p3 = other.position
        distance = area(p1,p2,p3)/dist(p1,p2)
        if distance < 2*radius:
            return ((p3[0]-p1[0])*(p2[1]-p1[1])+(p3[1]-p1[1])*(p2[0]-p1[0]))/dist(p1,p2)
        else:
            return -1
    
    def area(p1,p2,p3):
        return p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]-p1[0]*p3[1]-p2[0]*p1[1]-p3[0]*p2[1]
    
    def bounce(self):
        width = 1440.0
        height = 900.0
        radius = 15.0
        self.position = self.endpoint
        if self.endpoint[0] == 0 or self.endpoint[0] == width:
            self.heading = (-self.heading[0],self.heading[1])
        elif self.endpoint[1] == 0 or self.endpoint[1] == height:
            self.heading = (self.heading[0],-self.heading[1])
        self.endpoint = self.cal_endpoint()

    def dist(self, p1, p2):
        return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
