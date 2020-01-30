#!/usr/bin/env python
# coding: utf-8

# ### Load Programs

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ### File Upload

# In[4]:


# Label File Tag
# file = 'Rider University B (40.283093852918036 -74.74257493436426) Primary 06_01_2019 08_31_2019'

# import file
PA = pd.read_csv("data.csv")
date=[]
time=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
J=[]

for index, row in PA.iterrows():
    split=row['created_at'].split()
    date.append(split[0])
    time.append(split[1])
    B.append(row['entry_id'])
    C.append(row['PM1.0_CF_ATM_ug/m3'])
    D.append(row['PM2.5_CF_ATM_ug/m3'])
    E.append(row['PM10.0_CF_ATM_ug/m3'])
    F.append(row['UptimeMinutes'])
    G.append(row['ADC'])
    H.append(row['Temperature_F'])
    I.append(row['Humidity_%'])
    J.append(row['PM2.5_CF_1_ug/m3'])
data_modify={'date':date, 'time':time,'entry_id':B, 'PM1.0_CF_ATM_ug/m3':C,'PM2.5_CF_ATM_ug/m3':D, 'PM10.0_CF_ATM_ug/m3':E,'UptimeMinutes':F,'ADC':G,'Temperature_F':H,'Humidity_%':I,'PM2.5_CF_1_ug/m3':J}
df=pd.DataFrame(data_modify)
df.to_csv('data_modified.csv')

PB = pd.read_csv("data_modified.csv")


# show data with limited rows called head
PB.head(5)

# ### Histogram

# In[50]:


# bin data
bins = [0, 1, 2.5, 5, 7.5, 10, 15, 20, 25, 35, 40]

# build Histogram for Column Heading in csv
plt.hist(PB['PM1.0_CF_ATM_ug/m3'], bins=bins, color='#C73354')
# plt.hist(PA['PM2.5_CF_ATM_ug/m3'], bins=bins, color='#C73354')
# plt.hist(PA['PM10.0_CF_ATM_ug/m3'], bins=bins, color='#C73354')


# plot title and formatting
plt.title('PM1.0 Distribution', fontdict={'fontweight': 'bold', 'fontsize': 18})

# Adding a x and y axis label
plt.xlabel('Concentration ug m-3', fontdict={'fontname': 'Times New Roman', 'fontsize': 18})
plt.ylabel('Frequency of Concentrations', fontdict={'fontname': 'Times New Roman', 'fontsize': 18})

# show the begnning and end by intervals of an value
plt.xticks()
plt.yticks()
# [0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])

# plot legend
# plt.legend()

plt.show()

# In[53]:


# bin data
bins = [0, 1, 2.5, 5, 7.5, 10, 15, 20, 25, 35, 40]

# build Histogram for Column Heading in csv
# plt.hist(PA['PM1.0_CF_ATM_ug/m3'], bins=bins, color='#C73354')
plt.hist(PB['PM2.5_CF_ATM_ug/m3'], bins=bins, color='#C73354')
# plt.hist(PA['PM10.0_CF_ATM_ug/m3'], bins=bins, color='#C73354')


# plot title and formatting
plt.title('PM2.5 Distribution', fontdict={'fontweight': 'bold', 'fontsize': 18})

# Adding a x and y axis label
plt.xlabel('Concentration ug m-3', fontdict={'fontname': 'Times New Roman', 'fontsize': 18})
plt.ylabel('Frequency of Concentrations', fontdict={'fontname': 'Times New Roman', 'fontsize': 18})

# show the begnning and end by intervals of an value
plt.xticks()
plt.yticks()
# [0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])

# plot legend
# plt.legend()

plt.show()

# In[3]:


# bin data
bins = [0, 1, 2.5, 5, 7.5, 10, 15, 20, 25, 35, 40]

# build Histogram for Column Heading in csv
# plt.hist(PA['PM1.0_CF_ATM_ug/m3'], bins=bins, color='#C73354')
# plt.hist(PA['PM2.5_CF_ATM_ug/m3'], bins=bins, color='#C73354')
plt.hist(PB['PM10.0_CF_ATM_ug/m3'], bins=bins, color='#C73354')

# plot title and formatting
plt.title('PM10.0 Distribution', fontdict={'fontweight': 'bold', 'fontsize': 18})

# Adding a x and y axis label
plt.xlabel('Concentration ug m-3', fontdict={'fontname': 'Times New Roman', 'fontsize': 18})
plt.ylabel('Frequency of Concentrations', fontdict={'fontname': 'Times New Roman', 'fontsize': 18})

# show the begnning and end by intervals of an value
plt.xticks()
plt.yticks()
# [0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])

# plot legend
# plt.legend()

plt.show()




