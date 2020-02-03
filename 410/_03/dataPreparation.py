#This tutorial originally created by Rising Odegua@towardsdatascience and modified by Dr. Ali for educational purpose
# at Rider University

import pandas as pd
import datasist as ds  #import datasist library
import numpy as np


train_df = pd.read_csv('train_data.csv')
test_df = pd.read_csv('test_data.csv')

# _________________________________Working with the structdata module___________________________________________________
# The structdata module contains numerous functions for working with structured data mostly in the Pandas DataFrame format.
# That is, you can use these functions to easily manipulate and analyze DataFrames.

#describe: We all know the describe function in Pandas

#print(train_df) #print all
#print(train_df.head()) #print the first 5 rows
#print(train_df.head(10))  # print the first n rows

# we decided to extend it to support full description of a dataset at a glance using datasist.
#print(ds.structdata.describe(train_df))

# check_train_test_set: This function is used to check the sampling strategy of two dataset.
# pass in the two dataset (train_df and test_df ), a common index (customer_id) and finally any feature or column present in both dataset.

#ds.structdata.check_train_test_set(train_df, test_df, index='Customer Id',  col='Building Dimension')

# display_missing: You can check for the missing values in your dataset and
# display the result in the well formatted DataFrame using this function.

# print(ds.structdata.display_missing(train_df))

# get_cat_feats and get_num_feats: Just like their names,
# you can retrieve categorical and numerical features respectively as a Python list.

cat_feats = ds.structdata.get_cat_feats(train_df)
#print(cat_feats)
num_feats = ds.structdata.get_num_feats(train_df)
#print(num_feats)

# get_unique_counts: Ever wanted to check the number of unique classes in your categorical features before you decide what encoding scheme to use?
# well, you can use the get_unique_count function to easily do that.

#unique_count=ds.structdata.get_unique_counts(train_df)
#print(unique_count) #Will not work in Pycharm. Try in Jupyter.

# join_train_and_test: Most of the time when prototyping, you may want to concatenate both train and test set,
# and then apply some transformations to it. You can use the join_train_and_test function for that.
# It returns a concatenated dataset and the size of the train and test set for future splitting.
all_data, ntrain, ntest = ds.structdata.join_train_and_test(train_df, test_df)
#print("New size of combined data {}".format(all_data.shape))
#print("Old size of train data: {}".format(ntrain))
#print("Old size of test data: {}".format(ntest))

#later splitting after transformations
train = all_data[:ntrain]
test = all_data[ntrain:]

#____________________________________ Feature engineering with datasist.________________________________________________
# Feature Engineering is the act of extracting important features from raw data and
# transforming them into formats that are suitable for machine learning models.
# drop_missing: This function drops columns/features with a specified percentage of missing values.

#print(ds.structdata.display_missing(train_df))
# we’ll drop the column with 7.1 percent missing values (Date_of_Occupancy).
# Note: You should not drop a column/feature with so little missing values. The ideal thing to do is to fill it. We drop it here, just for demonstration purpose.

#new_train_df = ds.feature_engineering.drop_missing(train_df, percent=7.0)
#print(ds.structdata.display_missing(new_train_df))

# drop_redundant: This function is used to remove features with low or no variance.
# That is, features that contain the same value all through.
# We show a simple example using an artificial dataset.
df = pd.DataFrame({'a': [1,1,1,1,1,1,1], 'b': [2,3,4,5,6,7,8]})
#print(df)

# column a is redundant, that is it has the same value all through.
# We can drop this column automatically by just passing in the dataset to the drop_redundant function.

#df = ds.feature_engineering.drop_redundant(df)
#print(df)

# convert_dtypes: This function takes a DataFrame as argument and
# automatically type-cast the features to their correct data types.

data = {'Name':['Tom', 'nick', 'jack'],
        'Age':['20', '21', '19'],
        'Date of Birth': ['1999-11-17','20 Sept 1998','Wed Sep 19 14:55:02 2000']}
df = pd.DataFrame(data)
#print(df)

#let’s check the data types…
#print(df.dtypes)

# The features Age and Date of Birth are supposed to be integer and DateTime respectively,
# by passing this dataset to the convert_dtype function, this can be fixed automatically.

#df = ds.feature_engineering.convert_dtype(df)
#print(df.dtypes)

# fill_missing_cats: As the name implies, this function takes a DataFrame,
# and automatically detects categorical columns with missing values.
# It fills them using the mode. # From the dataset,
# we have two categorical features with missing values, these are Garden and Geo_Code.

#df = ds.feature_engineering.fill_missing_cats(train_df)
#print (ds.structdata.display_missing(df))

# fill_missing_nums: This is similar to the fill_missing_cats, except it works on numerical features and
# you can specify a filling strategy (mean, mode or median).
# From the dataset, we have two numerical features with missing values,
# these are Building Dimension and Date_of_Occupancy.

#df = ds.feature_engineering.fill_missing_num(train_df)
#print(ds.structdata.display_missing(df))

# log_transform: This function can help you log transform a set of features.
# It also display the before and after plot with level of skewness to help you
# decide if log transforming feature is what you really want.
# The feature Building Dimension is a right skewed, and we can transform it.
# Note: Columns passed to the log_transform function
# should not contain missing values, else it will throw an error.

#df = ds.feature_engineering.fill_missing_num(train_df)
#df = ds.feature_engineering.log_transform(df, columns=['Building Dimension'])

#_____________________________________WORKING WITH TIME BASED FEATURES__________________________________________________
# extract_dates: This function can extract specified features like day of the week,
# day of the year, hour, min and second of the day from a specified date feature.
new_train = pd.read_csv("Train.csv")
#print(new_train.head(3).T)

# Let’s demonstrate how easy it is to extract information from
# Placement — Time, Arrival at Destination — Time features using the extract_dates function.
# We specify that we want to extract just day of the week (dow) and hour of the day (hr).

date_cols = ['Placement - Time', 'Arrival at Destination - Time']
df = ds.timeseries.extract_dates(new_train, date_cols=date_cols, subset=['dow', 'hr'])
#print(df.head(3).T)
#dff=pd.DataFrame(df)
#dff.to_csv('Train_modified.csv')

# You will instead of 'Placement - Time', 'Arrival at Destination - Time' column, four new column:Placement - Time_dow ,
# Placement - Time_hr, Arrival at Destination - Time_dow, Arrival at Destination - Time_hr

# timeplot: The timeplot function can help you visualize a set features against a particular time feature.
# This can help you identify trends and patterns. To use this function, you can pass a set of numerical columns,
# and then specify the Date feature you want to plot against.

num_cols = ['Time from Pickup to Arrival', 'Destination Long',  'Pickup Long','Platform Type', 'Temperature']
# ds.timeseries.timeplot(new_train, num_cols=num_cols,  time_col='Placement - Time')

# _______________________________Visualization__________________
# VISUALIZATION FOR CATEGORICAL FEATURES
# boxplot: This function makes a box plot of all numerical features against a specified categorical target column.
# A box plot (or box-and-whisker plot) shows the distribution of quantitative data in a way that
# facilitates comparisons between variables or across levels of a categorical variable

#ds.visualizations.boxplot(train_df, target='Claim')


# VISUALIZATION FOR NUMERICAL FEATURES
# histogram: This function makes a histogram plot of all numerical features in a dataset.
# This helps to show distribution of the features.

#fill the missing values first
#df = ds.feature_engineering.fill_missing_num(train_df)
#ds.visualizations.histogram(df)
# scatterplot: This function makes a scatter plot of all numerical features in a
# dataset against a specified numerical target. It helps to show the correlation between features.

#feats = ['Insured_Period', 'Residential', 'Building Dimension', 'Building_Type', 'Date_of_Occupancy']
#ds.visualizations.scatterplot(train_df,num_features=feats, target='Building Dimension',save_fig='ali.png')

#__________________Testing and comparing machine learning models with datasist____________
#import libraries and datasets
'''
import pandas as pd
import numpy as np
import datasist as ds

train = pd.read_csv('train_data.csv')
#test = pd.read_csv('test_data.csv')


# Next, we do some processing. First, we drop the ID column (Customer Id) and
# then we fill missing numerical and categorical features.

#drop the id column
train.drop(columns='Customer Id', axis=1, inplace=True)
#test.drop(columns='Customer Id', axis=1, inplace=True)

#fill missing values
train = ds.feature_engineering.fill_missing_cats(train)
train = ds.feature_engineering.fill_missing_num(train)

#test = ds.feature_engineering.fill_missing_cats(test)
#test = ds.feature_engineering.fill_missing_num(test)

#check the unique classes in each categorical feature
ds.structdata.class_count(train)

# We will label encode Geo_Code, since the unique classes is large, and one-hot-encode the rest.

import category_encoders as ce

# drop target column
target = train['Claim'].values
train.drop(columns='Claim', axis=1, inplace=True)

enc = ce.OrdinalEncoder(cols=['Geo_Code'])
enc.fit(train)
train_enc = enc.transform(train)
#test_enc = enc.transform(test)


#one-hot-encode the rest categorical features
hot_enc = ce.OneHotEncoder()
hot_enc.fit(train_enc)
train_enc = hot_enc.transform(train_enc)
#test_enc = hot_enc.transform(test_enc)


# Now we will split the

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


Xtrain, Xtest, ytrain, ytest = train_test_split(train_enc, target, test_size=0.3, random_state=1)
rf_classifier = RandomForestClassifier(n_estimators=20, max_depth=4)
rf_model=rf_classifier.fit(Xtrain,ytrain)
pred=rf_model.predict(Xtest)
ds.model.get_classification_report(pred,ytest)
'''

'''
# For Example I want to compare three ML models such as naive bayes, decision trees and svm
# compare_model: This model takes as argument multiple machine learning models
# and returns a plot showing each model’s performance.
# Now, let’s see this function in action. We will be comparing three models


from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC

Xtrain, Xtest, ytrain, ytest = train_test_split(train_enc, target, test_size=0.3, random_state=1)
rf_classifier = RandomForestClassifier(n_estimators=20, max_depth=4)
nb_classifier = GaussianNB()
svm_classifier = LinearSVC()
classifiers = [rf_classifier, nb_classifier, svm_classifier]
models, scores = ds.model.compare_model(models_list=classifiers, x_train=Xtrain, y_train=ytrain, scoring_metric='accuracy')
'''