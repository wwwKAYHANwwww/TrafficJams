from ITimeDependent import ITimeDependent

class Car(ITimeDependent):
    def __init__(self,v0,x0,targetVelocity,name,frontCar): #Constractor of the class
        self.v0=v0                                         #Initial Velocity
        self.x0=x0                                         #Initial Position
        self.x=0                                           #Starting Point     ???
        self.v=0                                           #Statrting Velocity ???
        self.targetVelocity= targetVelocity                #TargetVelocity
        self.frontCar=frontCar;                            #The Car in Front of me (Should be Updated Once)
        self.acceleration=0                                #
        self.name=name
        self.positiveA=0.5
        self.negativeA=-1.
        self.criticalDistance=10
        
    def setFrontCar(self,frontCar):
        self.frontCar=frontCar
        
    def update(self, time,timeStep):
        distance=(self.frontCar.x - self.x)
        self.acceleration = self.positiveA if distance>self.criticalDistance else self.negativeA
        
        if (self.v<self.targetVelocity) and (self.v>=0):
            self.v+=self.acceleration * timeStep
            
        self.x+= self.v * timeStep
        file=open("report/{}.dat".format(self.name),"a")
        file.write("{}     {}\n".format(time,self.x))
        file.close()
        
        
    
    