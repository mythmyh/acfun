from tkinter import ttk
from tkinter import *
import time
root= Tk()
root.columnconfigure(0,weight=1)
p=ttk.Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
p['maximum']=100
p['value']=0
p.grid(column=0,row=1)
p.setvar('20')
w,h=500,300
jbc=StringVar()
ttk.Entry(root,textvariable=jbc).grid(column=0,row=2)
def start():
    print(jbc.get())
    for i in range(100):
        p['value'] += 2.5
        p.update()
        if i==50:
            p.destroy()
            ttk.Label(text='下载完成').grid(column=0,row=0)
            break
        time.sleep(0.5)

ttk.Button(text='hello',command=start).grid(column=0,row=0)
root.geometry('{}x{}'.format(w,h))
#root.mainloop()
t = 100%202
print(t)
