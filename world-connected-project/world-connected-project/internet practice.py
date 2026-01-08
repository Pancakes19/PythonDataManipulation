import matplotlib.pyplot as plt
import pandas as pd

internet = pd.read_csv('world-internet-users.csv')
print(internet)

int_user_10M = internet.query('internet_users > 100e6')
print(int_user_10M.head(1))