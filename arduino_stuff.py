from pyfirmata import Arduino, util
import time
import os


class Placa:
    def __init__(self):
        self.AnalogPin = 0
        self.tyrelength = 2.04 #meters
        self.threshold = 0.06
        self.counts = 0
        self.board = Arduino("COM3")
        self.zeroLevel = 0
        self.switch = True
        self.length = 0
        self.wait = 0.02
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
        if os.path.exists("length.txt"):
            os.remove("length.txt")
        self.inicia_file()      

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
                    print(rawValue)
                
                
    def inicia_file(self):
        with open("length.txt", "a") as file_object:
            
            file_object.write("0"+ "\n")

    def escribe(self):
        with open("length.txt", "a") as file_object:
            # Append 'hello' at the end of file
            file_object.write(str(self.length)+ "\n"  )

    def total_length(self):
        self.length = self.counts*self.tyrelength
        

        

if __name__=="__main__":
    uno = Placa()
    uno.init()
    uno.calibration()
    uno.mide(verbose=True)    