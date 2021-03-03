from p5 import *

WIDTH=500
HEIGHT=500
RIGHT=WIDTH/2
LEFT=-RIGHT
DOWN=HEIGHT/2
UP=-DOWN

def mandelbrot(c):
	z=0
	n=0
	max_iter=100
	while(abs(z)<=2 and n < max_iter):
		z = z*z + c
		n+=1

	if(abs(z)<=2):
		return True
	else:
		return False

def _map(n, start1, stop1, start2, stop2):
	return ((n-start1)/(stop1-start1))*(stop2-start2)+start2
		
def setup():
	size(WIDTH,HEIGHT)
	no_stroke()
	background(204)
	no_loop()
def draw():
	x=LEFT
	while(x<RIGHT):
		y=UP
		while(y<DOWN):
			x_=_map(x,LEFT,RIGHT,-2,2)
			y_=_map(y,UP,DOWN,-2,2)
			m=mandelbrot(complex(x_,y_))
			
			if(m):
				fill(0)
				circle(( int(_map(x_,-2,2,0,WIDTH)) , int(_map(y_,-2,2,0,HEIGHT)) ),2)
			y+=1
		x+=1
	print("Done frame")

run()
#print(mandelbrot(0.26))
