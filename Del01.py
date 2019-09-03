import sys
sys.path.insert(0, 'C:\Users\Thomas\Desktop\Leap_Motion_SDK_Windows_2.3.1\LeapDeveloperKit_2.3.1+31549_win\LeapSDK/lib')
# Was having an error of not being able to import LeapPython.  This workaround was found at
# https://stackoverflow.com/questions/37914792/python-not-importing-leap-motion-library
sys.path.insert(0, 'C:\Users\Thomas\Desktop\Leap_Motion_SDK_Windows_2.3.1\LeapDeveloperKit_2.3.1+31549_win\LeapSDK/lib/x64')
import Leap

from pygameWindow import PYGAME_WINDOW
import random

x = 500
y = 500
xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

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

def Handle_Frame(frame):
    hand = frame.hands[0]
    fingers = hand.fingers
    indexFingerList = fingers.finger_type(Leap.Finger.TYPE_INDEX)
    indexFinger = indexFingerList[0]
    distalPhalanx = indexFinger.bone(Leap.Bone.TYPE_DISTAL)
    tip = distalPhalanx.next_joint
    global x, y, xMin, xMax, yMin, yMax, pygameY, pygameX
    x = int(tip[0])
    y = int(tip[1])
    if x < xMin:
        xMin = x
    if x > xMax:
        xMax = x
    if y < yMin:
        yMin = y
    if y > yMax:
        yMax = y


# For this function I had hints given to me by Professor and used
# https://stackoverflow.com/questions/929103/convert-a-number-range-to-another-range-maintaining-ratio/929107
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
    frame = controller.frame()
    handlist = frame.hands
    for hand in handlist:
        if hand > 0:
            Handle_Frame(frame)
            pygameX = Scale(x, 0, 200, 500, 800)
            pygameY = Scale(y, 0, 300, 1000, 500)
            x = pygameX
            y = pygameY
            print x, y
    pygameWindow.Prepare()

    pygameWindow.Draw_Black_Circle(x, y)
#     Perturb_Circle_Position()
    pygameWindow.Reveal()



