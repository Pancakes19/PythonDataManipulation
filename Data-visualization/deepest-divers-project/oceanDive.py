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
max_depths = divers.groupby('category')['depth'].max()
# print(max_depths)

# turning the series into a df with reset.index
max_depths = max_depths.reset_index(name='max_depth')
# print(max_depths)


# ploting with the max categories
plt.bar(max_depths['category'], max_depths['max_depth'])
plt.ylabel('Maximum depth (meters)')
plt.show()
























