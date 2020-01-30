# Ryan Lin , CSC 110, 10/1/19
# Task 1

base_hours = 40
ot_multiplier = 1.5

hours = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))


if hours > base_hours:

    overtime_hours = hours - base_hours
    overtime_pay = overtime_hours * pay_rate * ot_multiplier
    gross_pay = base_hours * pay_rate + overtime_pay

else:

    gross_pay = hours * pay_rate

if gross_pay > 100:
    net_pay = gross_pay - 15

print('The gross pay is $', format(gross_pay, ',.2f'), sep='')
print('The net pay is $', format(net_pay,',.2f'))


# Task 2
base_hours = 40
ot_multiplier = 1.5

hours = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))


if hours > base_hours:

    overtime_hours = hours - base_hours
    overtime_pay = overtime_hours * pay_rate * ot_multiplier
    gross_pay = base_hours * pay_rate + overtime_pay

else:

    gross_pay = hours * pay_rate

medicareCost = gross_pay * .029
socialSecurityCost = gross_pay * .124

if gross_pay > 100:
    net_pay = ((gross_pay - medicareCost) - socialSecurityCost - 15)

print('The gross pay is $', format(gross_pay, ',.2f'), sep='')
print('The net pay is $', format(net_pay,',.2f'))


# Task 3

x = int(input('Give me an integer'))

if x % 2 == 0:
    print('Even number')

else:
    print('Odd Number')



####################################

elif x % 2 != 0:
    print('Odd number')

else:
    print('Whole number pls')

elif x != int:
    print('fake')
