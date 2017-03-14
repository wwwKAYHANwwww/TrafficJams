from ICarLogger import ICarLogger
from Model.Config import Config

class CriticalDensityCarLogger(ICarLogger):
    def __init__(self,cars=None):
        self.cars=cars
        self.file=None
        
    def initialize(self,cars):
        self.cars=cars
        self.file=open("report/variance.dat","a")
        
    def update(self,time,timeStep):
        mean=0
        squareMean=0
        for i in range(len(self.cars)-1):
            mean+=self.cars[i].distanceToFrontCar()
            squareMean+=self.cars[i].distanceToFrontCar()**2
        mean=mean/(len(self.cars)-1)
        squareMean=squareMean/(len(self.cars)-1)
        self.file.write("{}    {}\n".format(time,squareMean-mean**2))
    
    def finalize(self):
        self.file.write("\n\n")
        self.file.close()
        