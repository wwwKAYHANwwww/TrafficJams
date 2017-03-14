from Model.Car import Car
from Model.Clock import Clock
from Model.CarFactory import CarFactory

from Logger.DataFileCarLogger import DataFileCarLogger


clock=Clock(.01, 100)
fileLogger=DataFileCarLogger()
carFactory=CarFactory(10,fileLogger,clock)
carFactory.startBuilding()


clock.start()