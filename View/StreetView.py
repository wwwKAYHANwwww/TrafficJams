from ITimeDependent import ITimeDependent

class StreetView(ITimeDependent):
    
    def __init__(self,cars):
        self.cars=cars
    
    
    def update(self,time,timeStep):
        pass