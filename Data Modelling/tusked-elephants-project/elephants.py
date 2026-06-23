import os
os.system('cls')
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('male-elephant-tusk-size.csv')
#print(df.head(10))

# creating a pre proaching dataframe to see the tusk lenght

pre_poaching = df.query('period == "1966-68"')
#print(pre_poaching.head(3))


# do same for post poaching
post_recovery = df.query('period == "2005-13"')

#print(post_recovery.head(3))

# printing the avarage for before and after 

#print('Before: ', pre_poaching['tusk_length'].mean())
#print('After: ', post_recovery['tusk_length'].mean())

#ploting a scatter plot for tusk length and a shoulder and formating the plot
plt.figure(figsize=(6, 4))
plt.scatter(pre_poaching['shoulder_height'],
            pre_poaching['tusk_length'], marker='^')
plt.scatter(post_recovery['shoulder_height'], post_recovery['tusk_length'], marker='s')
plt.xlabel('Shoulder height (cm)')
plt.ylabel('Tusk Length (cm)')
plt.text(x=200, y=120, s='Pre-poaching', color='C0')
plt.text(x=200, y=35, s='Pre-poaching', color='C1')
plt.show()

#modelling tusk length











