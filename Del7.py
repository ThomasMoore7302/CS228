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

    # print testData
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

def HandleState0(programState):
    programState = 0
    handOver = pygame.image.load('handover.jpg')
    pygameWindow.Draw_Image(handOver, 500, 0)
    return programState

def HandleState1(programState):
    if xBase > 400:
        programState = 1
        handLeft = pygame.image.load('handleft.jpg')
        pygameWindow.Draw_Image(handLeft, 500, 0)
        return programState
    elif xBase < 200:
        programState = 1
        handRight = pygame.image.load('handright.jpg')
        pygameWindow.Draw_Image(handRight, 500, 0)
        return programState
    elif yTip > 225:
        programState = 1
        handForward = pygame.image.load('handforward.jpg')
        pygameWindow.Draw_Image(handForward, 500, 0)
        return programState
    elif yTip < 125:
        programState = 1
        handBackward = pygame.image.load('handback.jpg')
        pygameWindow.Draw_Image(handBackward, 500, 0)
        return programState
    else:
        programState = 2
        handgood = pygame.image.load('handgood.jpg')
        pygameWindow.Draw_Image(handgood, 500, 0)
        return programState

def HandleState2(programState):
    programState = 2
    number = random.randint(0,1)
    # if number == 0:
    zero = pygame.image.load('zero.jpg')
    pygameWindow.Draw_Image(zero, 500, 0)
    aslzero = pygame.image.load('aslzero.jpg')
    pygameWindow.Draw_Image(aslzero, 500, 500)
    if predictedClass == 0:
        great = pygame.image.load('great.png')
        pygameWindow.Draw_Image(great, 500, 500)
    # elif number == 1:
    #     one = pygame.image.load('one.jpg')
    #     pygameWindow.Draw_Image(one, 500, 0)
    # elif number == 2:
    #     two = pygame.image.load('two.jpg')
    #     pygameWindow.Draw_Image(two, 500, 0)
    # elif number == 3:
    #     three = pygame.image.load('three.jpg')
    #     pygameWindow.Draw_Image(three, 500, 0)
    # elif number == 4:
    #     four = pygame.image.load('four.jpg')
    #     pygameWindow.Draw_Image(four, 500, 0)
    # elif number == 5:
    #     five = pygame.image.load('five.jpg')
    #     pygameWindow.Draw_Image(five, 500, 0)
    # elif number == 6:
    #     six = pygame.image.load('six.jpg')
    #     pygameWindow.Draw_Image(six, 500, 0)
    # elif number == 7:
    #     seven = pygame.image.load('seven.jpg')
    #     pygameWindow.Draw_Image(seven, 500, 0)
    # elif number == 8:
    #     eight = pygame.image.load('eight.jpg')
    #     pygameWindow.Draw_Image(eight, 500, 0)
    # elif number == 9:
    #     nine = pygame.image.load('nine.jpg')
    #     pygameWindow.Draw_Image(nine, 500, 0)


    return programState


pygameWindow = PYGAME_WINDOW()

controller = Leap.Controller()
while True:
    global programState
    programState = 0
    pygame.event.get()
    pygameWindow.Prepare()

    frame = controller.frame()

    handlist = frame.hands

    for hand in handlist:

        if hand > 0:
            programState = 1

            Handle_Frame(frame)


    if programState == 0:
        programState = HandleState0(programState)
    if programState == 1:
        programState = HandleState1(programState)
    if programState == 2:
        programState = HandleState2(programState)


    pygameWindow.Reveal()


