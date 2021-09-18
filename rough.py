## add this file to .gitignore
## this is testing file


@app.route('/',methods = ['POST', 'GET'])
def home():
   if request.method == 'POST':
      year = request.form['value']
      for filepath in glob.iglob('Data/Real-Data/*.csv'):
        if filepath == 'Data/Real-Data/real_{}.csv'.format(year):
            df=pd.read_csv(filepath)
            my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
            my_prediction=my_prediction.tolist()
            return render_template('home.html', prediction = my_prediction )
        elif filepath == 'Data/Real-Data/real_{}.csv'.format(year):
            df=pd.read_csv(filepath)
            my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
            my_prediction=my_prediction.tolist()
            return render_template('home.html', prediction = my_prediction )
        



@app.route('/',methods = ['POST', 'GET'])
def home():
   if request.method == 'POST':
      year = request.form['value']
      for filepath in glob.iglob('Data/Real-Data/*.csv'):
        if filepath == 'Data/Real-Data/real_{}.csv'.format(year):
            df=pd.read_csv(filepath)
            my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
            my_prediction=my_prediction.tolist()
            return render_template('home.html', prediction = my_prediction)
   else:
       return render_template('home.html')





