# Ryan Lin, Prof Ali, Nov 18, 2019, Assignment 08
# Task 01
#

def main():

    x = open('/Users/Ryan/Documents/GitHub/csc110/Assignments/lin_assignment08/test.txt', 'r')
    a = b = c = d = e = f = 0

    y = x.read()
    g = y.split()
    # print(g)

    for z in g:
        # print(z)
        if z[0].isupper():
            a += 1;
        elif z.islower():
            b += 1;

        # Can't use 'elif' here because prior conditions are already met for elements in the list such as '650-horsepower', which is lowercase
        if z[0].isdigit():
            c += 1;
            # print(z)


    d = len(g)

    print('There are', a ,'words in uppercase')
    print('There are', b ,'words in lowercase')
    print('There are', c ,'numbers')
    print('There are', d ,'spaces')

main();
#
# a = 0
# x = ['four', '650-horsepower', 'ships', 'at']
# for i in x:
#
#     if z.islower():
#         print('toads')
#
#     elif i[0].isdigit():
#         a += 1
#         print(i)
        # print(a)
    # print(i)

###########################################################################################
# Task 02
#

def main():

    roomNumber = {'CS101':'3004', 'CS102':'4501', 'CS103':'6755', 'NT110':'1244', 'CM241':'1411'}
    instructor = {'CS101':'Haynes', 'CS102':'Alvarodo', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}
    meetingTime = {'CS101':'8:00am', 'CS102':'9:00am', 'CS103':'10:00am', 'NT110':'11:00am', 'CM241':'1:00pm'}

    a = input('Enter a course number (key): ')

    def userInput(a):

        print('You are meeting in room', roomNumber[a], 'with instructor', instructor[a], 'at', meetingTime[a])

    userInput(a)
main();
