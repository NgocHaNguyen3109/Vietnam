import turtle

flag_height = 400 
flag_width = 1.5 * flag_height 


screen = turtle.Screen()
screen.title("Đồng bào Việt Nam yêu nước")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(3)  
t.hideturtle()
t.pensize(1)

def yellow_star(t, center_x, center_y, side):
    t.penup()
    t.goto(center_x, center_y + side)  
    t.setheading(-72)  
    t.pendown()
    t.fillcolor('#FFFF00')
    t.pencolor('#FFFF00')  
    t.begin_fill()
    
    for i in range(5):
        t.forward(side) 
        t.left(72) 
        t.forward(side)  
        t.right(144) 
    t.end_fill()


t.color("#da251d")
t.penup()
t.goto(-flag_width // 2, flag_height // 2)
t.pendown()
t.begin_fill()
for _ in range(2):
    t.forward(flag_width)
    t.right(90)
    t.forward(flag_height)
    t.right(90)
t.end_fill()


star_radius = flag_width * 0.15 
yellow_star(t, 0, 30, star_radius)

screen.exitonclick()
screen.mainloop()
