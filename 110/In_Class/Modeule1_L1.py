#Write a program in python that displays your name, address, and telephone number
from textwrap import wrap


school = 'Rider Unviersity'
name = 'Ryan Lin'
csc = 'CSC 110 Computer Science I'
assignment = 'Assignment Number 01 '

lines = '\n Rider University \n Ryan Lin \n CSC 110 Computer Science I \n Assignment Number 01'
test = 'asdlfkadf'
width = 30

print ('-' * width)

for line in wrap(lines, width):
    print('| {0:^{1}} |'.format(line, width))

print('-' * width)

#print('-' * 70)
#print('{:^24s}'.format(school + '\n' + csc + '\n' + assignment + '\n' + name))
print(lines)
