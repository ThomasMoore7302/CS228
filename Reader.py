import pickle
import os
from pygameWindow_Del03 import PYGAME_WINDOW
import pygame
import time

class READER:
    def __init__(self):
        # pickle_in = open('userData/gesture0.p', 'rb')
        # gestureData = pickle.load(pickle_in)
        # print gestureData
        path, dirs, files = next(os.walk('userData'))
        self.numGestures = len(files)
        self.pygameWindow = PYGAME_WINDOW()

    def Print_Gesture(self):
        for i in range(0,self.numGestures):
            pickle_in = open("userData/gesture"+str(i) + ".p", 'rb')
            print pickle.load(pickle_in)

    def Draw_Gestures(self):
        while True:
            pygame.event.get()

            READER.Draw_Each_Gesture_Once(self)



    def Draw_Each_Gesture_Once(self):
            for i in range(0, self.numGestures):
                READER.Draw_Gesture(self, i)

    def Draw_Gesture(self, i):
        self.pygameWindow.Prepare()
        pickle_in = open("userData/gesture" + str(i) + ".p", 'rb')
        gesture_data = pickle.load(pickle_in)
        for i in range(0,5):
            for j in range(0,4):
                xBaseNotYetScaled = -gesture_data[i,j,0]
                yBaseNotYetScaled = -gesture_data[i,j,2]
                xTipNotYetScaled = -gesture_data[i,j,3]
                yTipNotYetScaled = -gesture_data[i,j,5]

                xBase = READER.Scale(self, xBaseNotYetScaled, 1000, -1000, -100, 700)
                yBase = READER.Scale(self, yBaseNotYetScaled, 1000, -1000, 0, 700)
                xTip = READER.Scale(self, xTipNotYetScaled, 1000, -1000, -100, 700)
                yTip = READER.Scale(self, yTipNotYetScaled, 1000, -1000, 0, 700)

                self.pygameWindow.Draw_Line(xBase,yBase,xTip,yTip, 1, 2)
        self.pygameWindow.Reveal()
        time.sleep(0.1)

    def Scale(self, param1, old_min, old_max, new_min, new_max):
        scale = (((param1 - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min

        if old_min == old_max:
            return 0
        if new_min == new_max:
            return 0
        return scale





