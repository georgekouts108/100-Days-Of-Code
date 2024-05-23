import csv
import pandas as pd

data = pd.read_csv('weather_data.csv')
temps = list(data.get('temp'))

data_dict = data.to_dict()
temps2 = data['temp'].to_list()

avg_temp = data['temp'].mean()
max_temp = data.temp.max()

print(data[data.day=='Monday'])
print(data[data.temp < 20])

my_dict = {
    'movies': ['pinocchio', 'fantasia', 'the wizard of oz', 'white christmas'],
    'year': [1940, 1940, 1939, 1954]
}

my_data = pd.DataFrame(my_dict)
my_data.to_csv('my_data.csv')

        
