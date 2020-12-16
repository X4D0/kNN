import pandas as pd
from math import sqrt
import numpy as np
import matplotlib.pyplot as  plt

# Split Dataset (Training Set and Testing Set)
def createDataset(x,y):
    #Dataset 1 (1-614 Training Set, sisanya Testing set)
    x_train1 = x[:614]
    x_test1 = x[614:]
    y_train1 = y[:614]
    y_test1 = y[614:]
    #Dataset 2 (1-461 dan 642-768 Training Set, sisanya Testing set)
    x_train2 = x[:461]
    x_train2.append(x[641:])
    x_test2 = x[461:641]
    y_train2 = y[:461]
    y_train2.append(y[641:])
    y_test2 = y[461:641]
    #Dataset 3 (1-307 dan 462-768 Training Set, sisanya Testing set)
    x_train3 = x[:307]
    x_train3.append(x[461:])
    x_test3 = x[307:461]
    y_train3 = y[:307]
    y_train3.append(y[461:])
    y_test3 = y[307:461]
    #Dataset 4 (1-154 dan 308-768 Training Set, sisanya Testing set)
    x_train4 = x[:154]
    x_train4.append(x[307:])
    x_test4 = x[154:307]
    y_train4 = y[:154]
    y_train4.append(y[307:])
    y_test4 = y[154:307]
    #Dataset 5 (155-768 Training Set, sisanya Testing set)
    x_train5 = x[154:]
    x_test5 = x[:154]
    y_train5 = y[154:]
    y_test5 = y[:154]
    return (x_train1,x_test1,y_train1,y_test1,x_train2,x_test2,y_train2,y_test2
            ,x_train3,x_test3,y_train3,y_test3,x_train4,x_test4,y_train4,y_test4
            ,x_train5,x_test5,y_train5,y_test5)

# Distance Calculation using Manhattan
def distance(xtr1,xtr2,xtr3,xtr4,xtr5,xtr6,xtr7,xtr8,xte1,xte2,xte3,xte4,xte5,xte6,xte7,xte8):
    jarak = abs(xtr1-xte1)-abs(xtr2-xte2)-abs(xtr3-xte3)-abs(xtr4-xte4)-abs(xtr5-xte5)-abs(xtr6-xte6)-abs(xtr7-xte8)-abs(xtr8-xte8)
    return (jarak)

def vote(zero,one):
    kategori = []
    kategori.insert(0,zero)
    kategori.insert(1,one)
    return (kategori)

def sort(listnya):
    for i in range(1, len(listnya)):
        j = i-1
        nextnya = listnya[i]
        while (listnya[j] > nextnya) and (j >= 0):
            listnya[j+1] = listnya[j]
            j-=1
        listnya[j+1] = nextnya
    return (listnya)

' =============== MAIN ==================== '

' --- Importing CSV file --- '
diabetes = pd.read_csv('Diabetes.csv')

''' --- Create Variable X and Y --- 

X untuk seluruh kolom kecuali Outcome, dan
Y untuk Kolom Outcome dan mengubah tipe numerik menjadi category

'''
x = diabetes.drop(['Outcome'], axis = 1)
x_data = x.values.tolist()
y = diabetes.Outcome.astype('category')
y_data = y.values.tolist()

' Generate Datasets '
x_train1,x_test1,y_train1,y_test1,x_train2,x_test2,y_train2,y_test2,x_train3,x_test3,y_train3,y_test3,x_train4,x_test4,y_train4,y_test4,x_train5,x_test5,y_train5,y_test5 = createDataset(x_data,y_data)

' START '
k = 7
jarak1 = []
temp = []
jarak2 = []
close = []
categor = []
categores = []
i = 0

while i < len(x_test1):
    n = 0
    while n < len(x_train1):
        jarak = distance(float(x_train1[n][0]),float(x_train1[n][1]),float(x_train1[n][2]),float(x_train1[n][3]),float(x_train1[n][4]),float(x_train1[n][5]),
                         float(x_train1[n][6]),float(x_train1[n][7]),float(x_test1[i][0]),float(x_test1[i][1]),float(x_test1[i][2]),float(x_test1[i][3]),
                         float(x_test1[i][4]),float(x_test1[i][5]),float(x_test1[i][6]),float(x_test1[i][7]))
        temp.insert(n,jarak)
        jarak1.insert(n,jarak)
        temp.append(y_train1[n])
        jarak2.extend(temp)
        temp.clear()
        n += 1
    m = 0
    while m <= k:
        zero = 0
        one = 0
        close = sort(jarak1)
        z = 0
        while z < 614 :
            if close[m] == jarak2[z] :
                z += 1  
                if (jarak2[z] == '1'):
                    one += 1
                else :
                    zero += 1 
            else :
                z=z+1
        categor = vote(zero,one)
        m += 1
    if (categor[1]==1):
        categores.insert(i,1)
    else :
        categores.insert(i,0)
    jarak2.clear()
    jarak1.clear()
    close.clear()
    categor.clear()
    i += 1
x = 0
for x in range(0, len(categores)):
    print ("baris ke-",x+1,", dengan Y = ",categores[x])'''
