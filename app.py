from flask import Flask,render_template,url_for,request,redirect
import pandas as pd
import glob
import os
import pickle

# load the model from disk
# here we load random forest model as it gave good results when compared
loaded_model=pickle.load(open('pickle-files/RandomForestRegressor.pkl', 'rb'))
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def home():
   if request.method == 'POST':
        year = request.form['value']
        if len(year) == 0:
            return render_template('home.html')
        elif year != 2013 or year != 2014 or year != 2015 or year != 2016 or year != 2017 or year != 2018:
            return render_template('home.html', num = 'You did not enter the above year correctly')
        else:
            df=pd.read_csv('Data/Real-Data/real_{}.csv'.format(year))
            my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
            my_prediction=my_prediction.tolist()
            return render_template('home.html', prediction = my_prediction)
   else:
       return render_template('home.html')




if __name__ == '__main__':
	app.run(debug=True)