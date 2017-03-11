from ITimeDependent import ITimeDependent

class Car(ITimeDependent):
    def __init__(self,v0,x0,targetVelocity,frontCar):
        self.v0=v0
        self.x0=x0
        self.targetVelocity= targetVelocity
        self.fronCar=frontCar
        
    def update(self, time):
        print(time)
    