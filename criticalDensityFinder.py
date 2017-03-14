from Model.Car import Car
from Model.Clock import Clock
from Model.Config import Config
from Factory.CarFactory import CarFactory
from Logger.CriticalDensityCarLogger import CriticalDensityCarLogger

for i in range(3,20):
    Config.CONST_MinimumDistance=Config.CONST_LengthOfRoad/i
    print(i,Config.CONST_MinimumDistance)
    clock=Clock(.005, 250)
    carLogger=CriticalDensityCarLogger()
    carFactory=CarFactory(i,carLogger,clock)
    carFactory.startBuilding()
    carFactory.setRandomBreak(100,1)
    clock.addListener(carLogger)
    clock.start()
    carLogger.finalize()
    
