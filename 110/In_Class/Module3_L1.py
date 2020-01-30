# Ryan Lin , CSC 110, 9/24/19
#
# Task 1
x = float(input('Number: '))

if x > 100:
    y = 20
    z = 40
    print(y,z)




# Task 2
a = 1

if a < 10:
    b = 20
else:
    b = 99



# Task 3

x = int(input('Enter your first number: '))
y = int(input('Enter your second number: '))

if y<=0:
    print('Division by zero is not possible. Please run the program again and enter a number other than zero.')
else:
    print('The quotient of', x, 'divided by', y, 'is: ', x/y)


##################### Extra

# x = float(245.334)
# print('The quotient of {} is '.format(10/3, '.2f'))
#
#
# print(format(20/3, '.3f'))



####

4:30 October 1. Science building meet professor


print('Room   Capacity   Test')
print('----   --------   ----')

n = 10
x = 1

while x<=n:
    sum = sum + x
    x = x + 1
print(sum)
