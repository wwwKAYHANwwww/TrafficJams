from ITimeDependent import ITimeDependent
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from Model.Car import Car
import numpy as np
from config import *

fig1 = plt.figure(figsize=(10,7))
gs = gridspec.GridSpec(4, 1)


for i in range(nsteps):
    if ((i*dt/pause>tmpN) & (tmpN < N)):     #if puase time elapsed add a car
        tmpCar = Car(t=t0+i*pause,
                     x0=0,
                     v0=v0[tmpN],
                     vf=vf[tmpN],
                     dm=dm,
                     carID=tmpN)
        cars[tmpN] = tmpCar
        tmpN = len(cars)

    for j in range(tmpN):                   # move all cars in each time step
        cars[j].move(dt,j,cars)
    Car.animate(i*dt,cars,gs)                      #create a frame of animation for each time step

#line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, l),
                                   #interval=50, blit=True)
plt.show()

class StreetView(ITimeDependent):

    def __init__(self,cars):
        self.cars=cars



    def update(self,time,timeStep):
        pass
