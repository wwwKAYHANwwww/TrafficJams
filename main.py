from Car import Car
from Clock import Clock
import random
from Logger.DataFileCarLogger import DataFileCarLogger

CONST_MinimumDistance = 10
CONST_MaxPositionNoise = 1
CONST_MaxVelocityNoise = 5
CONST_LengthOfRoad=1000

clock=Clock(.1, 20)
cars=[]
position = 0.
fileLogger=DataFileCarLogger()
tmpCar1=Car(0,position,"car1", maxVelocity=25+random.uniform(-CONST_MaxVelocityNoise, CONST_MaxVelocityNoise), logger=fileLogger)
fileLogger.initialize(tmpCar1)
clock.addListener(tmpCar1)
cars.append(tmpCar1)


position += CONST_MinimumDistance + random.uniform(0,CONST_MaxPositionNoise)
for i in range(2,10):
    fileLogger=DataFileCarLogger()
    tmpCar2=Car(0,position,"car{}".format(i),maxVelocity=20+random.uniform(-CONST_MaxVelocityNoise, CONST_MaxVelocityNoise), logger=fileLogger)
    fileLogger.initialize(tmpCar2)
    tmpCar2.setFrontCar(tmpCar1)
    cars.append(tmpCar2)
    clock.addListener(tmpCar2)
    tmpCar1=tmpCar2
    position += CONST_MinimumDistance + random.uniform(0,CONST_MaxPositionNoise)
    
cars[0].frontCar=cars[-1]

for i in cars:
    print(i.name,i.frontCar.name,i.x )

clock.start()