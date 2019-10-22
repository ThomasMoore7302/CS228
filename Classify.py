import numpy as np
import pickle
import knn


train1 = open("userData/Clark_train1.p", 'rb')
test1 = open("userData/Clark_test1.p", 'rb')
train2 = open("userData/Liu_train2.p", 'rb')
test2 = open("userData/Liu_test2.p", 'rb')
train3 = open("userData/Trinity_train3.p", 'rb')
test3 = open("userData/Trinity_test3.p", 'rb')
train4 = open("userData/Beatty_train4.p", 'rb')
test4 = open("userData/Beatty_test4.p", 'rb')
train5 = open("userData/Ortigara_train5.p", 'rb')
test5 = open("userData/Ortigara_test5.p", 'rb')
train6 = open("userData/Huang_train6.p", 'rb')
test6 = open("userData/Huang_test6.p", 'rb')
train7 = open("userData/Huang_train7.p", 'rb')
test7 = open("userData/Huang_test7.p", 'rb')
train8 = open("userData/Burleson_train8.p", 'rb')
test8 = open("userData/Burleson_test8.p", 'rb')
test9 = open("userData/test9.dat", 'rb')
train9 = open("userData/train9.dat", 'rb')
test0 = open("userData/test0.dat", 'rb')
train0 = open("userData/train0.dat", 'rb')

train1 = pickle.load(train1)
test1 = pickle.load(test1)
train2 = pickle.load(train2)
test2 = pickle.load(test2)
train3 = pickle.load(train3)
test3 = pickle.load(test3)
train4 = pickle.load(train4)
test4 = pickle.load(test4)
train5 = pickle.load(train5)
test5 = pickle.load(test5)
train6 = pickle.load(train6)
test6 = pickle.load(test6)
train7 = pickle.load(train7)
test7 = pickle.load(test7)
train8 = pickle.load(train8)
test8 = pickle.load(test8)
test9 = pickle.load(test9)
train9 = pickle.load(train9)
test0 = pickle.load(test0)
train0 = pickle.load(train0)


def ReshapeData(set1, set2, set3, set4, set5, set6, set7, set8, set9, set0):
    X = np.zeros((10000,5*2*3),dtype='f')
    Y = np.zeros(10000)
    for row in range(0,1000):
        Y[row] = 1
        Y[row + 1000] = 2
        Y[row + 2000] = 3
        Y[row + 3000] = 4
        Y[row + 4000] = 5
        Y[row + 5000] = 6
        Y[row + 6000] = 7
        Y[row + 7000] = 8
        Y[row + 8000] = 9
        Y[row + 9000] = 0
        col = 0
        for j in range(0,5):
            for k in range(0,2):
                for m in range(0,3):
                    X[row,col] = set1[j,k,m,row]
                    X[row + 1000,col] = set2[j,k,m,row]
                    X[row + 2000,col] = set3[j,k,m,row]
                    X[row + 3000,col] = set4[j,k,m,row]
                    X[row + 4000, col] = set5[j, k, m, row]
                    X[row + 5000, col] = set6[j, k, m, row]
                    X[row + 6000, col] = set7[j, k, m, row]
                    X[row + 7000, col] = set8[j, k, m, row]
                    X[row + 8000, col] = set9[j, k, m, row]
                    X[row + 9000, col] = set0[j, k, m, row]
                    col = col + 1

    return X , Y

def ReduceData(X):
    X = np.delete(X,1,1)
    X = np.delete(X,1,1)
    X = np.delete(X,0,2)
    X = np.delete(X,0,2)
    X = np.delete(X,0,2)
    return X


def CenterData(X):

    allXCoordinates = X[:,:,0,:]
    meanValue = allXCoordinates.mean()
    X[:,:,0,:] = allXCoordinates - meanValue
    allYCoordinates = X[:,:,1,:]
    meanValue = allYCoordinates.mean()
    X[:,:,1,:] = allYCoordinates - meanValue
    allZCoordinates = X[:,:,2,:]
    meanValue = allZCoordinates.mean()
    X[:,:,2,:] = allZCoordinates - meanValue
    return X

train1 = ReduceData(train1)
train2 = ReduceData(train2)
train3 = ReduceData(train3)
train4 = ReduceData(train4)
train5 = ReduceData(train5)
train6 = ReduceData(train6)
train7 = ReduceData(train7)
train8 = ReduceData(train8)
train9 = ReduceData(train9)
train0 = ReduceData(train0)

test1 = ReduceData(test1)
test2 = ReduceData(test2)
test3 = ReduceData(test3)
test4 = ReduceData(test4)
test5 = ReduceData(test5)
test6 = ReduceData(test6)
test7 = ReduceData(test7)
test8 = ReduceData(test8)
test9 = ReduceData(test9)
test0 = ReduceData(test0)

train1 = CenterData(train1)
train2 = CenterData(train2)
train3 = CenterData(train3)
train4 = CenterData(train4)
train5 = CenterData(train5)
train6 = CenterData(train6)
train7 = CenterData(train7)
train8 = CenterData(train8)
train9 = CenterData(train9)
train0 = CenterData(train0)

test1 = CenterData(test1)
test2 = CenterData(test2)
test3 = CenterData(test3)
test4 = CenterData(test4)
test5 = CenterData(test5)
test6 = CenterData(test6)
test7 = CenterData(test7)
test8 = CenterData(test8)
test9 = CenterData(test9)
test0 = CenterData(test0)



trainX, trainY = ReshapeData(train1, train2, train3, train4, train5, train6, train7, train8, train9, train0)
testX, testY = ReshapeData(test1, test2, test3, test4, test5, test6, test7, test8, test9, test0)


knn = knn.KNN()
knn.Use_K_Of(15)
knn.Fit(trainX,trainY)

correct = 0
for row in range(0, 10000):
    prediction = int(knn.Predict(testX[row]))
    answer = int(testY[row])
    if prediction == answer:
        correct += 1
    print prediction, answer, correct, '/', row
print "accuracy of",(float(correct) / float(10000)) * float(100), '%', "(", correct, "Right )"



pickle.dump(knn,open ('userData/classifer.p','wb'))
