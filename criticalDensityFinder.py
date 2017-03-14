from Model.Car import Car
from Model.Clock import Clock
from Model.Config import Config
from Factory.CarFactory import CarFactory
from Logger.CriticalDensityCarLogger import CriticalDensityCarLogger

for i in range(50,5000,200):
#i=500
    Config.CONST_MinimumDistance=Config.CONST_LengthOfRoad/i
    print(i,Config.CONST_MinimumDistance)
    clock=Clock(.05, 1000)
    carLogger=CriticalDensityCarLogger()
    carFactory=CarFactory(i,carLogger,clock)
    carFactory.startBuilding()
    carFactory.setRandomBreak(1,0.7)
    clock.addListener(carLogger)
    clock.start()
    carLogger.finalize()

