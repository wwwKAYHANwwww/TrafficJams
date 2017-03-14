from Model.Car import Car
from Model.Clock import Clock
from Model.Config import Config
from Factory.CarFactory import CarFactory
from Logger.CriticalDensityCarLogger import CriticalDensityCarLogger

for i in range(0,20):
    CONST_MinimumDistance=i*3
    print(CONST_MinimumDistance)
    clock=Clock(.005, 500)
    carLogger=CriticalDensityCarLogger()
    carFactory=CarFactory(10,carLogger,clock)
    carFactory.startBuilding()
    carFactory.setRandomBreak(100,1)
    clock.addListener(carLogger)
    clock.start()
    carLogger.finalize()
    
