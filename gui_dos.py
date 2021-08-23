import clase
from tkinter import *
from tkinter.ttk import *




import multiprocessing
import sys


c_total = 200




def UI_stuff():
    def start():

        c_total = 100

        download = 0

        speed = 2

        while(count<c_total):

            time.sleep(0.05)

            bar['value']+=(count/c_total)*100 #read the value of length variable. += total_length

            download+=speed

            percent.set(str(int((download/c_total)*100))+"%")

            text.set(str(download)+"/"+str(c_total)+" counts completed")

            #umbral.set(threshold) si lo pongo aquí no saldría hasta que le doy a start

            window.update_idletasks()



    window = Tk() #Creo una ventana tk 



    percent = StringVar() #el porcentaje de arriba

    text = StringVar() #el texto de abajo

    umbral = DoubleVar(value=threshold)
    cuentas_ui = IntVar(value = count)



    bar = Progressbar(window,orient=HORIZONTAL,length=300) #la barra de progreso

    bar.pack(pady=10) #pady no se lo que es



    percentLabel = Label(window,textvariable=percent).pack() #hago un label para las variables que he dicho antes

    taskLabel = Label(window,textvariable=text).pack()

    umbralLabel = Label(window, textvariable=umbral).pack()

    countLabel = Label(window, textvariable=cuentas_ui).pack()



    button = Button(window,text="download",command=start).pack() #esto me permite iniciar

    cerrar = Button(window, text="Quit", command=window.destroy).pack()



    window.mainloop()