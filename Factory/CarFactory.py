import sys
sys.path.append("..") 

from Model.Car import Car 
from Model.Config import Config
from Logger.DataFileCarLogger import DataFileCarLogger
import random

class CarFactory(object):
    
    def __init__(self,numOfCars,loggerFactory,clock,view=None):
        self.numOfCars=numOfCars
        self.loggerFactory=loggerFactory
        self.view=view
        self.clock=clock
        self.cars=[]
        
    def startBuilding(self):
        fileLogger=self.loggerFactory.getLogger()
        position=0.0
        tmpCar1=Car(0,position,"car1", maxVelocity=self.getRandomMaxVelocity(25), logger=fileLogger)
        fileLogger.initialize(tmpCar1)
        self.clock.addListener(tmpCar1)
        self.cars.append(tmpCar1)
        
        position =self.getRanfomPosition(position) 
        for i in range(2,10):
            fileLogger=self.loggerFactory.getLogger()
            tmpCar2=Car(0,position,"car{}".format(i),maxVelocity=self.getRandomMaxVelocity(25), logger=fileLogger)
            fileLogger.initialize(tmpCar2)
            tmpCar1.setFrontCar(tmpCar2)
            self.cars.append(tmpCar2)
            self.clock.addListener(tmpCar2)
            tmpCar1=tmpCar2
            position =self.getRanfomPosition(position) 
            
        self.cars[-1].frontCar=self.cars[0]
        for i in self.cars:
            print(i.name,i.frontCar.name,i.x )


    def getRandomMaxVelocity(self,mean):
        return mean+random.uniform(-Config.CONST_MaxVelocityNoise, Config.CONST_MaxVelocityNoise)
        
    def getRanfomPosition(self,previousPosition):
        return previousPosition+Config.CONST_MinimumDistance*2 + random.uniform(0,Config.CONST_MaxPositionNoise)