from Car import Car
from Clock import Clock

# creating empty list of cars, assign them to temCar1 variable
cars=[]
tmpCar1=Car(10,15,20,"car1")
# appeing the temCar1 to cars
cars.append(tmpCar1)

clock=Clock(.1, 20)

# line od code that generate car, assign them to tempCar2, appends to cars variable
for i in range(2,10):
    tmpCar2=Car(10,15,20,"car{}".format(i))
    tmpCar2.setFrontCar(tmpCar1)
    cars.append(tmpCar2)
    clock.addListener(tmpCar2)
    tmpCar1=tmpCar2
    
# accessing the cars using indexing
cars[0].frontCar=cars[-1]

# looping through to get names of cars
for i in cars:
    print(i.name,i.frontCar.name)

# updatine the frontCars
def updateFrontCars():                              #Should be defined
    pass

updateFrontCars()
clock.start()
