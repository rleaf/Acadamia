# Test 1 Lab, Ryan Lin, CSC 110, Prof Ali, 10/8/19
#

hours = int(input('Enter hour: '))

if hours >= 1 and hours <= 11:
    print(hours, 'AM')

elif hours == 12:
    print(hours, 'PM')

elif hours >= 13 and hours <= 23:
    print(hours - 12, 'PM')

elif hours == 24:
    print(hours - 12, 'AM')

else:
    print('You have entered an invalid value')
