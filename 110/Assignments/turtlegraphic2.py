# Ryan Lin | CSC 101 | 9/18/19
# Updated 9/24/19

import turtle

t = turtle.Turtle()
t.hideturtle()
t.begin_fill()
t.penup()

t.goto(300, 0)
t.goto(300, 130)
t.goto(130, 130)
t.goto(130, 260)
t.goto(0, 260)
t.goto(0, 0)


# t.goto(300, 0)
# t.goto(300,200)
# t.goto(0, 200)
# t.goto(0, 0)
t.fillcolor('#4b99e0')
t.end_fill()

turtle.exitonclick()
