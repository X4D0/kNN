import pandas as pd
from math import sqrt
import numpy as np
import matplotlib.pyplot as  plt

# Split Dataset (Training Set and Testing Set)
def createDataset(x,y):
    dataset = []
    for i in range(5):
        if i == 0 : # Subset 1 (1-614 Training Set, sisanya Testing set)
            subset1 = []
            x_train = x[:614]
            x_test = x[614:]
            y_train = y[:614]
            y_test = y[614:]
            subset1.append(x_train)
            subset1.append(x_test)
            subset1.append(y_train)
            subset1.append(y_test)
            dataset.append(subset1)
        elif i == 1 : # Subset 2 (1-461 dan 615-768 Training Set, sisanya Testing set)
            subset2 = []
            x_train = x[:461]
            x_train.append(x[614:])
            x_test = x[461:614]
            y_train = y[:461]
            y_train.append(y[614:])
            y_test = y[461:614]
            subset2.append(x_train)
            subset2.append(x_test)
            subset2.append(y_train)
            subset2.append(y_test)
            dataset.append(subset2)
        elif i == 2 : # Subset 3 (1-307 dan 462-768 Training Set, sisanya Testing set)
            subset3 = []
            x_train = x[:307]
            x_train.append(x[461:])
            x_test = x[307:461]
            y_train = y[:307]
            y_train.append(y[461:])
            y_test = y[307:461]
            subset3.append(x_train)
            subset3.append(x_test)
            subset3.append(y_train)
            subset3.append(y_test)
            dataset.append(subset3)
        elif i == 3 : # Subset 4 (1-154 dan 308-768 Training Set, sisanya Testing set)
            subset4 = []
            x_train = x[:154]
            x_train.append(x[307:])
            x_test = x[154:307]
            y_train = y[:154]
            y_train.append(y[307:])
            y_test = y[154:307]
            subset4.append(x_train)
            subset4.append(x_test)
            subset4.append(y_train)
            subset4.append(y_test)
            dataset.append(subset4)
        else: # Subset 5 (155-768 Training Set, sisanya Testing set)
            subset5 = []
            x_train = x[154:]
            x_test = x[:154]
            y_train = y[154:]
            y_test = y[:154]
            subset5.append(x_train)
            subset5.append(x_test)
            subset5.append(y_train)
            subset5.append(y_test)
            dataset.append(subset5)

    return (dataset)

# Distance Calculation using Manhattan
def euclidean(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)

# Pre-Processing Data
def prepro():
    ' --- Importing CSV file --- '
    pd.set_option('display.max_columns', None)
    diabetes = pd.read_csv('Diabetes.csv')

    ' --- Pre-Processing --- '
    x = diabetes.drop(['Outcome'], axis = 1)
    for col in x.columns:
        x[col].replace([0],[x[col].mean()], inplace = True)
    x_data = x.values.tolist()
    y = diabetes.Outcome.astype('category')
    y_data = y.values.tolist()
    return (x_data,y_data)

# Get similar neighbors
def get_neighbors(train,baris_test,k):
    distances = list()
    for baris_train in train:
        dist = euclidean(baris_test,baris_train)
        distances.append((baris_train, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors

' =============== MAIN ==================== '

x_data,y_data = prepro()

' --- Generate Subsets --- '
dataset = createDataset(x_data,y_data)

'''row0 = dataset[0][0][0]
for row in dataset[0][0]:
    distance = euclidean(row0,row)
    print(distance)'''

