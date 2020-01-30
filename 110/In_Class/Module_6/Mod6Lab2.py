# Ryan Lin, CSC 110, Prof Ali, 10/26/19
#

# This is not apart of the lab? Just doing what he wants us to do in class

infile = open('/Users/Ryan/Documents/GitHub/csc110/In_Class/Mod6Lab/numbers.txt', 'w')

for i in range(21):
    number = str(i)
    infile.write(number + '\n')

infile.close()

infile = open('/Users/Ryan/Documents/GitHub/csc110/In_Class/Mod6Lab/numbers.txt', 'r')
c = 0

for line in infile:
    number = float(line)
    print('{:.2f}'.format(number))
    c += number
    print(c)
infile.close()

# End of inclass version. Notice different way of converting string -> int / float


##############################################################################
# Task 02

def main():

    x = open('/Users/Ryan/Documents/GitHub/csc110/In_Class/Mod6Lab/numbers.txt', 'r')
    c = 0

    for line in x:

        # Empty "objects" such as lines are considered false in boolean context
        # Therefore, will iterate until it gets to an empty line.
        # https://stackoverflow.com/questions/17264226/what-does-if-x-strip-mean
        if line.strip():
            n = int(line)
            c += n
    print(c)

    x.close();
main();


##############################################################################
# Task 02

def main():

    x = open('/Users/Ryan/Documents/GitHub/csc110/In_Class/Mod6Lab/numbers.txt', 'r')
    c = i = 0

    for line in x:

        if line.strip():
            n = int(line)
            c += n
            i += 1
    # print('{:.3f}'.format(c/n))
    print(c/n)

    x.close()
main();
