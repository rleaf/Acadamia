# Ryan Lin, CSC 110, 15 October 2019, Prof Ali
#Task 1
#

product = float(input('Enter a number:'))
while product < 100:
    product *= 10

    # Will terminate print statement if the product is > 100.
    # if product > 100:
    #     break

    print('{:.3f}'.format(product))


######################################################
# Task 2

base_size = 8

for i in range(base_size):
    for c in range(i - 1):
        print('*', end='')
    print()

######################################################
# Task 3

n = int(input('Enter a number: '))
x = 0
for i in range(0, n + 1, 2):
    x +=i

print(x)




for hours in range(24):
    for min in range(60):
        for sec in range(60):
            print(hours, min, sec)
