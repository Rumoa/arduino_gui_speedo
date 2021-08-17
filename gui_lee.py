from tkinter import *

from tkinter.ttk import *

from pyfirmata import Arduino, util

import time

from multiprocessing import Process
import sys

from lee import *



def arduino_stuff():
    init()
    zeroLevel = calibration()
    mide()

def UI_stuff():
    def start():

        GB = 100

        download = 0

        speed = 2

        while(download<GB):

            time.sleep(0.05)

            bar['value']+=(speed/GB)*100 #read the value of length variable. += total_length

            download+=speed

            percent.set(str(int((download/GB)*100))+"%")

            text.set(str(download)+"/"+str(GB)+" GB completed")

            #umbral.set(threshold) si lo pongo aquí no saldría hasta que le doy a start

            window.update_idletasks()



    window = Tk() #Creo una ventana tk 



    percent = StringVar() #el porcentaje de arriba

    text = StringVar() #el texto de abajo

    umbral = DoubleVar(value=threshold)



    bar = Progressbar(window,orient=HORIZONTAL,length=300) #la barra de progreso

    bar.pack(pady=10) #pady no se lo que es



    percentLabel = Label(window,textvariable=percent).pack() #hago un label para las variables que he dicho antes

    taskLabel = Label(window,textvariable=text).pack()

    umbralLabel = Label(window, textvariable=umbral).pack()



    button = Button(window,text="download",command=start).pack() #esto me permite iniciar

    cerrar = Button(window, text="Quit", command=window.destroy).pack()



    window.mainloop()

if __name__=='__main__':
    p1 = Process(target = arduino_stuff)
    p1.start()
    p2 = Process(target = UI_stuff)
    p2.start()