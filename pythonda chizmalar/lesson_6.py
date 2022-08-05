from turtle import *
import colorsys as cs

speed(0)
bgcolor('black')
h=0.1       
for i in range(350):
    c=cs.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.001
    fd(i*20/15)
    rt(1500)

done()