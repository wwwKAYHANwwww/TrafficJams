import matplotlib.pyplot as plt
from module import Car,plottingTX,animate
import numpy as np

maxCarNumbers = 5
np.random.seed(123)
t0 = 0
timeStep = 0.1
tFinal = 100
intervalAddingCar = 20.*timeStep
targetVelocity = 20
