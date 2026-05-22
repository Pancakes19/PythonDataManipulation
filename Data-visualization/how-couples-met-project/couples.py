import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("how-couples-met.csv")
#print(df)

# ploting the df on a line graph
#df.plot()
#plt.show()

#making the decade column the index
df = df.set_index('decade')
#print(df)
#df.plot()
#plt.show()

# making the online dating line stand out more
focus_column = 'online'
focus_color = 'C3'
back_columns = [
    'college',
    'at work',
    'through friends',
    'through family',
    'restaurant',
    'neighbors'
    ]
back_colors = ['C0','C1','C2','C4','C5','C6']

df.plot(y=back_columns, color=back_colors, alpha=0.5)
plt.plot(df.index, df[focus_column], color= focus_color, linewidth=5)
plt.show()


































