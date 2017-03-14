from ICarLogger import ICarLogger
from Model.Config import Config

class CriticalDensityCarLogger(ICarLogger):
    def __init__(self,cars=None):
        self.cars=cars
        self.file=None
        self.file2=None
        self.avgMean=0
        self.avgSquareMean=0
        
    def initialize(self,cars):
        self.cars=cars
        self.file=open("report/variance.dat","a")
        self.file2=open("report/variance2.dat","a")
        
    def update(self,time,timeStep):
        mean=0.0
        squareMean=0.0
        for i in range(len(self.cars)-1):
            mean+=self.cars[i].distanceToFrontCar()
            squareMean+=self.cars[i].distanceToFrontCar()**2
        mean=mean/(len(self.cars)-1)
        squareMean=squareMean/(len(self.cars)-1)
        self.avgMean+=mean/5000
        self.avgSquareMean+=(mean**2)
        self.file.write("{}    {}\n".format(time,squareMean-mean**2))
    
    def finalize(self):
        self.file.write("\n\n")
        self.file2.write("{}\n".format(self.avgSquareMean-self.avgMean**2))
        self.file.close()
        