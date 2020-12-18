import pandas as pd
from math import sqrt

# Split Dataset (Training Set and Testing Set)
def createDataset(x):
    dataset = []
    for i in range(5):
        if i == 0 : # Subset 1 (1-614 Training Set, sisanya Testing set)
            subset1 = []
            x_train = x[:614]
            x_test = x[614:]
            subset1.append(x_train)
            subset1.append(x_test)
            dataset.append(subset1)
        elif i == 1 : # Subset 2 (1-461 dan 615-768 Training Set, sisanya Testing set)
            subset2 = []
            x_train = x[:461]
            x_train.extend(x[614:])
            x_test = x[461:614]
            subset2.append(x_train)
            subset2.append(x_test)
            dataset.append(subset2)
        elif i == 2 : # Subset 3 (1-307 dan 462-768 Training Set, sisanya Testing set)
            subset3 = []
            x_train = x[:307]
            x_train.extend(x[461:])
            x_test = x[307:461]
            subset3.append(x_train)
            subset3.append(x_test)
            dataset.append(subset3)
        elif i == 3 : # Subset 4 (1-154 dan 308-768 Training Set, sisanya Testing set)
            subset4 = []
            x_train = x[:154]
            x_train.extend(x[307:])
            x_test = x[154:307]
            subset4.append(x_train)
            subset4.append(x_test)
            dataset.append(subset4)
        else: # Subset 5 (155-768 Training Set, sisanya Testing set)
            subset5 = []
            x_train = x[154:]
            x_test = x[:154]
            subset5.append(x_train)
            subset5.append(x_test)
            dataset.append(subset5)

    return (dataset)

# Distance Calculation using Manhattan
def euclidean(row1, row2):
    jarak = 0.0
    for i in range(len(row1)-1):
        jarak += (row1[i] - row2[i])**2
    return sqrt(jarak)

# Pre-Processing Data
def prepro():
    ' --- Importing CSV file --- '
    #pd.set_option('display.max_columns', None)
    diabetes = pd.read_csv('Diabetes.csv')

    ' --- Pre-Processing --- '
    for col in diabetes.columns:
        if col!='Age' and col!='Outcome':
            diabetes[col].replace([0],[diabetes[col].mean()], inplace = True)
        else:
            break
        
    x_data = diabetes.values.tolist()
    return (x_data)

# Get similar neighbors
def neigh(datatrain,baris_test,k):
    jarak = []
    for baris_train in datatrain:
        j = euclidean(baris_test,baris_train)
        jarak.append((baris_train, j))
    jarak.sort(key=lambda tup: tup[1])
    neighbors = []
    for i in range(k):
        neighbors.append(jarak[i][0])
    return neighbors

# Classification
def classification(tatanggi):
    one = 0
    zero = 0
    for i in range(len(tatanggi)):
        if tatanggi[i][8] == 0: zero += 1
        else: one += 1
    if zero > one: outcome_res = 0
    else: outcome_res = 1
    return outcome_res

# Calculate accuracy
def accuracy(actual,predicted):
    correct = 0
    for i in range(len(predicted)):
        if actual[i] == predicted[i]:
            correct += 1
    return (correct/len(predicted))*100

# Best K
def bestK(avgsub,avg):
    for i in range(len(avgsub)):
        if avgsub[i][1] == avg:
            return avgsub[i][0]
        else:
            return print("Not Found!")
        
# kNN
def start(dataset,n_neighbor):
    k = 5
    akurazee = []
    avgsub = []
    for n in n_neighbor:
        akurasi_total = []
        
        for i in range(k):
            predict_result = []
            old_result = []
            for j in range(len(dataset[i][1])):
                #print("Ke-",i)
                datatest = dataset[i][1][j]
                #print("Test : ",datatest)
                datatrain = dataset[i][0]
                #print("Train : ",len(datatrain))
                knn = neigh(datatrain,datatest,n)
                #print("GetNeighbor : ",len(knn))
                #print("Outcome : ",knn[0][8])
                predict = classification(knn)
                predict_result.append(predict)
                fix_old = dataset[i][1][j][8]
                old_result.append(fix_old)
                akurasi = accuracy(old_result,predict_result)
            #print("Dataset-"+str(i+1)+" K="+str(n)+" Accuracy: "+str(akurasi))
            akurasi_total.append(akurasi)
        avg = sum(akurasi_total)/len(akurasi_total)
        avgsub.append([n,avg])
        akurazee.append(avg)
        akurasi_total.clear()
        #print("Accuracy Average : ",avg,"%\n")
    return print("K for testing : ",n_neighbor,"\nHighest Accuracy : "+str(max(akurazee))+"% with K = ",bestK(avgsub,max(akurazee)))

' =============== MAIN ==================== '

x_data = prepro()

' --- Generate Subsets --- '
dataset = createDataset(x_data)
'''print("Length dataset : ",len(dataset))
print("\n")
print("length subset 1 train : ",len(dataset[0][0]))
print("length subset 2 train : ",len(dataset[1][0]))
print("length subset 3 train : ",len(dataset[2][0]))
print("length subset 4 train : ",len(dataset[3][0]))
print("length subset 5 train : ",len(dataset[4][0]))
print("=======================")
print("length subset 1 test : ",len(dataset[0][1]))
print("length subset 2 test : ",len(dataset[1][1]))
print("length subset 3 test : ",len(dataset[2][1]))
print("length subset 4 test : ",len(dataset[3][1]))
print("length subset 5 test : ",len(dataset[4][1]))'''

' --- BISMILLAH --- '
n_neighbor = [31,33]
start(dataset,n_neighbor)
