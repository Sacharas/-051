
import turtle 
k = 20
turtle.left(90)
turtle.speed(5)
for i in range(4):  
    turtle.forward(10 * k)
    turtle.right(60)
    turtle.forward(10 * k)
    turtle.right(120)
turtle.up()

for x in range(-10, 15):
    for y in range(0, 20):
        turtle.goto(x * k, y * k)
        turtle.dot(3) 
turtle.done()



    
 

