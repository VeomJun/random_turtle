import turtle as t
import random

t.speed(1)
t.shape('turtle')
t.width(10)
while True:
   if random.randint(0,2) == 0:
      t.forward(50)
      t.rt(90)
      t.begin_fill()
      t.color('red')
      t.end_fill()
   elif random.randint(0,2) == 1:
      t.forward(50)
      t.lt(90)
      t.begin_fill()
      t.color('blue')
      t.end_fill()
   else:
      t.fd(5)
t.done()