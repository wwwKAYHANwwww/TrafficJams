set term png size 1200,800
set output "positions.png"

numOfCars=50

set ylabel "X Position" 
set xlabel "Time" 
set title "Position of cars in each time"
pl for[i=1:numOfCars] sprintf("car%d.dat",i) w l t sprintf("car %d",i)

set output "velocity.png"
set ylabel "Velocity" 
set xlabel "Time" 
set title "Velocity of cars in each time"
pl for[i=1:numOfCars] sprintf("car%d.dat",i) u 1:3 w l t sprintf("car %d",i)
