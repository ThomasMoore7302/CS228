# hand over image from https://www.keyshot.com/customers/leap-motion/

import sys
sys.path.insert(0, 'C:\Users\Thomas\Desktop\Leap_Motion_SDK_Windows_2.3.1\LeapDeveloperKit_2.3.1+31549_win\LeapSDK/lib')
sys.path.insert(0, 'C:\Users\Thomas\Desktop\Leap_Motion_SDK_Windows_2.3.1\LeapDeveloperKit_2.3.1+31549_win\LeapSDK/lib/x64')
import Leap
import pickle
import numpy as np
from pygameWindow import PYGAME_WINDOW
import pygame
import random

global zero
global testData

clf = pickle.load(open("userData/classifer.p", 'rb'))
testData = np.zeros((1,30),dtype='f')


x = 500
y = 600
xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0


def Handle_Frame(frame):
    global k, testData, predictedClass
    k = 0
    hand = frame.hands[0]
    fingers = hand.fingers
    length = len(fingers)
    for i in range(length):
        finger = fingers[i]
        Handle_finger(finger)


    testData = CenterData(testData)
    predictedClass = clf.Predict(testData)



def CenterData(X):
    allXCoordinates = X[0,::3]
    meanValue = allXCoordinates.mean()
    X[0,::3] = allXCoordinates - meanValue
    allYCoordinates = X[0,1::3]
    meanValue = allYCoordinates.mean()
    X[0,1::3] = allYCoordinates - meanValue
    allZCoordinates = X[0,2::3]
    meanValue = allZCoordinates.mean()
    X[0,2::3] = allZCoordinates - meanValue
    return X



def Handle_finger(finger):
    global b
    for b in range(4):
        Handle_bone(finger.bone(b))


def Handle_bone(bone):
    base = bone.prev_joint
    tip = bone.next_joint
    global xBase,xTip, yBase, yTip, testData, k
    xBase, yBase = Handle_Vector_From_Leap(base)
    xTip, yTip = Handle_Vector_From_Leap(tip)
    xBase = Scale(xBase, -200, 100, 100, 350)
    xTip = Scale(xTip, -200, 100, 100, 350)
    yBase = Scale(yBase, -200, 100, 100, 350)
    yTip = Scale(yTip, -200, 100, 100, 350)


    pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, b)

    if ((b == 0) or (b == 3)):

        testData[0,k] = tip[0]
        testData[0,k + 1] = tip[1]
        testData[0,k + 2] = tip[2]
        k = k + 3

def Handle_Vector_From_Leap(v):
    return int(v[0]), int(v[2])



def Scale(param1, old_min, old_max, new_min, new_max):
    scale = (((param1 - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min
    if old_min == old_max:
        return 0
    if new_min == new_max:
        return 0
    return scale

def HandleState0():
    handOver = pygame.image.load('handover.jpg')
    pygameWindow.Draw_Image(handOver, 500, 0)


def HandleState1():
    global programState
    if xBase > 400:
        handLeft = pygame.image.load('handleft.jpg')
        pygameWindow.Draw_Image(handLeft, 500, 0)
    elif xBase < 200:
        handRight = pygame.image.load('handright.jpg')
        pygameWindow.Draw_Image(handRight, 500, 0)
    elif yTip > 225:
        handForward = pygame.image.load('handforward.jpg')
        pygameWindow.Draw_Image(handForward, 500, 0)
    elif yTip < 125:
        handBackward = pygame.image.load('handback.jpg')
        pygameWindow.Draw_Image(handBackward, 500, 0)
    else:
        handgood = pygame.image.load('handgood.jpg')
        pygameWindow.Draw_Image(handgood, 500, 0)
        programState = 2




def HandleState2():
    global number, programState

    if number == -1:
        number = random.randint(0, 9)

    if number == 0:
        zero = pygame.image.load('zero.jpg')
        pygameWindow.Draw_Image(zero, 500, 0)
        aslzero = pygame.image.load('aslzero.jpg')
        pygameWindow.Draw_Image(aslzero, 500, 500)
        try:
            if predictedClass == 0:
                programState = 3
                userRecord['digit0attempted'] += 1
            else:
                for i in range(500):
                    if i == 500:
                        userRecord['digit0attempted'] += 1
        except KeyError:
            userRecord['digit0attempted'] = 1

        database[userName] = userRecord
        pickle.dump(database, open('userData/database.p', 'wb'))



    if number == 1:
        one = pygame.image.load('one.jpg')
        pygameWindow.Draw_Image(one, 500, 0)
        aslone = pygame.image.load('aslone.jpg')
        pygameWindow.Draw_Image(aslone, 500, 500)
        try:
            if predictedClass == 1:
                programState = 3
                userRecord['digit1attempted'] += 1
            else:
                for i in range(500):
                    if i == 500:
                        userRecord['digit1attempted'] += 1
        except KeyError:
            userRecord['digit1attempted'] = 1

        database[userName] = userRecord
        pickle.dump(database, open('userData/database.p', 'wb'))

    if number == 2:
        two = pygame.image.load('two.jpg')
        pygameWindow.Draw_Image(two, 500, 0)
        asltwo = pygame.image.load('asltwo.jpg')
        pygameWindow.Draw_Image(asltwo, 500, 500)
        try:
            if predictedClass == 2:
                programState = 3
                userRecord['digit2attempted'] += 1
            else:
                for i in range(500):
                    if i == 500:
                        userRecord['digit2attempted'] += 1
        except KeyError:
            userRecord['digit2attempted'] = 1

        database[userName] = userRecord
        pickle.dump(database, open('userData/database.p', 'wb'))


    if number == 3:
        three = pygame.image.load('three.jpg')
        pygameWindow.Draw_Image(three, 500, 0)
        aslthree = pygame.image.load('aslthree.jpg')
        pygameWindow.Draw_Image(aslthree, 500, 500)
        try:
            if predictedClass == 3:
                programState = 3
                userRecord['digit3attempted'] += 1
            else:
                for i in range(500):
                    if i == 500:
                        userRecord['digit3attempted'] += 1
        except KeyError:
            userRecord['digit3attempted'] = 1

        database[userName] = userRecord
        pickle.dump(database, open('userData/database.p', 'wb'))

    if number == 4:
        four = pygame.image.load('four.jpg')
        pygameWindow.Draw_Image(four, 500, 0)
        aslfour = pygame.image.load('aslfour.jpg')
        pygameWindow.Draw_Image(aslfour, 500, 500)
        try:
            if predictedClass == 4:
                programState = 3
                userRecord['digit4attempted'] += 1
            else:
                for i in range(500):
                    if i == 500:
                        userRecord['digit4attempted'] += 1
        except KeyError:
            userRecord['digit4attempted'] = 1

        database[userName] = userRecord
        pickle.dump(database, open('userData/database.p', 'wb'))

    if number == 5:
        five = pygame.image.load('five.jpg')
        pygameWindow.Draw_Image(five, 500, 0)
        aslfive = pygame.image.load('aslfive.jpg')
        pygameWindow.Draw_Image(aslfive, 500, 500)
        try:
            if predictedClass == 5:
                programState = 3
                userRecord['digit5attempted'] += 1
            else:
                for i in range(500):
                    if i == 500:
                        userRecord['digit5attempted'] += 1
        except KeyError:
            userRecord['digit5attempted'] = 1

        database[userName] = userRecord
        pickle.dump(database, open('userData/database.p', 'wb'))


    if number == 6:
        six = pygame.image.load('six.jpg')
        pygameWindow.Draw_Image(six, 500, 0)
        aslsix = pygame.image.load('aslsix.jpg')
        pygameWindow.Draw_Image(aslsix, 500, 500)
        try:
            if predictedClass == 6:
                programState = 3
                userRecord['digit6attempted'] += 1
            else:
                for i in range(500):
                    if i == 500:
                        userRecord['digit6attempted'] += 1
        except KeyError:
            userRecord['digit6attempted'] = 1

        database[userName] = userRecord
        pickle.dump(database, open('userData/database.p', 'wb'))


    if number == 7:
        seven = pygame.image.load('seven.jpg')
        pygameWindow.Draw_Image(seven, 500, 0)
        aslseven = pygame.image.load('aslseven.jpg')
        pygameWindow.Draw_Image(aslseven, 500, 500)
        try:
            if predictedClass == 7:
                programState = 3
                userRecord['digit7attempted'] += 1
            else:
                for i in range(500):
                    if i == 500:
                        userRecord['digit7attempted'] += 1
        except KeyError:
            userRecord['digit7attempted'] = 1

        database[userName] = userRecord
        pickle.dump(database, open('userData/database.p', 'wb'))


    if number == 8:
        eight = pygame.image.load('eight.jpg')
        pygameWindow.Draw_Image(eight, 500, 0)
        asleight = pygame.image.load('asleight.jpg')
        pygameWindow.Draw_Image(asleight, 500, 500)
        try:
            if predictedClass == 8:
                programState = 3
                userRecord['digit8attempted'] += 1
            else:
                for i in range(500):
                    if i == 500:
                        userRecord['digit8attempted'] += 1
        except KeyError:
            userRecord['digit8attempted'] = 1

        database[userName] = userRecord
        pickle.dump(database, open('userData/database.p', 'wb'))


    if number == 9:
        nine = pygame.image.load('nine.jpg')
        pygameWindow.Draw_Image(nine, 500, 0)
        aslnine = pygame.image.load('aslnine.jpg')
        pygameWindow.Draw_Image(aslnine, 500, 500)
        try:
            if predictedClass == 9:
                programState = 3
                userRecord['digit9attempted'] += 1
            else:
                for i in range(500):
                    if i == 500:
                        userRecord['digit9attempted'] += 1
        except KeyError:
            userRecord['digit9attempted'] = 1

        database[userName] = userRecord
        pickle.dump(database, open('userData/database.p', 'wb'))





def HandleState3():
    global programState, number
    great = pygame.image.load('great.png')
    pygameWindow.Draw_Image(great, 500, 500)
    number = -1






global programState, number
pygameWindow = PYGAME_WINDOW()
controller = Leap.Controller()
number = -1

database = pickle.load(open('userData/database.p','rb'))

pickle.dump(database,open('userData/database.p','wb')) #First time

userName = raw_input('Please enter your name: ')
if userName in database:
	print('Welcome back ' + userName + '.')
	database[userName]['login'] += 1
else:
	database[userName] = {'login' : 1}
	print('Welcome ' + userName + '.')
print(database)
userRecord = database[userName]


pickle.dump(database,open('userData/database.p','wb')) #Second time


while True:



    pygame.event.get()
    pygameWindow.Prepare()

    frame = controller.frame()

    handlist = frame.hands
    programState = 0
    for hand in handlist:



        if hand > 0:
            programState = 1
            Handle_Frame(frame)
            HandleState1()
    if programState != 1 and programState != 2 and programState != 3:
        HandleState0()
    elif programState == 2:
        HandleState2()
    if programState == 3:
        HandleState3()



    pygameWindow.Reveal()


