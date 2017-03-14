from ITimeDependent import ITimeDependent
from Config import Config

class Car(ITimeDependent):
    
    def __init__(self,v0,x0,name,maxVelocity=100,maxAcc=1,breakAcc=-15.0,criticalDistance=10,frontCar=None,logger=None):                                                                                   
        self.x=x0                                           
        self.v=v0                                            
        self.maxVelocity= maxVelocity             
        self.frontCar=frontCar;                             
        self.acceleration=0   
        self.breakAcc=breakAcc                         
        self.name=name
        self.maxAcc=maxAcc
        self.breakAcc=breakAcc
        self.criticalDistance=criticalDistance
        self.logger=logger
        self.breakDuration=0
        self.breakStartTime=0
        
    def setFrontCar(self,frontCar):
        self.frontCar=frontCar
        
    def update(self, time,timeStep):
        distance=self.distanceToFrontCar()
        
        if (self.breakDuration>0 and self.breakStartTime<time):
            self.acceleration=self.breakAcc
            self.breakDuration-=timeStep
            
        elif (distance<5):
            self.acceleration=0
            self.v=0
              
        elif (distance>self.criticalDistance):
            self.acceleration=self.maxAcc 
            
        else:
            self.acceleration=self.breakAcc
            
        
        if ((self.v<self.maxVelocity) and (self.v>=0))or((self.v>self.maxVelocity) and (self.acceleration<0))or((self.v<=0) and (self.acceleration>0)):
            self.v+=self.acceleration * timeStep
            
        self.x+= self.v * timeStep
        self.x=self.x%Config.CONST_LengthOfRoad
        self.logger.log(time)
       
    def distanceToFrontCar(self):
        d =  self.frontCar.x - self.x
        if d>=0:
            return d
        else:
            d =  abs(Config.CONST_LengthOfRoad -self.frontCar.x)+abs(Config.CONST_LengthOfRoad-self.frontCar.x)
            return d
    
    def pushBreak(self,breakDuration,startTime=0):
        self.breakDuration=breakDuration
        self.breakStartTime=startTime
        
    