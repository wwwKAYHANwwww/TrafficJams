set term png size 1200,800
set output "variance.png"

set ylabel "X Position" 
set xlabel "Time" 
set title "Position of cars in each time"
pl [0:300][] for[d=0:5] "variance.dat" index d w l t sprintf("%d",d*5)
