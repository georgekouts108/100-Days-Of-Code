import csv
import pandas as pd

try:
    data = pd.read_csv('squirrels_data.csv')
    fur_colors = set(data['Primary Fur Color'].to_list())
    
    my_dict = {'fur color':[], 'count':[]}
    for fc in fur_colors:
        if str(type(fc)) == "<class 'str'>":
            my_dict['fur color'] = my_dict['fur color'] + [fc]
            count = len(data[data['Primary Fur Color'] == fc])
            my_dict['count'] = my_dict['count'] + [count]
        
    my_data = pd.DataFrame(my_dict)
    my_data.to_csv('squirrel_count.csv') 
except Exception:
    print("an error occurred.")

        
