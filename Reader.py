import pickle
class READER:
    def __init__(self):
        pickle_in = open('userData/gesture0.p', 'rb')
        gestureData = pickle.load(pickle_in)
        print gestureData