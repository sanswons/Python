import turtle

def design():
    window=turtle.Screen()
    window.bgcolor("red")
    tri=turtle.Turtle()
    tri.shape("arrow")
    tri.color("yellow")
    tri.speed(10)
    
    for i in range(1,75):
        j=0
        while(j<4):
            tri.forward(100)
            tri.right(90)
            j=j+1
        tri.right(5)
        
        
        
    window.exitonclick()


def draw_triangle():
    window=turtle.Screen()
    
    


design()
    
        
            
    
