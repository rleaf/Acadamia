# Ryan Lin, CSC 110, Prof Ali, 10/21/19
# Assignment 5
#

def main():

    def instructions():
        print('This program reads race time in minutes and seconds for a runner.')
        print('It then computes and prints the speed in feet/second and meters/second.')


    def feetPerSecond(min, sec):
        _fps = (5280 / ((min * 60) + sec))
        return _fps
        # print('feet/sec')
        # print('')
        # print('{:.2f}'.format(fps))

    def metersPerSecond(min, sec):
        _mps = 1609.34 / ((min * 60) + sec)
        return _mps
        # print('meters/second')
        # print('')
        # print('{:.2f}'.format(mps))



    instructions();


    for i in range(1, 5):
        x = input("Press 'Y' or 'y' to continue, anything else to exit: ")

        while x == 'y' or x == 'Y':
            name = input('Enter first name: ')
            min = int(input('Enter minutes: '))
            sec = float(input('Enter seconds: '))

            fps = feetPerSecond(min, sec);
            mps = metersPerSecond(min, sec);

            print(' ')
            print('{:^10}'.format('feet/sec'), ' '.center(10), '{:^10}'.format('meters/sec'))
            print()
            print('{:^10,.2f}'.format(fps), '     ', '{:^20,.2f}'.format(mps))

            x = input("Press 'Y' or 'y' to continue, anything else to exit: ")
        else:
            break;




main();


# def no_return(x,y):
#     c = x + y
#     return c
#
# res = no_return(4,5)
# print(res)



# Ryan Lin, CSC 110, Prof Ali, 10/21/19
# Assignment 5
#

# import sys
#
# def main():
#
#     def instructions():
#         print('This program reads race time in minutes and seconds for a runner.')
#         print('It then computes and prints the speed in feet/second and meters/second.')
#         x = input("Press 'Y' or 'y' to continue, anything else to exit: ")
#
#         # if x == 'y' or x == 'Y':
#         #     return
#         # else:
#         #     sys.exit()
#
#         while x == 'y' or x == 'Y':
#             break
#         else:
#             sys.exit()
#
#     instructions();
#
#     name = input('Enter first name:')
#     min = int(input('Enter minutes: '))
#     sec = float(input('Enter seconds: '))
#
#     def feetPerSecond():
#         fps = 5280 / ((min * 60) + sec)
#         print('feet/sec')
#         print('')
#         print('{:.2f}'.format(fps))
#
#     def metersPerSecond():
#         mps = 1609.34 / ((min * 60) + sec)
#         print('meters/second')
#         print('')
#         print('{:.2f}'.format(mps))
#
#     # print('feet/sec     meters/sec')
#     # print()
#     # print('{:.2f}'.format(fps), '     ', '{:.2f}'.format(mps))
#
#
#
#
#     feetPerSecond();
#     metersPerSecond();
#
#
#
# main();
#
#
# #
# # x = 'y' or x == 'Y'
# # while x == 'y' or x == 'Y':
# #     print('toads')
# #     x = input()
