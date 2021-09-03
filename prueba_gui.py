from tkinter import *
import tkinter as tk

from tkinter.ttk import *
import tkinter.ttk as ttk
import time


from pathlib import Path
from datetime import datetime


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)





def start():
    button.pack_forget()
    
    bar.pack(ipady=40)
    bar.pack(fill=NONE, expand=0, side = TOP)#, side = TOP)
    percentLabel.pack(side = BOTTOM, pady=15)
    taskLabel.pack(side = BOTTOM,  pady=10)
    
    GB = 100

    download = 0

    speed = 0.1

    while(download<GB):
        window.update()
        time.sleep(0.05)

        bar['value']+=(speed/GB)*100

        download+=speed
        
        percent.set(str(int((download/GB)*100))+"%")

        text.set(str(download)+"/"+str(GB)+" KM COMPLETADOS")

        window.update_idletasks()



window = tk.Tk()
window.geometry("1440x1024")
window.configure(bg = "#000000")

#centrado variable creo
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)



percent = tk.StringVar()
text = tk.StringVar()

s = Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", 
            foreground='#0de03f', 
            borderwidth=0,
            background='#0de03f')


s.configure('TLabelframe', background='#000000',
borderwidth=0)    


# lf = ttk.LabelFrame(
#     window, style='TLabelframe')
lf = tk.LabelFrame(window, bg='#000000',
highlightthickness = 0, borderwidth=0)
lf.grid(column=0, row=0, padx=20, pady=20)



bar = ttk.Progressbar(lf,
style="red.Horizontal.TProgressbar",
orient=HORIZONTAL,length=600)

bar.pack_forget()

#bar.pack( anchor='center' )
# bar.pack(ipady=40)
# bar.pack(fill=NONE, expand=0, side = TOP)#, side = TOP)




# s.configure("Red.TCheckbutton", background="black",
# foreground='#0de03f',
# font=('Courier New Bold', 24),
# borderwidth=0)



percentLabel = tk.Label(lf,textvariable=percent,
bg = 'black',
borderwidth=0,
font = ("Courier New Bold", 24),
fg='#0de03f')

percentLabel.pack_forget()


taskLabel = tk.Label(lf,textvariable=text,
bg = 'black',
borderwidth=0,
font = ("Courier New Bold", 24),
fg='#0de03f')
taskLabel.pack_forget()




button = tk.Button(lf,text="START",command=start, 
bg = 'black',
borderwidth=0,
font = ("Courier New Bold", 40),
fg='#0de03f')
button.pack(side = BOTTOM)

# button.pack(ipady=40)
# button.pack(fill=BOTH, expand=1, side = TOP)#, side = TOP)



window.mainloop()