import sys
sys.path.insert(0, 'C:\Users\Thomas\Desktop\Leap_Motion_SDK_Windows_2.3.1\LeapDeveloperKit_2.3.1+31549_win\LeapSDK/lib')
sys.path.insert(0, 'C:\Users\Thomas\Desktop\Leap_Motion_SDK_Windows_2.3.1\LeapDeveloperKit_2.3.1+31549_win\LeapSDK/lib/x64')
import Leap
import pickle
import numpy as np
from pygameWindow import PYGAME_WINDOW
import pygame


clf = pickle.load(open("../../userData/classifer.p", 'rb'))
testData = np.zeros((1,30),dtype='f')


x = 500
y = 600
xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0


def Handle_Frame(frame):
    global k, testData
    k = 0
    hand = frame.hands[0]
    fingers = hand.fingers
    length = len(fingers)
    for i in range(length):
        finger = fingers[i]
        Handle_finger(finger)

    # print testData
    testData = CenterData(testData)
    predictedClass = clf.Predict(testData)
    print predictedClass


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
    xBase = Scale(xBase, -100, 100, 0, 700)
    xTip = Scale(xTip, -100, 100, 0, 700)
    yBase = Scale(yBase, -100, 100, 0, 700)
    yTip = Scale(yTip, -100, 100, 0, 700)

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

pygameWindow = PYGAME_WINDOW()

controller = Leap.Controller()
while True:
    pygame.event.get()
    pygameWindow.Prepare()
    frame = controller.frame()

    handlist = frame.hands
    for hand in handlist:
        if hand > 0:

            Handle_Frame(frame)
    pygameWindow.Reveal()


