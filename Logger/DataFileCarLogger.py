from ICarLogger import ICarLogger

class DataFileCarLogger(ICarLogger):
    def __init__(self,car=None):
        self.car=car
        self.file=None
        
    def initialize(self,car):
        self.car=car
        self.file=open("report/{}.dat".format(car.name),"a")
        
        
    def log(self,time):
        self.file.write("{}    {}    {}    {}\n".format(time,self.car.x,self.car.v,self.car.acceleration))
    