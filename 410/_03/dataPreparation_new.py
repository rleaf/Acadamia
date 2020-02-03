import pandas as pd
import numpy as np
import datasist as ds

train_df = pd.read_csv("train_data.csv")
test_df = pd.read_csv("test_data.csv")

# print(train_df.head(10))

ds.structdata.check_train_test_set(train_df, 
                                    test_df, 
                                    index='Customer Id', 
                                    col='Building Dimension')


# print(ds.structdata.display_missing(train_df))

cat_feats = ds.structdata.get_cat_feats(train_df)
num_feats = ds.structdata.get_num_feats(train_df)
unique_count=ds.structdata.get_unique_counts(train_df)

# print(cat_feats)