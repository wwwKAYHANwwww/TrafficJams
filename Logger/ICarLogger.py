import sys
sys.path.append("..") 

from Model.ITimeDependent import ITimeDependent
class ICarLogger(ITimeDependent):
    def __init__(self,car):
        self.car= car
    
    def initialize(self):
        pass
    
    def update(self,time,timeStep):
        pass
    
    def finalize(self):
        pass
    
