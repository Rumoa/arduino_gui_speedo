from pyfirmata import Arduino, util
import time

class Placa:
    def __init__(self):
        self.AnalogPin = 0
        self.tyrelength = 0.2
        self.threshold = 0.05
        self.counts = 0
        self.board = Arduino("COM3")
        self.zeroLevel = 0
        self.switch = True
        self.length = 0
        self.wait = 0.05
        self.time_write = 1.5

    def init(self):
        it = util.Iterator(self.board)
        it.start()
        self.board.analog[self.AnalogPin].enable_reporting()

    def calibration(self):
        print("Calibrando...")
        time.sleep(1)
        self.zeroLevel = self.board.analog[self.AnalogPin].read()
        time.sleep(1)
        print("Zero level = ", self.zeroLevel)   

    def mide(self, verbose=False):
        t0 = time.time()
        while self.switch==True:
            rawValue = self.board.analog[self.AnalogPin].read() - self.zeroLevel
            time.sleep(self.wait)
            if (abs(rawValue)> self.threshold):
                self.counts = self.counts + 1
                self.total_length()
                self.escribe()
                if verbose==True:
                    print(self.counts)
                    print(self.length)
                
                
            
    def escribe(self):
        with open("sample.txt", "a") as file_object:
            # Append 'hello' at the end of file
            file_object.write("\n" + str(self.length))

    def total_length(self):
        self.length = self.counts*self.tyrelength
        

        

if __name__=="__main__":
    uno = Placa()
    uno.init()
    uno.calibration()
    uno.mide()    