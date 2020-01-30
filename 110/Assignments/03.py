# Ryan Lin, October 3, 2019, CSC 110, Prof Ali
#
import sys

roomNumber = int(input('Enter room number: '))
capacity = int(input('Enter capacity: '))
enrollment = int(input('Enter enrollment: '))
#
# roomNumber = 345
# capacity = 32
# enrollment = 23

if roomNumber < 0 or capacity < 0 or enrollment < 0:
    print('Error! Capacity cannot be a negative number.')
    sys.exit()

if enrollment > capacity:
    print('Error! Enrollment can not be greater than capacity')
    sys.exit()

emptySeats = capacity - enrollment

if enrollment == capacity:
    filled = 'Filled'
else:
    filled = 'Not filled'

print('{:^15} {:^15} {:^15} {:^15} {:^15}'.format('Room',    'Capacity',    'Enrollment',    'Empty Seats',    'Filled/Not filled'))
print('{:^15} {:^15} {:^15} {:^15} {:^15}'.format('----', '--------', '----------', '-----------', '-----------------'))
print('{:^15} {:^15} {:^15} {:^15} {:^15}'.format(roomNumber, capacity, enrollment, emptySeats, filled))
