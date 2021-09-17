from flask import Flask,render_template,url_for,request
import pandas as pd
import glob
import pickle

# load the model from disk
# here we load random forest model as it gave good results when compared
loaded_model=pickle.load(open('pickle-files/RandomForestRegressor.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    csv_files = []
    # Lot of repetition done. Improve the below code
    for item in glob.iglob('Data/Real-Data/*.csv'):
        name = item.replace('Data/Real-Data/', '')
        name1 = name.replace('.csv', '')
        name2 = name1.replace('real_', '')
        name3 = name2.replace('Real_Combine', '2013-2018')
        csv_files.append(name3)
    return render_template('home.html', files = csv_files)

@app.route('/predict',methods=['POST'])
def predict():
    df=pd.read_csv('Data/Real-Data/real_2018.csv')
    my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
    my_prediction=my_prediction.tolist()
    return render_template('result.html',prediction = my_prediction)


if __name__ == '__main__':
	app.run(debug=True)