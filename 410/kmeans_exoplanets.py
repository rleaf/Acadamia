import matplotlib.pyplot as plt
import pandas as pd

from sklearn.cluster import KMeans
# from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("exoplanets_small.csv")

df.head(10)

# print(df)

plt.scatter(df.Planet_Name, df.Distance)
plt.show()