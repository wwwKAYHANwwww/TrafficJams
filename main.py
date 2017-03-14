from Model.Car import Car
from Model.Clock import Clock
from Factory.CarFactory import CarFactory
from Factory.DataFileCarLoggerFactory import DataFileCarLoggerFactory


clock=Clock(.01, 1000)
fileLoggerFactory=DataFileCarLoggerFactory()
carFactory=CarFactory(10,fileLoggerFactory,clock)
carFactory.startBuilding()


clock.start()