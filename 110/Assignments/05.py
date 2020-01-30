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

    # for i in range(1, 5):
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
        # else:
        #     break;

main();
