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