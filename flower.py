import turtle

def design():
    window=turtle.Screen()
    window.bgcolor("red")
    flower=turtle.Turtle()
    flower.shape("circle")
    flower.color("yellow")
    flower.speed(10)

    for i in range(1,37):
        j=0
        while(j<2):
            flower.forward(70)
            flower.right(50)
            flower.forward(70)
            flower.right(130)
            j=j+1
        flower.right(10)
            
    flower.right(90)
    flower.forward(300)
    
    window.exitonclick()



design()
