# Ryan Lin, CSC 110, Prof Ali, 10/31/19
# Task 01
#


import matplotlib.pyplot as plt

def main():

    programmingLanguages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = ['22.2', '17.6', '8.8', '8', '7.7', '6.7']

    programmingLanguages.reverse()
    popularity.reverse()

    plt.bar(programmingLanguages, popularity)
    plt.show()

main();
