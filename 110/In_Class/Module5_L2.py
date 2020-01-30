# Ryan Lin, CSC 110, Prof Ali, 10/22/19
# Task 01
#

def main():

    kilometers = int(input('Enter the distance in kilometers: '))
    print('This program converts miles to kilometers.')

    def miles(x):
        return x * 0.6214

    print(kilometers,' kilometers is equal to {:.2f} miles'.format(miles(kilometers)))

main();



####################################################################
# Task 02


def main():

    print('Enter 5 test scores')
    t1 = int(input('Test Score 1: '))
    t2 = int(input('Test Score 2: '))
    t3 = int(input('Test Score 3: '))
    t4 = int(input('Test Score 4: '))
    t5 = int(input('Test Score 5: '))


    def calc_average(t1, t2, t3, t4, t5):
        return (t1 + t2 + t3 + t4 +t5) / 5


    def determine_grade(testScore):
        if testScore <=100 and testScore >=90:
            return ('A')
        elif testScore <=89 and testScore >=80:
            return ('B')
        elif testScore <=79 and testScore >=70:
            return ('C')
        elif testScore <=69 and testScore >=60:
            return ('D')
        elif testScore <=59:
            return('F')



    print('Your test average is {:.2f}'.format(calc_average(t1, t2, t3, t4, t5)))
    print('Your test 1 letter grade is: ' , determine_grade(t1))
    print('Your test 2 letter grade is: ' , determine_grade(t2))
    print('Your test 3 letter grade is: ' , determine_grade(t3))
    print('Your test 4 letter grade is: ' , determine_grade(t4))
    print('Your test 5 letter grade is: ' , determine_grade(t5))

main();
