# Задание 1

import tkinter


class MyGUI:

    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.resizable(False, False)
        
        
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        
        self.info = tkinter.StringVar()
        self.info_label = tkinter.Label(self.top_frame,textvariable=self.info, justify='left')
        self.info_label.pack(side='left')
        
        
        self.show_button = tkinter.Button(self.bottom_frame, text='Показать инфо', command=self.show)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Выйти', command=self.main_window.destroy)
 

        self.quit_button.pack(side='right')
        self.show_button.pack(side='left')
        
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        
        tkinter.mainloop()
    
    
    def show(self):
        self.info.set('Стивен Маркус\n274 Бейли\nУэйнзвилль, Северная Каролина 27999')
        

my_gui = MyGUI()
