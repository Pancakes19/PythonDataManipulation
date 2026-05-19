import pandas as pd
import matplotlib.pyplot as plt

df_public = pd.read_csv("healthy-food-survey-public.csv")
#print(df_public)

#calculating the percentage of people who answerd yes and rounding it off

df_public['public'] = df_public.eval('yes / (yes + no + no_opinion)')

df_public['public'] = df_public.eval('public * 100').round()

#

# ok now we drop the columns we dont need 
df_public = df_public[['food', 'public']]
#print(df_public)


#ok now we do the same data cleaning for the experts

df_experts = pd.read_csv('healthy-food-survey-experts.csv')


df_experts['experts'] = df_experts.eval('yes / (yes + no + no_opinion)')


df_experts['experts'] = df_experts.eval('experts * 100').round()


df_experts = df_experts[['food', 'experts']]
#print(df_experts)

#merging the public and expert datasets together and create a new df

df = df_public.merge(df_experts, on='food', how='left')
#print(df)


# visualising paired data with a scatterplot
# each dot represents a food item 
plt.scatter(
    df['public'], 
    df['experts'],
    alpha=0.5
    )

plt.xlabel('Public (%)')
plt.ylabel('Experts (%)')
plt.title('Is food healthy?')

#adding a line
def add_equality_line():
    x = [0, 100]
    y = [0, 100]
    plt.plot(x,y, 
        linestyle='--', 
        alpha=0.5, 
        color='red')    

#a function for squaring the plot and other grid properties
def square_the_plot():
    plt.xlim(0,100)
    plt.ylim(0,100)
    ax = plt.gca()
    ax.set_aspect(1)
    ax.grid(True)


add_equality_line()
square_the_plot()
plt.show()












