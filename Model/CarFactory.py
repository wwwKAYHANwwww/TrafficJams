from Car import Car 
import sys
from Config import Config
sys.path.append("..") 
from Logger.DataFileCarLogger import DataFileCarLogger
import random

class CarFactory(object):
    
    def __init__(self,numOfCars,logger,clock,view=None):
        self.numOfCars=numOfCars
        self.logger=logger
        self.view=view
        self.clock=clock
        self.cars=[]
        
    def startBuilding(self):
        position=0.0
        tmpCar1=Car(0,position,"car1", maxVelocity=25+random.uniform(-Config.CONST_MaxVelocityNoise, Config.CONST_MaxVelocityNoise), logger=self.logger)
        self.logger.initialize(tmpCar1)
        self.clock.addListener(tmpCar1)
        self.cars.append(tmpCar1)
        
        position += Config.CONST_MinimumDistance*2 + random.uniform(0,Config.CONST_MaxPositionNoise)
        for i in range(2,10):
            fileLogger=DataFileCarLogger()
            tmpCar2=Car(0,position,"car{}".format(i),maxVelocity=20+random.uniform(-Config.CONST_MaxVelocityNoise, Config.CONST_MaxVelocityNoise), logger=fileLogger)
            fileLogger.initialize(tmpCar2)
            tmpCar1.setFrontCar(tmpCar2)
            self.cars.append(tmpCar2)
            self.clock.addListener(tmpCar2)
            tmpCar1=tmpCar2
            position += Config.CONST_MinimumDistance*2 + random.uniform(0,Config.CONST_MaxPositionNoise)
            
        self.cars[-1].frontCar=self.cars[0]
        for i in self.cars:
            print(i.name,i.frontCar.name,i.x )


        