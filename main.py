from Car import Car
from Clock import Clock

Const_MinimumDistance = 30
cars=[]
tmpCar1=Car(10,15,20,"car1")
cars.append(tmpCar1)

clock=Clock(.1, 20)

for i in range(2,10):
    tmpCar2=Car(10,15,"car{}".format(i),maxVelocity=20)
    tmpCar2.setFrontCar(tmpCar1)
    cars.append(tmpCar2)
    clock.addListener(tmpCar2)
    tmpCar1=tmpCar2
    
cars[0].frontCar=cars[-1]

for i in cars:
    print(i.name,i.frontCar.name)

def updateFrontCars():                              #Should be defined
    pass

updateFrontCars()
clock.start()