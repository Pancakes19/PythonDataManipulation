# ocean's deepest divers
import pandas as pd
import matplotlib.pyplot as plt

divers = pd.read_csv('deepest-diving-animals.csv')
# print(divers)

# finding lowest diver in three ways
divers = divers.query('depth == @divers["depth"].max()')

divers[divers['depth'] == divers['depth'].max()]

divers.loc[divers['depth'].idxmax()]


print(divers)