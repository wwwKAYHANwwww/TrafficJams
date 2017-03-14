from ICarLogger import ICarLogger

class AnimationCarLogger(ICarLogger):
    def __init__(self,cars=None):
        self.cars=cars
        self.file=[]
        
    def initialize(self,cars):
        self.cars=cars
        self.file=open("report/animation.dat","w")
        
    def update(self,time,timeStep):
       
        for i in range(len(self.cars)):
            self.file.write("{}    {}    {}    {}\n".format(i,self.cars[i].x,self.cars[i].v,time))
            
        self.file.write("\n\n")
    def finalize(self):
        self.file.close()
    