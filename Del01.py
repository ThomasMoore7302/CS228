import sys
sys.path.insert(0, 'C:\Users\Thomas\Desktop\Leap_Motion_SDK_Windows_2.3.1\LeapDeveloperKit_2.3.1+31549_win\LeapSDK/lib')
# Was having an error of not being able to import LeapPython.  This workaround was found at
# https://stackoverflow.com/questions/37914792/python-not-importing-leap-motion-library
sys.path.insert(0, 'C:\Users\Thomas\Desktop\Leap_Motion_SDK_Windows_2.3.1\LeapDeveloperKit_2.3.1+31549_win\LeapSDK/lib/x64')
import Leap

# from pygameWindow import PYGAME_WINDOW
# import random
#
# x = 500
# y = 500
#
# def Perturb_Circle_Position():
#     global x, y
#     fourSidedDieRoll = random.randint(1, 4)
#     if fourSidedDieRoll == 1:
#         x -= 1
#     elif fourSidedDieRoll == 2:
#         x += 1
#     elif fourSidedDieRoll == 3:
#         y -= 1
#     else:
#         y += 1
#
# pygameWindow = PYGAME_WINDOW()
# print pygameWindow
#
controller = Leap.Controller()
while True:
    frame = controller.frame()
#     pygameWindow.Prepare()
#     pygameWindow.Draw_Black_Circle(x, y)
#     Perturb_Circle_Position()
#     pygameWindow.Reveal()
#
#
#
#
