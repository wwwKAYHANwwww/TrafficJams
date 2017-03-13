from ITimeDependent import ITimeDependent

class Car(ITimeDependent):
    
    def __init__(self,v0,x0,maxVelocity=100,maxAcc=0.5,breakAcc=-0.1,criticalDistance=10,name,frontCar=None,logger=None):                                                                                   
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
        
        
    def setFrontCar(self,frontCar):
        self.frontCar=frontCar
        
    def update(self, time,timeStep):
        distance=(self.frontCar.x - self.x)
        self.acceleration = self.maxAcc if distance>self.criticalDistance else self.breakAcc
        
        if (self.v<self.maxVelocity) and (self.v>=0):
            self.v+=self.acceleration * timeStep
            
        self.x+= self.v * timeStep
        self.logger.log(time)
        
    
    