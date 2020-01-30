# Ryan Lin, CSC 110, Prof Ali, 10/24/19
# Task 01

def main():

    # x = open('filename.txt', 'w')
    x = open('/Users/Ryan/Documents/GitHub/csc110/In_Class/Mod6Lab/filename.txt', 'w')
    x.write('Ryan Lin')
    x.close()

    # print(type(x))

main();

####################################################################################
# Task 02

def main():

    x = open('/Users/Ryan/Documents/GitHub/csc110/In_Class/Mod6Lab/filename.txt', 'r')
    print(x.read())
    x.close()

main();


####################################################################################
# Task 03

def main():

    x = open('/Users/Ryan/Documents/GitHub/csc110/In_Class/Mod6Lab/names.txt', 'r')
    i = 0
    n1 = x.readline()

    while n1 != '':
        i += 1
        n1 = x.readline()

    print(i)

    x.close()
main();


# x = open('/Users/Ryan/Documents/GitHub/csc110/In_Class/Mod6Lab/numbers.txt', 'r')
# n1 = int(x.readline())
# n2 = int(x.readline())
# n3 = int(x.readline())
# n4 = int(x.readline())
#
# print(n1, n2, n3, n4)



######
# Task 03 Redo
#
# x = open('/Users/Ryan/Documents/GitHub/csc110/In_Class/Mod6Lab/names.txt', 'r')
#
# y = x.readline()
#
# for i in :
#
#     y = x.readline();
#
#     i+=1
#
# print(i)
