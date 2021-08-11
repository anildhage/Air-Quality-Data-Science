#importing variables from another file
from Plot_AQI import avg_data_2013, avg_data_2014, avg_data_2015, avg_data_2016, avg_data_2017, avg_data_2018
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv

#this function will scrape HTML file, grab table that contains data and store it in
#finalD 
def met_data(month, year):
    
    file_html = open('Data/Html_Data/{}/{}.html'.format(year,month), 'rb')
    plain_text = file_html.read()

    tempD = []
    finalD = []

    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)
#after grabbing data in tempD, the data is converted into 15 features
    rows = len(tempD) / 15

#the below code will create list similar to a table with rows and columns
    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)

    length = len(finalD)

#removing the features that are not required as independent features
    finalD.pop(length - 1)
    finalD.pop(0)

    for a in range(len(finalD)):
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)

    return finalD
#the below code will combine all the years data and save it in one file
#cs is the chunksize, if you have low ram, add less size. But we will need as much
#data in the real world to generate correct prediction
def data_combine(year, cs):
    for a in pd.read_csv('Data/Real-Data/real_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist


if __name__ == "__main__":
#Writing the data captured from HTML files and AQI files to a csv file
    if not os.path.exists("Data/Real-Data"):
        os.makedirs("Data/Real-Data")
    for year in range(2013, 2019):
        final_data = []
        with open('Data/Real-Data/real_' + str(year) + '.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(
                ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        for month in range(1, 13):
            temp = met_data(month, year)
            final_data = final_data + temp
#the below one line code will run the module, and bring all the variables of AQI to this
# file so we combine it with the HTML data.            
        pm = getattr(sys.modules[__name__], 'avg_data_{}'.format(year))()

#This below condition is optional
        if len(pm) == 364:
            pm.insert(364, '-')
#add the dependent feature, from Plot_AQI file to the last index
        for i in range(len(final_data)-1):
            # final[i].insert(0, i + 1)
            final_data[i].insert(8, pm[i])
#saving the combined data in a csv file
        with open('Data/Real-Data/real_' + str(year) + '.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
#removing the rows that contain bad data            
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == "-":
                        flag = 1
                if flag != 1:
                    wr.writerow(row)

#Combining all the individual yearly csv files to one file called Real_Combine.csv                    
#Taking cs as 200 for testing purpose, my computer has less memory
    data_2013 = data_combine(2013, 200)
    data_2014 = data_combine(2014, 200)
    data_2015 = data_combine(2015, 200)
    data_2016 = data_combine(2016, 200)
    data_2017 = data_combine(2017, 200)
    data_2018 = data_combine(2018, 200)
    
    total=data_2013+data_2014+data_2015+data_2016+data_2017+data_2018
    
    with open('Data/Real-Data/Real_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
        
        
df=pd.read_csv('Data/Real-Data/Real_Combine.csv')