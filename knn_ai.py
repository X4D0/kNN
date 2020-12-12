import pandas as pd

#Read Diabetes.csv
def readExcel():
    baca = pd.read_csv(r'Diabetes.csv')
    print(baca)

readExcel()