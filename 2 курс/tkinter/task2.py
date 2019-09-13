# Задание 2

import tkinter


class MyGUI:

    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.resizable(False, False)
        
        
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        
        self.side = tkinter.StringVar()
        self.side_label = tkinter.Label(self.top_frame, textvariable=self.side)
        self.side_label.pack()
        
        
        self.btn1 = tkinter.Button(self.bottom_frame, text='sinister', command=lambda: self.fun(1))
        self.btn2 = tkinter.Button(self.bottom_frame, text='dexter', command=lambda: self.fun(2))
        self.btn3 = tkinter.Button(self.bottom_frame, text='medium', command=lambda: self.fun(3))
        
        self.btn1.pack(side='left')
        self.btn2.pack(side='left')
        self.btn3.pack(side='left')
        
        
        self.top_frame.pack()
        self.bottom_frame.pack()

        
        tkinter.mainloop()
        
        
    def fun(self, i):
        outputs = {1 : 'левый', 2 : 'правый', 3 : 'центральный'}
        self.side.set(outputs[i])

my_gui = MyGUI()
