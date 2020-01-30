import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

####

PA = pd.read_csv("./base/pre.csv")
date= []
time= []
B= []
C= []
D= []
E= []
F= []
G= []
H= []
I= []
J= []

for index, row in PA.iterrows():
   split=row['Team'].split()
   print('toads')