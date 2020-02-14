# libraries
import numpy as np # used for handling numbers
import pandas as pd # used for handling the dataset

#Importing the Dataset:
# to import the dataset into a variable with
# Removing the first unnamed column

dataset = pd.read_csv('mpg.csv',index_col=0)

#print(dataset) #print all
#print(dataset.head()) #print the first 5 rows
#print(dataset.head(10))  # print the first n rows


# Total missing values for each feature
print(dataset.isnull().sum())

# Replace using median
median = dataset['cyl'].median()
dataset['cyl'].fillna(median, inplace=True) #fillna fills the NaN values with a given number with which you want to substitute
print(dataset.isnull().sum())# Check again any missing or not

# Now we are going to encode the categorical data into numerical data type.
print(dataset.dtypes)# See the datatypes

# encode categorical data
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
dataset["manufacturer"]=le.fit_transform(dataset["manufacturer"])
dataset["model"]=le.fit_transform(dataset["model"])
dataset["trans"]=le.fit_transform(dataset["trans"])
dataset["drv"]=le.fit_transform(dataset["drv"])
dataset["fl"]=le.fit_transform(dataset["fl"])
dataset["class"]=le.fit_transform(dataset["class"])
print(dataset.dtypes)
'''
#Visualize the data with boxplot
import matplotlib.pyplot as plt

for column in dataset:
    plt.figure()
    dataset.boxplot([column])
    plt.show()

# Visualize all column in one histogram
fig, axes = plt.subplots(ncols=len(dataset.columns), figsize=(10,5))
for col, ax in zip(dataset, axes):
    dataset[col].value_counts().sort_index().plot.bar(ax=ax, title=col)
plt.tight_layout()
plt.show()
# Visualize all column in separate histogram
fig = plt.figure(figsize = (8,8))
ax = fig.gca()
dataset.hist(ax=ax)
plt.show()
'''
# Splitting the attributes into independent and dependent attributes
X = dataset.iloc[:, :-1].values # attributes to determine independent variable / Class
Y = dataset.iloc[:, -1].values # dependent variable / Class
#print(X)
#print(Y)

#Split data into training and testing dataset. test_size=0.2 means 80% trainig data 20% test data
#Random state ensures that the splits that you generate are reproducible. Scikit-learn uses random permutations to generate the splits.
#The random state that you provide is used as a seed to the random number generator.
from sklearn.model_selection import train_test_split # used for splitting training and testing data
# splitting the dataset into training set and test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

#import your model from scikit-learn
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

#Train Random Forest Model
rf_classifier = RandomForestClassifier(n_estimators=20, max_depth=4)
rf_model=rf_classifier.fit(X_train,Y_train)

#Predict Label
pred=rf_model.predict(X_test)

#Test Model
print("Accuracy:",metrics.accuracy_score(Y_test, pred))

from matplotlib import pyplot as plt
## The line / model
plt.scatter(Y_test, pred)
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.show()

from sklearn.model_selection import KFold
kf = KFold(n_splits=5,random_state=42,shuffle=True)
# Splitting the attributes into independent and dependent attributes
X = dataset.iloc[:, :-1].values # attributes to determine independent variable / Class
Y = dataset.iloc[:, -1].values # dependent variable / Class
accuracies = []
for train_index, test_index in kf.split(X):

    data_train   = X[train_index]
    target_train = Y[train_index]

    data_test    = X[test_index]
    target_test  = Y[test_index]

    # if needed, do preprocessing here

    clf = RandomForestClassifier(n_estimators=20, max_depth=4)
    clf.fit(data_train,target_train)

    preds = clf.predict(data_test)

    # accuracy for the current fold only
    accuracy = metrics.accuracy_score(target_test,preds)

    accuracies.append(accuracy)

# this is the average accuracy over all folds
average_accuracy = np.mean(accuracies)
print("Using Kfold validation, average accuracy:", average_accuracy)