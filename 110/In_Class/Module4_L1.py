# Ryan Lin, CSC 110, 15 October 2019, Prof Ali
# Task 1
#

max_temp = 102.5

#Get the temp
temperature = float(input("Enter the substance's Celcius temperature:  "))

while temperature > max_temp:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait')
    print('5 minutes. Then take the temperature')
    print('again and enter it.')
    temperature = float(input('Enter the new Celcius temperature: '))
    print('The temperature is acceptable.')
    print('Check it again in 15 minutes.')


######################################################
# Task 2

max = 5

total = 0.0

print('This program calculates the total of')
print(max, 'numbers you will enter.')

for counter in range(max):
    number = int(input('Enter a number: '))
    total += number

print('The total is', total)

######################################################
# Task 3

for x in range(0, 1001, 10):
    print(x)

# Ryan Lin, CSC 110, 15 October 2019, Prof Ali
#Task 1
#
