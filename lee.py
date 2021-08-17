from pyfirmata import Arduino, util
import time


AnalogPin = 0
tyrelength = 0.2
switch = True
threshold = 0.4
count = 0


def init():
    board = Arduino("COM3")
    it = util.Iterator(board)
    it.start()
    board.analog[AnalogPin].enable_reporting()





def calibration():
    time.sleep(2000)
    zeroLevel = board.analog[AnalogPin].read()
    time.sleep(2000)
    return zeroLevel

def total_length(counts):
    return counts*tyrelength

def mide():

    while switch==True:
        rawValue = board.analog[AnalogPin].read() - zeroLevel
        print(rawValue)

        if (abs(rawValue)> threshold):
            count = count + 1
        time.sleep(200)




if __name__ == "__main__":
    zeroLevel = calibration()

    # for x in range (10):
    #     # board.digital[LED].write(1)
    #     time.sleep(.500)
    #     # board.digital[LED].write(0)
    #     time.sleep(.500)

    while switch==True:
        rawValue = board.analog[AnalogPin].read() - zeroLevel
        print(rawValue)

        if (abs(rawValue)> threshold):
            count = count + 1
        time.sleep(200)
