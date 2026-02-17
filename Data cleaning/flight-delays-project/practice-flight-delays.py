# flight delays
import pandas as pd
import matplotlib.pyplot as plt

flights = pd.read_csv('flights.csv')
# print(flights)

# making a df from the scheduled and actual flights
departures = flights[['scheduled', 'actual']]
# print(departures)

# departures.info()

# converting sring values to date time
departures['scheduled'] = pd.to_datetime(departures['scheduled'])
departures['actual'] = pd.to_datetime(departures['actual'])

# print(departures.info())

# this modifies the real flights df instead of the departures view we created
# flights.loc[:, 'scheduled'] = pd.to_datetime(flights['scheduled'])
# flights.loc[:, 'actual'] = pd.to_datetime(flights['actual'])

# calcualting the delays
departures['delay'] = departures.eval('actual - scheduled')
print(departures)



