# Ryan Lin , 9/24/19, CSC 110
#

test1 = float(input('Enter the first test score: '))
test2 = float(input('Enter the second test score: '))
test3 = float(input('Enter the third test score: '))

sum = test1 + test2 + test3
avg = sum/3

print('The sum of the score is ', sum)
print('The average of the score is ', avg)


# Task 1

import turtle

turtle.hideturtle()
turtle.fillcolor('#00ff00')
turtle.begin_fill()
turtle.goto(150, 0)
turtle.goto(150, 200)
turtle.goto(-150, 200)
turtle.goto(-150, 0)
turtle.goto(0, 0)
turtle.end_fill()

turtle.penup()
turtle.hideturtle()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.goto(0,20)
turtle.circle(75)
turtle.end_fill()

turtle.exitonclick()

# EXTRA CREDITTTT

# Download .csv file
# Install pandas module
# Copy a couple columns into another csv file
# 2 / 3 weeks
# this is extra credit
