import math
from turtle import *

penup()
setpos(0,150)
pendown()
color("red", "yellow")
pensize(8)
begin_fill()

t = 7

for i in range(t+1):
    goto(math.sin((360/t)*i*math.pi/180)*150, math.cos((360/t)*i*math.pi/180)*150)
end_fill()
done()