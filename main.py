from Car import Car
from Clock import Clock

c1=Car(10,15,20,None)
c2=Car(5,16,30,c1)
c3=Car(5,16,30,c2)

clock=Clock(.5, 2.)
clock.addListener(c1)
clock.addListener(c2)
clock.addListener(c3)

clock.start()