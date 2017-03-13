from Car import Car
from Clock import Clock
import random
from Logger.DataFileCarLogger import DataFileCarLogger

CONST_MinimumDistance = 10
CONST_MaxNoise = 1
CONST_LengthOfRoad=1000

cars=[]
tmpCar1=Car(10,15,20,"car1")
cars.append(tmpCar1)


clock=Clock(.1, 20)

position = 0.
for i in range(2,10):
    fileLogger=DataFileCarLogger()
    tmpCar2=Car(0,position,"car{}".format(i),maxVelocity=20, logger=fileLogger)
    fileLogger.initialize(tmpCar2)
    tmpCar2.setFrontCar(tmpCar1)
    cars.append(tmpCar2)
    clock.addListener(tmpCar2)
    tmpCar1=tmpCar2
    position += CONST_MinimumDistance + random.uniform(0,CONST_MaxNoise)
    
cars[0].frontCar=cars[-1]

for i in cars:
    print(i.name,i.frontCar.name,i.x )
    

def updateFrontCars():                              #Should be defined
    pass

updateFrontCars()
clock.start()