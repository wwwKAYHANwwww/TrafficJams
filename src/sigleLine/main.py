import matplotlib.pyplot as plt

from module import Car,plottingTX,animate


cars={}
tmpCarNumbers = 0
maxCarNumber = 5
t0 = 0
timeStep = 0.1
tFinal = 100
nsteps = int(tFinal / timeStep)
intervalAddingCar = 20.*timeStep

plt.figure(figsize=(15,10))

for i in range(nsteps):
    if ((i*timeStep/intervalAddingCar > tmpCarNumbers) & (tmpCarNumbers <= maxCarNumber)):
        tmpCar = Car(t=t0 + i*20,x0=0,v0=10,targetVelocity=20,carID=tmpCarNumbers+1 )
        #cars[tmpCarNumbers] = {'x':tmpCar.x,'v':tmpCar.v}
        cars[tmpCarNumbers] = tmpCar
        tmpCarNumbers = len(cars)
        
    for j in range(tmpCarNumbers):
        cars[j].move(timeStep,j,cars)
    #animate(i*timeStep,cars)
    plottingTX(i*timeStep,cars)