from Model.Car import Car
from Model.Clock import Clock
from Factory.CarFactory import CarFactory
from Logger.DataFileCarLogger import DataFileCarLogger


clock=Clock(.005, 500)
carLogger=DataFileCarLogger()
carFactory=CarFactory(10,carLogger,clock)
carFactory.startBuilding()
clock.addListener(carLogger)
clock.start()
carLogger.finalize();