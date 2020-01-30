# Ryan Lin, CSC 110, Prof Ali, 11/1/19
# assignment07 task 02
#

def main():

    # WINDOWS
    x = open('D:\Github\CSC110\Assignments\lin_assignment07\lottery.txt', 'r')
    #MAC
    # x = open('/Users/Ryan/Documents/GitHub/csc110/Assignments/lin_assignment07/lottery.txt', 'r')

    newNumbers = [i.rstrip('\n') for i in x]

    # for i in x:
    #     z = i.rstrip('\n')
    #     newNumbers.append(z)

    print(newNumbers)
    # print(type(newNumbers))


    x.close();
main();
