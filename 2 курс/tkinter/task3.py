# Задание 3

import tkinter


class ConverterGUI:

    def __init__(self):


        self.main_window = tkinter.Tk()
        self.main_window.resizable(False, False)

        
        self.top_frame = tkinter.Frame()
        self.mid1_frame = tkinter.Frame()
        self.mid2_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # 1 слой
        
        self.gallon_label = tkinter.Label(self.top_frame, text='Введите количество галлонов:')
        self.gallon_entry = tkinter.Entry(self.top_frame, width=10)

        self.gallon_label.pack(side='left')
        self.gallon_entry.pack(side='right')

        # 2 слой

        self.mile_label = tkinter.Label(self.mid1_frame, text='Введите количество миль:')
        self.mile_entry = tkinter.Entry(self.mid1_frame, width=10)
        
        self.mile_label.pack(side='left')
        self.mile_entry.pack(side='right')
        
        # 3 слой
        
        self.miles_label = tkinter.Label(self.mid2_frame, text='Мили на галлон (MPG) =')
        self.value = tkinter.StringVar()
        self.ans_label = tkinter.Label(self.mid2_frame, textvariable=self.value)
        
        self.miles_label.pack(side='left')
        self.ans_label.pack(side='right')

        # 4 слой (кнопки)
        
        self.calc_button = tkinter.Button(self.bottom_frame, text='Вычислить MPG', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Выйти', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='right')


        self.top_frame.pack()
        self.mid1_frame.pack()
        self.mid2_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop()

        
    def convert(self):

        gallons = float(self.gallon_entry.get())
        miles = float(self.mile_entry.get())

        self.value.set(miles / gallons)



conv = ConverterGUI()
