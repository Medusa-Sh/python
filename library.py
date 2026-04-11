import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()

num_size=6
side_length=70
angle=360.0/num_size
for i in range(num_size):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()