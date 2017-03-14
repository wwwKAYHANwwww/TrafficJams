set terminal gif animate delay 10
set output "a.gif"


do for [i=1:100] {
	plot [0:8000][0:100] "animation.dat" u ($2):(20) i (i*1000-1) w p
}
