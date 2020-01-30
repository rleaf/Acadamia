# Ryan Lin, CSC 110, Prof Ali, 11/1/19
# assignment 07
#

import random as r

def main():

    # WINDOWS
    x = open('D:\Github\CSC110\Assignments\lin_assignment07\lottery.txt', 'w')

    #MAC
    # x = open('/Users/Ryan/Documents/GitHub/csc110/Assignments/lin_assignment07/lottery.txt', 'w')
    number = []

    for i in range(0,6):
        randomNumber = r.randrange(0,10)
        number.append(randomNumber)
        # number[i] = randomNumber

    for item in number:
        # x.write('%s\n' % item)
        x.write('{0!s}\n'.format(item))

    print(number)

    x.close();
main();
