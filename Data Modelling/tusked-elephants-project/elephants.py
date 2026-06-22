import os
os.system('cls')
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('male-elephant-tusk-size.csv')
#print(df.head(10))

# creating a pre proaching dataframe to see the tusk lenght

pre_poaching = df.query('period == "1966-68"')
#print(pre_poaching.head(3))


# do same for post poaching
post_recovery = df.query('period == "2005-13"')

#print(post_recovery.head(3))

# printing the avarage for before and after 

print('Before: ', pre_poaching['tusk_length'].mean())
print('After: ', post_recovery['tusk_length'].mean())










