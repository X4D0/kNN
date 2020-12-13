import pandas as pd
import numpy as np
import matplotlib.pyplot as  plt

#Create 5 Dataset (Training Set and Testing Set)

#Importing CSV file
diabetes = pd.read_csv('Diabetes.csv')
#print(diabetes.head()) #Showing top 5 data

# Create Variable X and Y
x = diabetes.drop(['Outcome'], axis = 1) #X untuk seluruh kolom kecuali Outcome
#print(x.head()) #Showing top 5 data, Outcome not included
y = diabetes.Outcome.astype('category') #Mengubah kolom Outcome dari bertipe numerik menjadi category
# category terbagi 2 yaitu 0 = Non-Diabetic, 1 = Diabetic
#print(y.head()) #Showing top 5 data just the Outcome

