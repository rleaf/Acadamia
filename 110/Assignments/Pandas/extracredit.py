# Ryan Lin , CSC 110, 9/27/19
# EXTRA CREDIT
#

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
### Version 1
### Automated Version, Cleaner syntax
### Only works when the column headers are iterating by 1 (ie: 2000, 2001, 2002, 2003...)

import pandas as pd

x = 'Year'
y = 2000

# df = pd.read_csv('/Users/Ryan/Desktop/pre.csv')
df = pd.read_csv('pre.csv')

while y <= 2018:
    df.rename(columns={str(y): x + ' ' + str(y)}, inplace=True)

    #print(str(y))
    y += 1

    #header = ['Team', x + ' ' + str(y), x + ' ' + str(y), x + ' ' + str(y)]

#df.rename(columns={'2000': x + ' 2000', '2001': x + ' 2001', '2002': x + ' 2002', '2003': x + ' 2003', '2004': x + ' 2004', '2005': x + ' 2005'}, inplace=True)

header = ['Team', 'Year 2000', 'Year 2001', 'Year 2002', 'Year 2003', 'Year 2004', 'Year 2005', 'Year 2006', 'Year 2007', 'Year 2008', 'Year 2009', 'Year 2010',
'Year 2011', 'Year 2012', 'Year 2013', 'Year 2014', 'Year 2015', 'Year 2016', 'Year 2017', 'Year 2018']

#list(df)

#df.to_csv('/Users/Ryan/Desktop/test.csv', header=[col1, col2])
# df.to_csv('/Users/Ryan/Desktop/post.csv', columns=(header))
df.to_csv('post.csv', columns=(header))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
### Version 2
### Messy Version, Specifically referencing each column header in pre.csv
### 100% functionality for only pre.csv

import pandas as pd

x = 'Year'
# df = pd.read_csv('/Users/Ryan/Desktop/pre.csv')
df = pd.read_csv('pre.csv')

df.rename(columns={'2000': x + ' 2000', '2001': x + ' 2001', '2002': x + ' 2002', '2003': x + ' 2003', '2004': x + ' 2004', '2005': x + ' 2005', '2005': x + ' 2005',
'2006': x + ' 2006', '2007': x + ' 2007', '2008': x + ' 2008', '2009': x + ' 2009', '2010': x + ' 2010', '2011': x + ' 2011', '2012': x + ' 2012', '2013': x + ' 2013',
'2014': x + ' 2014', '2015': x + ' 2015', '2016': x + ' 2016', '2017': x + ' 2017', '2018': x + ' 2018'}, inplace=True)

header = ['Team', 'Year 2000', 'Year 2001', 'Year 2002', 'Year 2003', 'Year 2004', 'Year 2005', 'Year 2006', 'Year 2007', 'Year 2008', 'Year 2009', 'Year 2010',
'Year 2011', 'Year 2012', 'Year 2013', 'Year 2014', 'Year 2015', 'Year 2016', 'Year 2017', 'Year 2018']

#list(df)

#df.to_csv('/Users/Ryan/Desktop/test.csv', header=[col1, col2])
# df.to_csv('/Users/Ryan/Desktop/post.csv', columns=(header))
df.to_csv('post.csv', columns=(header))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Do not run this code w/ the assignment. Automatically erases post.csv after run
# Truncates document immediately

# post = '/Users/Ryan/Desktop/post.csv'
# f = open(post, 'w+')
# f.close()
