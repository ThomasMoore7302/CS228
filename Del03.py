import Deliverable
import sys
sys.path.insert(0, 'C:\Users\Thomas\Desktop\Leap_Motion_SDK_Windows_2.3.1\LeapDeveloperKit_2.3.1+31549_win\LeapSDK/lib')
sys.path.insert(0, 'C:\Users\Thomas\Desktop\Leap_Motion_SDK_Windows_2.3.1\LeapDeveloperKit_2.3.1+31549_win\LeapSDK/lib/x64')
import Leap
from pygameWindow_Del03 import PYGAME_WINDOW


deliverable = Deliverable.DELIVERABLE(Leap.Controller(), PYGAME_WINDOW(), 500, 600, -100.0, 100.0, 0.0, 700.0, 0, 0, 0)
Deliverable.DELIVERABLE.Run_Forever(deliverable)

