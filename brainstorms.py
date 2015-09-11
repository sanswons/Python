import turtle

def draw_square():
    window=turtle.Screen()
    window.bgcolor("red")
    
    brad=turtle.Turtle()
    brad.shape("square")
    brad.color("pink")
    brad.speed(2)
    
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

def draw_circle():
    window=turtle.Screen()
    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)
    angie.speed(2)

def draw_triangle():
    window=turtle.Screen()
    tri=turtle.Turtle()
    tri.shape("arrow")
    tri.right(120)
    tri.forward(200)
    tri.right(120)
    tri.forward(200)
    tri.right(120)
    tri.forward(200)
    window.exitonclick()

    

draw_square()
draw_circle()
draw_triangle()
