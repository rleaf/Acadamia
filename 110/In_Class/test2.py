# Ryan Lin, redo, better code and understanding of test2
# declare 3 functions: main, instruction, and prime_funciton



def main():



    def instruction():
        print('This program asks the user for an integer and verifies whether it is prime or not')

    instruction();

    x = input('Enter y or Y to continue');

    while x == 'y' or x == 'Y':

        y = int(input('Enter an integer:'))

        def prime_function(x):
            r = 0;
            for i in range(2, x):
                # print(i)
                if x % i == 0 and r == 0:
                    # print('beepboop')
                    r = 1;
                    print(x, 'is not a prime number');

                elif x % i != 0 and r == 0:
                    r = 1;

                    print(x, 'is a prime number');

# It is only determining if the input is divisible by 2, not the following
# numbers in the for loop. This is not what a prime number is.

        prime_function(y)

        x = input('Enter y or Y to continue');
main();


#
# x = 0;
# for i in range(6):
#     print(i)
#     if i == i and x == 0:
#         print('toads');
#         x += 1;
