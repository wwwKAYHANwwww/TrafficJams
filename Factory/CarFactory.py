import sys
sys.path.append("..") 

from Model.Car import Car 
from Model.Config import Config
from Logger.DataFileCarLogger import DataFileCarLogger
import random

class CarFactory(object):
    
    def __init__(self,numOfCars,carLogger,clock,view=None):
        self.numOfCars=numOfCars
        self.carLogger=carLogger
        self.view=view
        self.clock=clock
        self.cars=[]
        
    def startBuilding(self):
        
        position=0.0
        tmpCar1=Car(0,position,"car1", maxVelocity=self.getRandomMaxVelocity(25),)

        self.clock.addListener(tmpCar1)
        self.cars.append(tmpCar1)
        
        position =self.getRandomPosition(position) 
        for i in range(2,self.numOfCars):
            tmpCar2=Car(0,position,"car{}".format(i),maxVelocity=self.getRandomMaxVelocity(25),)
            tmpCar1.setFrontCar(tmpCar2)
            self.cars.append(tmpCar2)
            self.clock.addListener(tmpCar2)
            tmpCar1=tmpCar2
            position =self.getRandomPosition(position) 
            
        
        self.cars[-1].frontCar=self.cars[0]
        #for i in self.cars:
        #    print(i.name,i.frontCar.name,i.x )
            
        self.carLogger.initialize(self.cars)
        

    def getRandomMaxVelocity(self,mean):
        return mean+random.uniform(-Config.CONST_MaxVelocityNoise, Config.CONST_MaxVelocityNoise)
        
    def getRandomPosition(self,previousPosition):
        return previousPosition+Config.CONST_MinimumDistance*2 + random.uniform(0,Config.CONST_MaxPositionNoise)
    
    def setRandomBreak(self,startTime,duration):
        ind=int(random.uniform(0,self.numOfCars-1))
        #ind=5
        self.cars[ind].pushBreak(duration,startTime=startTime)
        