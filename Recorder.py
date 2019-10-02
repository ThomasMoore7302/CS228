import os
import shutil
import sys
sys.path.insert(0, 'C:\Users\Thomas\Desktop\Leap_Motion_SDK_Windows_2.3.1\LeapDeveloperKit_2.3.1+31549_win\LeapSDK/lib')
sys.path.insert(0, 'C:\Users\Thomas\Desktop\Leap_Motion_SDK_Windows_2.3.1\LeapDeveloperKit_2.3.1+31549_win\LeapSDK/lib/x64')
from pygameWindow_Del03 import PYGAME_WINDOW
import numpy as np
import pickle
import pygame

class DELIVERABLE:
    def __init__(self, controller, pygameWindow, x,y,xMin, xMax, yMin, yMax, currentNumberOfHands, previousNumberOfHands, num):
        self.controller = controller
        self.pygameWindow = pygameWindow
        self.x = x
        self.y = y
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.currentNumberOfHands = currentNumberOfHands
        self.previousNumberOfHands = previousNumberOfHands
        self.num = num
        self.gestureData = np.zeros((5, 4, 6), dtype='f')

    def Run_Forever(self):
        DELIVERABLE.Run_Once(self)

    def Run_Once(self):
        DELIVERABLE.OS_Subdirectory(self)
        while True:
            pygame.event.get()
            self.pygameWindow.Prepare()
            frame = self.controller.frame()

            handlist = frame.hands
            for hand in handlist:
                if hand > 0:
                    DELIVERABLE.Handle_Frame(self, frame)
            self.previousNumberOfHands = self.currentNumberOfHands
            self.pygameWindow.Reveal()

    def Handle_Frame(self, frame):
        hand = frame.hands[0]
        handList = frame.hands
        nHands = len(handList)
        if(nHands == 1):
            self.currentNumberOfHands = 1
        elif(nHands == 2):
            self.currentNumberOfHands = 2
        fingers = hand.fingers
        length = len(fingers)
        for i in range(length):
            finger = fingers[i]
            DELIVERABLE.Handle_finger(self,i, finger, self.currentNumberOfHands)
        if self.Recording_Is_Ending():
            print(self.gestureData)
            self.Save_Gesture()
            self.num +=1

    def Handle_finger(self,i,finger, currentNumberOfHands):
        global b
        for b in range(4):
            DELIVERABLE.Handle_bone(self,i, finger.bone(b), self.currentNumberOfHands,b )

    def Handle_bone(self,i,bone, currentNumberOfHands,j):
        base = bone.prev_joint
        tip = bone.next_joint
        xBase, yBase = DELIVERABLE.Handle_Vector_From_Leap(self, base)
        xTip, yTip = DELIVERABLE.Handle_Vector_From_Leap(self, tip)

        xBase = DELIVERABLE.Scale(self, xBase, self.xMin, self.xMax, self.yMin, self.yMax)
        xTip = DELIVERABLE.Scale(self, xTip,self.xMin, self.xMax, self.yMin, self.yMax)
        yBase = DELIVERABLE.Scale(self, yBase, self.xMin, self.xMax, self.yMin, self.yMax)
        yTip = DELIVERABLE.Scale(self, yTip,self.xMin, self.xMax, self.yMin, self.yMax)
        self.pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, b, self.currentNumberOfHands)

        if self.Recording_Is_Ending() == True:
            self.gestureData[i, j, 0] = base[0]
            self.gestureData[i, j, 1] = base[1]
            self.gestureData[i, j, 2] = base[2]
            self.gestureData[i, j, 3] = tip[0]
            self.gestureData[i, j, 4] = tip[1]
            self.gestureData[i, j, 5] = tip[2]

    def Handle_Vector_From_Leap(self, v):
        return int(v[0]), int(v[2])

    def Scale(self, param1, old_min, old_max, new_min, new_max):
        scale = (((param1 - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min

        if old_min == old_max:
            return 0
        if new_min == new_max:
            return 0

        return scale

    def Recording_Is_Ending(self):
        if self.currentNumberOfHands == 1 and self.previousNumberOfHands == 2:
            return True

    def Save_Gesture(self):
        filename = "userData/gesture"+str(self.num) +".p"
        pickle_out = open(filename, 'wb')
        pickle.dump(self.gestureData, pickle_out)
        pickle_out.close()

    def OS_Subdirectory(self):
        shutil.rmtree("userData")
        os.mkdir("userData")
