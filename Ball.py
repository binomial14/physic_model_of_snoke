import time

import math
import numpy as np

class Ball:
    width = 582.0
    height = 303.0
    radius = 15.0
    
    def __init__(self, id, position = np.array([0,0]), heading = np.array([0,0])):
        self.id = id
        self.position = position
        #determine the end point
        self.heading = heading
        self.endpoint = self.cal_endpoint()
    
    def cal_endpoint(self):
        
        if self.heading[0] == 0:
            if self.heading[1] == 0:
                return self.position
            elif self.heading[1] > 0:
                return ([self.position[0],self.height])
            elif self.heading[1] < 0:
                return ([self.position[0],0.0])
    
        elif self.heading[0] > 0:
            if self.heading[1] == 0:
                return ([self.width,self.position[1]])
            elif self.heading[1] > 0:
                if (self.width-self.position[0])/self.heading[0] > (self.height-self.position[1])/self.heading[1]:
                    return ([self.position[0]+(self.heading[0])*((self.height-self.position[1])/self.heading[1]),self.height])
                elif (self.width-self.position[0])/self.heading[0] < (self.height-self.position[1])/self.heading[1]:
                    return ([self.width,self.position[1]+(self.heading[1])*((self.width-self.position[0])/self.heading[0])])
                else:
                    return ([self.width,self.height])
            else:
                if (self.width-self.position[0])/self.heading[0] > self.position[1]/(-self.heading[1]):
                    return ([self.position[0]+(self.heading[0])*(self.position[1]/(-self.heading[1])),0.0])
                elif (self.width-self.position[0])/self.heading[0] < self.position[1]/(-self.heading[1]):
                    return ([self.width,self.position[1]+(self.heading[1])*((self.width-self.position[0])/self.heading[0])])
                else:
                    return ([self.width,0.0])


        elif self.heading[0] < 0:
            if self.heading[1] == 0:
                return ([0.0,self.position[1]])
            elif self.heading[1] > 0:
                if (self.position[0])/(-self.heading[0]) > (self.height-self.position[1])/self.heading[1]:
                    return ([self.position[0]+(self.heading[0])*((self.height-self.position[1])/self.heading[1]),self.height])
                elif (self.position[0])/(-self.heading[0]) < (self.height-self.position[1])/self.heading[1]:
                    return ([0.0,self.position[1]+(self.heading[1])*((self.position[0])/(-self.heading[0]))])
                else:
                    return ([0.0,self.height])
            else:
                if (self.position[0])/(-self.heading[0]) > self.position[1]/(-self.heading[1]):
                    return ([self.position[0]+(self.heading[0])*(self.position[1]/(-self.heading[1])),0.0])
                elif (self.position[0])/(-self.heading[0]) < self.position[1]/(-self.heading[1]):
                    return ([0.0,self.position[1]+(self.heading[1])*((self.position[0])/(-self.heading[0]))])
                else:
                    return ([0.0,0.0])



    #after collision, position will be the collision point, re-calculate the endpoints
    def collide(self, other):
        original_heading = ([self.heading[0],self.heading[1]])
        other.heading = ([(((self.heading[0]*(self.position[0]-other.position[0]))+(self.heading[1]*(self.position[1]-other.position[1])))*(self.position[0]-other.position[0])/(self.dist(self.position,other.position)**2)),(((self.heading[0]*(self.position[0]-other.position[0]))+(self.heading[1]*(self.position[1]-other.position[1])))*(self.position[1]-other.position[1])/(self.dist(self.position,other.position)**2))])
        self.heading = ([(self.heading[0] - ((self.heading[0]*(self.position[0]-other.position[0]))+(self.heading[1]*(self.position[1]-other.position[1])))*(self.position[0]-other.position[0])/(self.dist(self.position,other.position)**2)),(self.heading[1] - ((self.heading[0]*(self.position[0]-other.position[0]))+(self.heading[1]*(self.position[1]-other.position[1])))*(self.position[1]-other.position[1])/(self.dist(self.position,other.position)**2))])
        a = original_heading[0]**2+original_heading[1]**2
        b = 2*((self.position[0]-other.position[0])*(original_heading[0])+(self.position[1]-other.position[1])*(original_heading[1]))
        c = ((self.position[0]-other.position[0])**2+(self.position[1]-other.position[1])**2)-4*self.radius**2
        t = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        
        self.position = ([self.position[0]+t*original_heading[0],self.position[1]+t*original_heading[1]])
        self.endpoint = self.cal_endpoint()
        other.endpoint = other.cal_endpoint()

    #check distance from point to line using area
    #return the projection distance
    def checkCollision(self, other, scale = 1):
        p1 = self.position
        p2 = self.endpoint
        p3 = other.position
        distance = self.area(p1,p2,p3)/self.dist(p1,p2)
        if (distance <= 2*self.radius*scale) & (((p3[0]-p1[0])*(p2[0]-p1[0])+(p3[1]-p1[1])*(p2[1]-p1[1]))/self.dist(p1,p2) > -1):
            return ((p3[0]-p1[0])*(p2[0]-p1[0])+(p3[1]-p1[1])*(p2[1]-p1[1]))/self.dist(p1,p2)
        else:
            return -1
    
    def area(self,p1=(0,0),p2=(0,0),p3=(0,0)):
        return abs(p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]-p1[0]*p3[1]-p2[0]*p1[1]-p3[0]*p2[1])
    
    def bounce(self):
        if self.endpoint[0] == 0 :
            self.position = ([self.radius,self.endpoint[1]-self.radius*(self.heading[1])/(-self.heading[0])])
            self.heading = ([-self.heading[0],self.heading[1]])

        elif self.endpoint[0] == self.width :
            self.position = ([self.width-self.radius,self.endpoint[1]-self.radius*self.heading[1]/self.heading[0]])
            self.heading = ([-self.heading[0],self.heading[1]])
            
        elif self.endpoint[1] == 0 :
            self.position = ([self.endpoint[0]-self.radius*self.heading[0]/(-self.heading[1]),self.radius])
            self.heading = ([self.heading[0],-self.heading[1]])

        elif self.endpoint[1] == self.height :
            self.position = ([self.endpoint[0]-self.radius*self.heading[0]/self.heading[1],self.height-self.radius])
            self.heading = ([self.heading[0],-self.heading[1]])
            
        self.endpoint = self.cal_endpoint()

    def dist(self, p1 = (0,0), p2 = (0,0)):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
'''
ts = time.time()

ball1 = Ball(1,([70,20]),([1,-1]))
print("Ball1 position : ", ball1.position[0],',',ball1.position[1])
print("Ball1 endpoint : ",ball1.endpoint[0],',',ball1.endpoint[1])
print("Ball1 heading : ",ball1.heading[0],',',ball1.heading[1])
ball1.bounce()
print("Ball1 position : ",ball1.position[0],',',ball1.position[1])
print("Ball1 endpoint : ",ball1.endpoint[0],',',ball1.endpoint[1])
print("Ball1 heading : ",ball1.heading[0],',',ball1.heading[1])

ball2 = Ball(2,([15,15]),([1,0]))
ball3 = Ball(3,([200,20]),([0,0]))
print("Ball2 position : ",ball2.position[0],',',ball2.position[1])
print("Ball2 endpoint : ",ball2.endpoint[0],',',ball2.endpoint[1])
print("Ball2 heading : ",ball2.heading[0],',',ball2.heading[1])

print("Ball3 position : ",ball3.position[0],',',ball3.position[1])
print("Ball3 endpoint : ",ball3.endpoint[0],',',ball3.endpoint[1])
print("Ball3 heading : ",ball3.heading[0],',',ball3.heading[1])

print("Ball2 check : ",ball2.checkCollision(ball3,1))
ball2.collide(ball3)
print("Ball2 position : ",ball2.position[0],',',ball2.position[1])
print("Ball2 endpoint : ",ball2.endpoint[0],',',ball2.endpoint[1])
print("Ball2 heading : ",ball2.heading[0],',',ball2.heading[1])

print("Ball3 position : ",ball3.position[0],',',ball3.position[1])
print("Ball3 endpoint : ",ball3.endpoint[0],',',ball3.endpoint[1])
print("Ball3 heading : ",ball3.heading[0],',',ball3.heading[1])

#ball0 = Ball(0,([500,250]),([,]))

te = time.time()
print("It cost %f sec"%(te-ts))


ball2 = Ball(2,([310,110]),([20,0]))
ball3 = Ball(3,([214,130]),([0,0]))
print("Ball2 position : ",ball2.position[0],',',ball2.position[1])
print("Ball2 endpoint : ",ball2.endpoint[0],',',ball2.endpoint[1])
print("Ball2 heading : ",ball2.heading[0],',',ball2.heading[1])

print("Ball3 position : ",ball3.position[0],',',ball3.position[1])
print("Ball3 endpoint : ",ball3.endpoint[0],',',ball3.endpoint[1])
print("Ball3 heading : ",ball3.heading[0],',',ball3.heading[1])

print("Ball2 check : ",ball2.checkCollision(ball3,1))
ball2.collide(ball3)
print("Ball2 position : ",ball2.position[0],',',ball2.position[1])
print("Ball2 endpoint : ",ball2.endpoint[0],',',ball2.endpoint[1])
print("Ball2 heading : ",ball2.heading[0],',',ball2.heading[1])

print("Ball3 position : ",ball3.position[0],',',ball3.position[1])
print("Ball3 endpoint : ",ball3.endpoint[0],',',ball3.endpoint[1])
print("Ball3 heading : ",ball3.heading[0],',',ball3.heading[1])
'''
