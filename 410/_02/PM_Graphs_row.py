import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# PA = pd.read_csv("data.csv")
# df = pd.DataFrame([{'c1':10, 'c2':100}, {'c1':11,'c2':110}, {'c1':12,'c2':120}])
df = pd.read_csv("data.csv")


date = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []
J = []

for index, row in df.iterrows():
    print(row['ADC'])

# for index, row in PA.iterrows():
#    split = row['created_at'].split()

# print(split)