# import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import torch
from torch.autograd import Variable
import torch.nn as nn
# import warnings
# warnings.filterwarnings("ignore")

# Defining car prices
car_prices_array = [3, 4, 5, 6, 7, 8, 9]
car_prices_np = np.array(car_prices_array, dtype=np.float32)

# https://stackoverflow.com/questions/18691084/what-does-1-mean-in-numpy-reshape
car_prices_np = car_prices_np.reshape(-1, 1)
car_price_tensor = Variable(torch.from_numpy(car_prices_np))

#Defining car sales
number_of_car_sell_array = [7.5, 7, 6.5, 6, 5.5, 5, 4.5]
number_of_car_sell_np = np.array(number_of_car_sell_array, dtype=np.float32)
number_of_car_sell_np = number_of_car_sell_np.reshape(-1, 1)
number_of_car_sell_tensor = Variable(torch.from_numpy(car_prices_np))

# plt.scatter(car_prices_array, number_of_car_sell_array)
# plt.xlabel("Car Price $")
# plt.ylabel("Number of Car Sales")
# plt.title("Car Price VS # of Car Sales")
# plt.show()

class LinearRegression(nn.Module):
   def __init__(self, input_size, output_size):
      super(LinearRegression, self).__init__()
      self.linear = nn.Linear(input_dim, output_dim)

   def forward(self, x):
      return self.linear(x)

# Model architecture
input_dim = 1
output_dim = 1
model = LinearRegression(input_dim, output_dim)

# MSE / Cost function
mse = nn.MSELoss()

# Optimization
learning_rate = 0.02
optimizer = torch.optim.SGD(model.parameters(), lr = learning_rate)

#train model
lost_list = []
iteration_number = 301
for iteration in range(iteration_number):
   # Optimization
   optimizer.zero_grad()
   # Forward to get output
   results = model(car_price_tensor)
   # Calculate Loss
   loss = mse(results, number_of_car_sell_tensor)
   # Backward prop
   loss.backward()
   # Updating parameters
   optimizer.step()
   # Store loss
   lost_list.append(loss.data)
   # Print loss
   if (iteration % 50 == 0):
      print('epoch {}, loss {}'.format(iteration, loss.data))

# plt.plot(range(iteration_number), lost_list)
# plt.xlabel("Number of Iterations")
# plt.ylabel("Loss")
# plt.show()

# Predict car price
predicted = model(car_price_tensor).data.numpy()
plt.scatter(car_prices_array, number_of_car_sell_array, label="original data", color="red")
plt.scatter(car_prices_array, predicted, label="predicted data", color="blue")

plt.legend()
plt.xlabel("Car Price $")
plt.ylabel("Number of Car Sell")
plt.title("Original vs Predicted values")
plt.show()


class One():
   def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z

   def oneMethod(self, j):
      return self.x + j

oneI = One(2, 5, 7)
print(oneI.x)

class Three():
   def __init__(self, j = 20):
      self.j = j

   def returnJ(self):
      return self.j

class Two(One):
   def __init__(self, x, y, z, l):
      super().__init__(x, y, z)
      self.l = 9
      self.t = Three(3)

   def twoMethod(self):
      return self.x + self.y + self.z + self.l
   
   def printParam(self):
      print(self.x, self.y, self.z, self.l)

two = Two(1, 2, 3, 4)
print(two.t.returnJ())

class Net():
    def __init__(self):

      # First 2D convolutional layer, taking in 1 input channel (image),
      # outputting 32 convolutional features, with a square kernel size of 3
      self.conv1 = 1
      # Second 2D convolutional layer, taking in the 32 input layers,
      # outputting 64 convolutional features, with a square kernel size of 3
      self.conv2 = 2

      # Designed to ensure that adjacent pixels are either all 0s or all active
      # with an input probability
      self.dropout1 = 3
      self.dropout2 = 4
      # First fully connected layer
      self.fc1 = 5
      # Second fully connected layer that outputs our 10 labels
      self.fc2 = 6

test = Net()
print(test.conv1)