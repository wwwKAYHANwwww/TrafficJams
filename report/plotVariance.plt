set term png size 1200,800
set output "variance.png"

set ylabel "Variance " 
set xlabel "Time" 
set title "Variance of cars in each time"
pl [0:300][] for[d=0:5] "variance.dat" index d w l t sprintf("%d",d*5)
