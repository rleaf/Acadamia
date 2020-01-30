# Ryan Lin, CSC 110, Prof Ali, 10/26/19
# Question 1
#

import random

def main():

    # MAC
    x = open('/Users/Ryan/Documents/GitHub/csc110/Assignments/random.txt', 'w')

    # WINDOWS
    # x = open('D:\Github\CSC110\Assignments/random.txt', 'w')

    y = int(input('How many random numbers do you want this file to hold? '))

    for z in range(y):
        i = str(random.randrange(1, 300))
        x.write(i + '\n')

    x.close()
main();

####################################################################################################
# Question 2

def main():

    # MAC
    x = open('/Users/Ryan/Documents/GitHub/csc110/Assignments/random.txt', 'r')
    h = open('/Users/Ryan/Documents/GitHub/csc110/Assignments/random.txt', 'r')

    # WINDOWS
    # x = open('D:\Github\CSC110\Assignments/random.txt', 'r')
    # h = open('D:\Github\CSC110\Assignments/random.txt', 'r')
    c = i = 0

    print(x.read())

    # Puts cursor back to beginning
    x.seek(0)

    for line in x:
        if line.strip():
            n = int(line)
            c += n
            i += 1
    print('The sum of these numbers is: ', c)
    print('The number of random numbers read from the file is: ', i)
    x.close()
main();
