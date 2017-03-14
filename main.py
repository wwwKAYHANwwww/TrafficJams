from Model.Car import Car
from Model.Clock import Clock
import random
from Logger.DataFileCarLogger import DataFileCarLogger

CONST_MinimumDistance = 50
CONST_MaxPositionNoise = 20
CONST_MaxVelocityNoise = 5
CONST_LengthOfRoad=1000

clock=Clock(.01, 100)
cars=[]
position = 0.
fileLogger=DataFileCarLogger()
tmpCar1=Car(0,position,"car1", maxVelocity=25+random.uniform(-CONST_MaxVelocityNoise, CONST_MaxVelocityNoise), logger=fileLogger)
fileLogger.initialize(tmpCar1)
clock.addListener(tmpCar1)
cars.append(tmpCar1)


position += CONST_MinimumDistance*2 + random.uniform(0,CONST_MaxPositionNoise)
for i in range(2,10):
    fileLogger=DataFileCarLogger()
    tmpCar2=Car(0,position,"car{}".format(i),maxVelocity=20+random.uniform(-CONST_MaxVelocityNoise, CONST_MaxVelocityNoise), logger=fileLogger)
    fileLogger.initialize(tmpCar2)
    tmpCar1.setFrontCar(tmpCar2)
    cars.append(tmpCar2)
    clock.addListener(tmpCar2)
    tmpCar1=tmpCar2
    position += CONST_MinimumDistance*2 + random.uniform(0,CONST_MaxPositionNoise)
    
cars[-1].frontCar=cars[0]

for i in cars:
    print(i.name,i.frontCar.name,i.x )

clock.start()