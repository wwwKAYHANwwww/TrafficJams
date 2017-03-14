from ICarLogger import ICarLogger
from Model.Config import Config

class CriticalDensityCarLogger(ICarLogger):
    def __init__(self,cars=None):
        self.cars=cars
        self.avgMean=0
        self.avgSquareMean=0
        #self.file=open("report/variance.dat","w")
        #self.file2=open("report/variance2.dat","w")
        
    def initialize(self,cars):
        self.cars=cars
        self.file=open("report/variance.dat","a")
        #self.file2=open("report/variance2.dat","a")
        
    def update(self,time,timeStep):
        mean=0.0
        for i in range(len(self.cars)-1):
            mean+=self.cars[i].v
        mean=mean/(len(self.cars)-1)
        
        self.avgMean+=mean/20000
        #self.file.write("{}    {}\n".format(time,mean))
        
    def finalize(self,dens):
        self.file.write("{}    {}\n".format(dens, 1-self.avgMean/25))
        self.file.close()