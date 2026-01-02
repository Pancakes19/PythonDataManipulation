import pandas as pd
df = pd.read_csv('human_skeleton.csv')


groups = df.groupby('region')
# this are the two ways to display the number of bones in each region
# by creating groups and the second one is simple
# print(groups['region'].value_counts())
# print()
print(df['region'].value_counts())

# checking the proportions
print(df.shape)
# proportion of 
print(64 + 52 / 204)