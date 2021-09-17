# This file is for testing
# Delete after project completion or add it to .gitignore
import glob


def home():
    csv_files = []
    home.var = "variable inside function_1"
    # Lot of repetition done. Improve the below code
    for item in glob.iglob('Data/Real-Data/*.csv'):
        name = item.replace('Data/Real-Data/', '')
        name1 = name.replace('.csv', '')
        name2 = name1.replace('real_', '')
        name3 = name2.replace('Real_Combine', '2013-2018')
        csv_files.append(name3)

def predict():
    csv = home.var
    print(len(csv))

home()
predict()