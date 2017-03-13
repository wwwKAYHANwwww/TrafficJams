from ICarLogger import ICarLogger

class DataFileCarLogger(ICarLogger):
    def __init__(self,car):
        self.car=car
        self.file=open("report/{}.dat".format(car.name),"a")
        
    def log(self,time):
        file.write("{}     {}\n".format(time,self.car.x))
    