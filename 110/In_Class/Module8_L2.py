# Ryan Lin, CSC 110, Prof Ali, 11/14/19, Mod 8 Lab 2
# Task 01
#

def main():
    values = 'one$two$three$four'
    newValues = values.split('$')

    print(newValues);
main();

##############################################################################
# Task 02

import calendar as c

def main():

    # I doubt this is how he wanted, it.

    x = input('Enter the date in mm/dd/yyyy syntax: ')
    y = x.split('/')

    # print(y[0])
    print(c.month_name[int(y[0])], y[1], y[2])

main();



def main():

    x = input('Enter the date in mm/dd/yyyy syntax: ')
    y = x.split('/')

    sample_list = values.split('/')
    print(sample_list[1])
    if int(sample_list[1]) == 1:
        print('January', end = '')


main();
##############################################################################
# Task 03

def main():

    x = {'a':1, 'b':2, 'c':3}
    print(x)

main();

##############################################################################
# Task 04

def main():

    dct = {'Jim':1, 'Ryan':2, 'Jared':3, 'Leo':4}

    if 'Jim' in dct:
        del dct['Jim']
    print(dct)
main();







x = {'a':'1', 'b':'2', 'c':'3'}
print(x[1])

stuff = {1:'aaa', 2:'bbb', 3:'ccc'}
print(stuff[3])
