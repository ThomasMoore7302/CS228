import numpy as np
import pickle
import knn


test9 = open("userData/test9.dat", 'rb')
train9 = open("userData/train9.dat", 'rb')
test0 = open("userData/test0.dat", 'rb')
train0 = open("userData/train0.dat", 'rb')

test9 = pickle.load(test9)
train9 = pickle.load(train9)
test0 = pickle.load(test0)
train0 = pickle.load(train0)


def ReshapeData(set1, set2):
    X = np.zeros((2000,5*2*3),dtype='f')
    Y = np.zeros(2000)
    for row in range(0,1000):
        Y[row] = 9
        Y[row + 1000] = 0
        col = 0
        for j in range(0,5):
            for k in range(0,2):
                for m in range(0,3):
                    X[row,col] = set1[j,k,m,row]
                    X[row + 1000,col] = set2[j,k,m,row]
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

train9 = ReduceData(train9)
train0 = ReduceData(train0)
test9 = ReduceData(test9)
test0 = ReduceData(test0)
train9 = CenterData(train9)
test9 = CenterData(test9)
train0 = CenterData(train0)
test0 = CenterData(test0)


trainX, trainY = ReshapeData(train9, train0)
testX, testY = ReshapeData(test9, test0)


knn = knn.KNN()
knn.Use_K_Of(15)
knn.Fit(trainX,trainY)

correct = 0
for row in range(0, 2000):
    prediction = int(knn.Predict(testX[row]))
    answer = int(testY[row])
    if prediction == answer:
        correct += 1

print "accuracy of",(float(correct) / float(2000)) * float(100), '%', "(", correct, "Right )"



pickle.dump(knn,open ('userData/classifer.p','wb'))
