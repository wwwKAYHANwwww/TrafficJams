from Model.Car import Car
from Model.Clock import Clock
from Model.Config import Config
from Factory.CarFactory import CarFactory
from Logger.CriticalDensityCarLogger import CriticalDensityCarLogger
from numpy import double

for i in range(1000,5000,100):
#i=500
    Config.CONST_MinimumDistance=Config.CONST_LengthOfRoad/i
    print(i,Config.CONST_MinimumDistance)
    clock=Clock(.05, 1000)
    carLogger=CriticalDensityCarLogger()
    carFactory=CarFactory(i,carLogger,clock)
    carFactory.startBuilding(Config.CONST_LengthOfRoad/i)
    carFactory.setRandomBreak(0.1,0.5)
    clock.addListener(carLogger)
    clock.start()
    carLogger.finalize(double(i)/Config.CONST_LengthOfRoad)

