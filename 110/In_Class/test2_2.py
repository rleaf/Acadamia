# Ryan Lin, Prof Ali, 11/7/19, Test 2
#


def main():

    def instruction():
        print('This program ask user for an integer number and checks the given number is prime or not.')
    instruction();

    x = input("Press 'y' or 'Y' to continue, anything else to exit: ")

    while x == 'y' or x == 'Y':
        y = int(input('Enter an integer number: '))

        def prime_function(x):
            for i in range(2, x):
                if x % i == 0:
                    print(x ,'is not a prime number')
                    break;
                else:
                    print(x, 'is a prime number')
                    break;

        prime_function(y)

        x = input("Press 'y' or 'Y' to continue, anything else to exit: ")


main();

# Bad because I can input 9 and it will output as both prime and not prime
# because 9 % 3 = 0.
