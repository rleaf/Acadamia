# Ryan Lin, CSC 110, 10/10/19, Prof Ali
#
# Assignment 1

x = 0

for x in range(1, 10, 2):
    y = "*" * x
    print('{:^10}'.format(y))
    x += 1;
    if x == 10:
        for x in range(7, 0 , -2):
            y = '*' * x
            print('{:^10}'.format(y))
            x -= - 1

##############################################
# Assignment 2

n = int(input('Give me a non negative integer to factorialize: '))
# n = 5
fac = 1
if n < 0 or isinstance(n, int) != True:
    print('Give me a non negative integer...')

for i in range(1,  n + 1):
        fac *= i

print(fac)

##############################################
# Assignment 3

n = int(input('Give me an integer: '))
# n = 5
ans = 0

for i in range(1, n + 1):
    # print(i)
    ans += (i / n)
    n -= 1
    # n = 1
    # ans += (i / n -1)

print('{0:.3f}'.format(ans))
