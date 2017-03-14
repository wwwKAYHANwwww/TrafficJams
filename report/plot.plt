set term png size 1200,800
set output "positions.png"

pl for[i=1:10] sprintf("car%d.dat",i) w l t sprintf("car %d",i)

set output "velocity.png"

pl for[i=1:10] sprintf("car%d.dat",i) u 1:3 w l t sprintf("car %d",i)
