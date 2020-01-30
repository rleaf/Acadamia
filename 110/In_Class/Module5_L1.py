# # Ryan Lin, CSC 110, Prof Ali, 10/19/2019
# # Task 2
# #
#
# def main():
#     x = int(input('Enter a number in kilometers: '))
#     print('This formula converts kilometers to miles.')
#
#     def kilometerConveter(y):
#         y *= 0.6214
#         print(x, 'miles is', '{:.2f}'.format(y), 'kilometers.')
#
#
#     kilometerConveter(x);
#
# main()
#
#


def main():
    x = int(input('Enter a number in kilometers: '))
    print('This function / formula will convert to miles.')

    def kilometerConverter(y):
        y *= 0.6214
        print(x, 'miles is', '{:.2f}'.format(y), 'kilometers.')

    kilometerConverter(x);

main()




x = int(input('Enter a number in kilometers: '))

def main():
    print('This formula will convert miles to kilometers')
    kilometerConverter(x)

def kilometerConverter(y):
    y *= 0.6214
    print(x, 'miles is', '{:.2f}'.format(y), 'kilometers.')


main()
