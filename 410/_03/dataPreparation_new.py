import pandas as pd
import numpy as np
import datasist as ds

train_df = pd.read_csv("train_data.csv")
test_df = pd.read_csv("test_data.csv")

# 1
# print(train_df)
# print(train_df.head(10))
# print(ds.structdata.describe(train_df))

# 2
# ds.structdata.check_train_test_set(train_df, 
#                                     test_df, 
#                                     index='Customer Id', 
#                                     col='Building Dimension')

# print(ds.structdata.check_train_test_set(train_df))                     


# 3
# print(ds.structdata.display_missing(train_df))

# 4
# cat_feats = ds.structdata.get_cat_feats(train_df)
# num_feats = ds.structdata.get_num_feats(train_df)

# print(cat_feats)
# print(num_feats)


# 5 This one does not work
unique_count = ds.structdata.get_unique_counts(train_df)
print(unique_count)

# 6
# all_data, ntrain, ntest = ds.structdata.join_train_and_test(train_df, test_df)
# print("New size of combined data {}".format(all_data.shape))
# print("Old size of train data: {}".format(ntrain))
# print("Old size of test data: {}".format(ntest))
# print(all_data)

# train = all_data[:ntrain]
# test = all_data[ntrain:]