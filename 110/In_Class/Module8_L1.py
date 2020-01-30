# Ryan Lin, CSC 110, Prof Ali, November 12 2019
# Task 1
#

def main():

    x = input('Enter your first name: ')
    y = input('Enter your middle name: ')
    z = input('Enter your last name: ')

    print(x[0], y[0], z[0])

main();


def main():
    # Extra credit if all the text is lowercase
    x = input('Enter your name, first characters should be upper case:').split()

    # Comprehends only uppercase text
    # for i in x:
    #     print(i)
    #     if i.isupper():
    #         print(i+'.', end='');


    # Comprehends lower and uppercase text
    for word in x:
        y = word[0].upper()
        print(y + '.' , end = '')


    # List comprehension syntax, same code as above.
    # [print(word[0] + '.' , end = '') for word in x]
main();


######################################################################
# Task 2


def main():

    x = input('Enter single-digit numbers with no seperators:')
    # y = [int(i) for i in x]
    # print(sum(y))
    total = 0
    for i in x:

        total += int(i);
    print(total)

main();
