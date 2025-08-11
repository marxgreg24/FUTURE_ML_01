import pandas as pd

train = pd.read_csv('./data/train.csv')
test = pd.read_csv('./data/test.csv')
store = pd.read_csv('./data/store.csv')

# Merge train and store data on 'store' column
train_merged = pd.merge(train, store, on='Store', how='left')
test_merged = pd.merge(test, store, on='Store', how='left')
# # retail_sales = pd.merge(train_merged, test_merged, on='Store', how='outer')

# # view the shapes of the merged dataframes before and after merging
# print("Train shape before merge:", train.shape)
# print("Train shape after merge:", train_merged.shape)

# print("Test shape before merge:", test.shape)
# print("Test shape after merge:", test_merged.shape)

# Save the merged dataframes to new CSV files
# train_merged.to_csv('./data/train_merged.csv', index=False)
# test_merged.to_csv('./data/test_merged.csv', index=False)  
# # retail_sales.to_csv('./data/retail_sales.csv', index=False)

# print(train_merged.describe())
# print(test_merged.describe())
print(train_merged.info())
# print(test_merged.info())