from ICarLogger import ICarLogger

class DataFileCarLogger(ICarLogger):
    def __init__(self,cars=None):
        self.cars=cars
        self.file=[]
        
    def initialize(self,cars):
        self.cars=cars
        for i in range(len(self.cars)):
            self.file.append(open("report/{}.dat".format(cars[i].name),"w"))
        
    def update(self,time,timeStep):
       
        for i in range(len(self.cars)):
            self.file[i].write("{}    {}    {}    {}\n".format(time,self.cars[i].x,self.cars[i].v,self.cars[i].acceleration))
    
    def finalize(self):
        for i in range(len(self.cars)):
            self.file[i].close()
    