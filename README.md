## Overview
Air Quality Prediction. In this project, we follow the complete life cycle of a data science project from data gathering to deployment of machine learning model. Here is the [link](https://air-prediction.herokuapp.com) where it is deployed. 

## Description
This [website](https://en.tutiempo.net/climate) will have climate data of every country in the world with historical data in some cases date back to 1929. Using a specified locations climate data, we perform feature engineering, explanatory data analysis, feature selection, a various machine learning model training, and deployment of the application to a server. 


## Motivation
After learning about python programming language, this topic of data science was interesting to me. Hence I explored why it is done. I was very much interested in it. Hence, I decided to implement a project that covers the complete data science work in a simple way. 

## Demo
![](ml.gif)
The years that I am entering are the climates historic datasets. The results are shown below Predictions

## Project Structure
```
.
├── Data
│   ├── AQI
│   │   ├── aqi2013.csv
│   │   ├── aqi2014.csv
│   │   ├── aqi2015.csv
│   │   ├── aqi2016.csv
│   │   ├── aqi2017.csv
│   │   └── aqi2018.csv
│   ├── Deployment
│   │   ├── Static
│   │   └── Templates
│   ├── Html_Data
│   │   ├── 2013
│   │   ├── 2014
│   │   ├── 2015
│   │   ├── 2016
│   │   ├── 2017
│   │   └── 2018
│   └── Real-Data
│       ├── real_2013-2018.csv
│       ├── real_2013.csv
│       ├── real_2014.csv
│       ├── real_2015.csv
│       ├── real_2016.csv
│       ├── real_2017.csv
│       └── real_2018.csv
├── Extract_combine.py
├── Html_script.py
├── LICENSE.md
├── ML-Modals
│   ├── DecisionTreeRegressor.ipynb
│   ├── KNearestNeighborRegressor.ipynb
│   ├── LassoRegression.ipynb
│   ├── LinearRegression.ipynb
│   ├── RandomForestRegressor.ipynb
│   └── XgboostRegressor.ipynb
├── Plot_AQI.py
├── Procfile
├── README.md
├── __pycache__
├── app.py
├── ml.gif
├── pickle-files
│   └── RandomForestRegressor.pkl
├── requirements.txt
└── templates
    └── home.html


```
FYI: The above structure is created using the below code from the terminal. You may want to install the dependencies of tree before running
```
tree -L 3

```

## Project status
    Completed but open for contributions, code corrections, improvements
## Steps performed in this project
1. Scraped website, and saved its contents in a folder called HTML_Data
2. The target feature which is also required to train the model is in AQI folder which is saved from a different source. 
3. Both of these folders having the data we need. We bring them together for preprocessing and training. They are saved in the Real-Data folder
4. We use jupyter notebooks or google colab to process the raw data, then train using ML-Models. Models performed can be found in ML-Modals folder
5. In order to deploy the program, we save the models in pickle file which you can find it in the pickle-files folder
6. After comparison, one model gave best result which is the random forest regression. Hence only this model is used for deployment to heroku

## Machine Learning models used
1. Linear Regression
2. Lasso Regression
3. Decision Tree 
4. K nearest Neighbour
5. Random Forest 
6. Xgboost regression

## Methods Used
1. Data Gathering
2. Fearue Engineering
3. EDA
4. Feature Selection
5. Model Building
6. Model Deployment

## Technologies 
1. Python libraries bs4, flask, pandas, matplotlib, scikit, numpy, seaborn
2. HTML
3. heroku for deployment

## Run Locally
### Run this program on your computer
1. fork this repository
2. Open terminal, chose the path where you want this program to be saved and run 
  git clone 'paste the Https link'
3. From terminal enter in to the projects directory then run the below code that will install the dependencies required for this program
  pip install -r requirements.txt
4. After the downloads, run the below code that will start the program
  python app.py
5. In the terminal, find the server link. Open this in your browser. 

## Contributing

I welcome any contributions from you all to make this program work efficiently and the web app to look more nicer. There are many things that can be improved in the project that I will list a few below
1. The web application interface is very simple but the interface is not so nice. This can be improved with CSS. I kept the interface like it served my purpose of showcasing the predictions and the data science work. 
2. If you also specialise in data science, you can also showcase more details on the web program such as charts, accuracy numbers, differences between other machine learning models, etc. This will make the web app more interesting and more informative. 
3. If you are begginer in coding and learning python, you can implement new code that serves some need or improvise some existing code 
4. You can test new machine learning models or algorithms for improving its performance
5. You want to learn how to contribute to the open source projects. Add a code, edit a document like this one, add more features, etc. 

### If you are interested, fork the project, clone the repository, make changes, send a pull requrest. 


## Feedback

If you have any feedback, please reach out to us at i.am.dhage@gmail.com
  

## Lessons Learned

1. How a data science project is supposed to be implemented from it initiation to deployment.
2. How flask can be used to deploy a ML model
3. How to scrape websites. Static and Dynamic


## License
[MIT](https://github.com/anildhage/Air-Quality-Data-Science/blob/master/LICENSE.md)




