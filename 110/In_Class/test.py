# Ryan Lin, CSC 110, Prof Ali, Final, 12/11
# Lab
#
# Write a python program that reads the test.txt file’s contents, counts and
# displays the number of vowels and the number of consonants it contains.

def main():

    x = open('/Users/Ryan/Documents/GitHub/csc110/test.txt', 'r')
    vowelCount = consCount = 0;
    vowels = ['a', 'e', 'i', 'o', 'u']
    # vowels = 'a'

    y = x.read();
    # z = y.split();

    for i in y:
        if i in vowels:
            vowelCount += 1;
            print(i)
        elif i not in vowels:
            consCount += 1;
    print('There are', vowelCount, 'vowels.');
    print('There are', consCount, 'consonats.');

    # print(vowels)




main();
