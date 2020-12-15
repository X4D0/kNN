import pandas as pd
import numpy as np
import matplotlib.pyplot as  plt
from collections import Counter

# Split Dataset (Training Set and Testing Set)
def createDataset(x,y):
    #Dataset 1 (1-614 Training Set, sisanya Testing set)
    x_train1 = x[:614]
    x_test1 = x[614:]
    y_train1 = y[:614]
    y_test1 = y[614:]
    #Dataset 2 (1-461 dan 642-768 Training Set, sisanya Testing set)
    x_train2 = x[:461]
    x_train2.append(x[641:], ignore_index = True)
    x_test2 = x[461:641]
    y_train2 = y[:461]
    y_train2.append(y[641:], ignore_index = True)
    y_test2 = y[461:641]
    #Dataset 3 (1-307 dan 462-768 Training Set, sisanya Testing set)
    x_train3 = x[:307]
    x_train3.append(x[461:], ignore_index = True)
    x_test3 = x[307:461]
    y_train3 = y[:307]
    y_train3.append(y[461:], ignore_index = True)
    y_test3 = y[307:461]
    #Dataset 4 (1-154 dan 308-768 Training Set, sisanya Testing set)
    x_train4 = x[:154]
    x_train4.append(x[307:], ignore_index = True)
    x_test4 = x[154:307]
    y_train4 = y[:154]
    y_train4.append(y[307:], ignore_index = True)
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
def distance(x_train1,x_test1,x_train2,x_test2,x_train3,x_test3,x_train4,x_test4,x_train5,x_test5):
    jarak = abs(x_train1-x_test1)-abs(x_train2-x_test2)-abs(x_train3-x_test3)-abs(x_train4-x_test4)-abs(x_train5-x_test5)
    return (jarak)

# Predict Data Test
def predict(x_test,x_train,y_train,k):
    final_output = []
    for i in range(len(x_test)):
        d = []
        votes = []
        for j in range(len(x_train)):
            dist = distance(x_train[j],x_test[j])
            d.append([dist,j])
        d.sort()
        d = d[0:k]
        for d, j in d:
            votes.append(y_train[j])
        final = Counter(votes).most_common(1)[0][0]
        final_output.append(final)
    return final_output

# Scoring
def score(x_test,x_train,y_train,y_test,k):
    prediction = predict(x_test,x_train,y_train,k)
    return (prediction==y_test).sum()/len(y_test)
    
' =============== MAIN ==================== '
k = 7

' --- Importing CSV file --- '
diabetes = pd.read_csv('Diabetes.csv')
#print(diabetes.head()) #Showing top 5 data

' --- Create Variable X and Y --- '
'''
X untuk seluruh kolom kecuali Outcome, dan
Y untuk Kolom Outcome daan mengubah tipe numerik menjadi category
'''
x = diabetes.drop(['Outcome'], axis = 1)
#print(x.head()) #Showing top 5 data, Outcome not included
y = diabetes.Outcome.astype('category')
#category terbagi 2 yaitu 0 = Non-Diabetic, 1 = Diabetic
#print(y.head()) #Showing top 5 data just the Outcome

' Generate Datasets '
x_train1,x_test1,y_train1,y_test1,x_train2,x_test2,y_train2,y_test2,x_train3,x_test3,y_train3,y_test3,x_train4,x_test4,y_train4,y_test4,x_train5,x_test5,y_train5,y_test5 = createDataset(x,y)

print("Dataset 1 :\n")
print("X-Train 1 :\n",x_train1)
print("X-Test 1 :\n",x_test1)
print("Y-Train 1 :\n",y_train1)
print("Y-Tes 1 :\n",y_test1)

print("check : \n")
print(x_train1.iloc[3])
