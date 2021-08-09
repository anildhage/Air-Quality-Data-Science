from Plot_AQI import lst2013, lst2014, lst2015, lst2016, lst2017, lst2018

from bs4 import BeautifulSoup

def meta_data(month,year):

    file_html = open('Data/Html_Data/{}/{}.html'.format(year,month), 'rb')
    plain_text = file_html.read()
    tempD = []
    finalD = []
    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a =  tr.get_text()
                tempD.append(a)
    rows = len(tempD)/15

    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)
    print(finalD)








meta_data(1,2013)