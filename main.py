from Model.Car import Car
from Model.Clock import Clock
from Factory.CarFactory import CarFactory
from Logger.DataFileCarLogger import DataFileCarLogger


clock=Clock(.005, 500)
carLogger=DataFileCarLogger()
carFactory=CarFactory(50,carLogger,clock)
carFactory.startBuilding()
clock.addListener(carLogger)
clock.start()
carFactory.setRandomBreak(100,1)
carLogger.finalize();