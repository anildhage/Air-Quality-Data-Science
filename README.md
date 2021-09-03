# Air Quality Index Prediction:
 

## Overview
This is a web app that will predict the air quality index feature for the dataset that has independent values. 

1. First the data is gathered from the data source API, which is scraped using python code with Bs4. 
2. Both the independent and target features are collected in a .csv files after cleaning the dataset to train the model using different algorithms 
3. After training the model, prediction is made using alogorithms like regression, rangom forest, lasso regression, etc. 
4. In this example, we have chosen the decision_regression_model. After training the model, we have saved it in the pickel file which will allow the model to be deployed on the local or heroku server. 
5. You can access the prediction results on this link:- https://airqualityindexx01.herokuapp.com
6. Click on predict, the source code has a file real_2018.csv which has the independent values only. These values are used to predict the target feature which is Air Quality Index.

## If you want to run file on the local server

1. Fork this repository, and clone the file on your PC directory 
2. Install the dependencies from the requirements.txt in your new local code environment using the command - 'pip3 install -r requirements.txt'.
3. Run the command - 'python app.py'
4. Open the link that you find in your browser
5. Click predict button to generate target values which is the Air Quality Index values for the independent values
6. Here we have used the real_2018.csv dataset 

## Credits

1. Krish Naik - youtuber. Who helped me to create this project.




