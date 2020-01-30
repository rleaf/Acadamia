# Ryan Lin, CSC 110, Prof Ali, Dec 5 2019
# Problem A | Turing Machine
#

# Power of 2 ------ 2 4 8 16 32 64

def main():

    x = int(input('Enter an integer less than 1000: '))
    y = x * '0'
    z = 2

    def orig(z):

        if z < 1000:
            while z < 1000:
                for i in range(1000):
                    print(z**i)


    print(x, 'Accepted')


    for i in range(x):
        aa = (y[i] * (i + 1))

        if len(aa) == range(z**z):
            bb = 'Accepted'
        else:
            bb = 'Rejected'


        # print(aa, bb)


    # print(z**z)
    orig(2)
main();
