
# Create a function that will accept all the csv files at once

import pandas as pd
import matplotlib.pyplot as plt

def avg_data(filename):
    temp_i = 0
    average = []
    for rows in pd.read_csv(filename,chunksize=24):
        add_var=0
        avg=0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        average.append(avg)
    return average


lst2013 = avg_data('Data/AQI/aqi2013.csv')
lst2014 = avg_data('Data/AQI/aqi2014.csv')
lst2015 = avg_data('Data/AQI/aqi2015.csv')
lst2016 = avg_data('Data/AQI/aqi2016.csv') 
lst2017 = avg_data('Data/AQI/aqi2017.csv')
lst2018 = avg_data('Data/AQI/aqi2018.csv')
   
 