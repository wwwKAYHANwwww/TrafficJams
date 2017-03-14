set terminal gif animate delay 10
set output "a.gif"


do for [i=1:100] {
	plot [][0:5000] "animation.dat"  i (i*1000-1) w p
}
