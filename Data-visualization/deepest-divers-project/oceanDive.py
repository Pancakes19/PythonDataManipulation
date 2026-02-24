# ocean's deepest divers
import pandas as pd
import matplotlib.pyplot as plt

divers = pd.read_csv('deepest-diving-animals.csv')
# print(divers)

# finding lowest diver in three ways
divers.query('depth == @divers["depth"].max()')

divers[divers['depth'] == divers['depth'].max()]

divers.loc[divers['depth'].idxmax()]

# print(divers)


# checking the diff categories
categories = divers['category'].value_counts()
# print(categories)

# finding the deepest diver in each cat
max_depth = divers.groupby('category')['depth'].max()
# print(max_depths)

# turning the series into a df with reset.index
max_depth = max_depth.reset_index(name='max_depth')
# print(max_depths)


# ploting with the max categories
max_depth = max_depth.sort_values('max_depth', ascending=False)
plt.barh(max_depth['category'], max_depth['max_depth'])
plt.xlabel('Maximum depth (meters)')
plt.show()
























