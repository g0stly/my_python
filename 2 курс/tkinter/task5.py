# Задание 5

import tkinter
from tkinter import messagebox as mb


class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.resizable(False, False)

        self.rd_btn_frame = tkinter.Frame(self.main_window)
        self.entry_frame = tkinter.Frame(self.main_window)
        self.cmn_btn_frame = tkinter.Frame(self.main_window)

        # 1 слой

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.rd1_btn = tkinter.Radiobutton(self.rd_btn_frame, text='Дневное время (6:00 - 17:59)',
                                           variable=self.radio_var, value=1)
        self.rd2_btn = tkinter.Radiobutton(self.rd_btn_frame, text='Вечернее время (18:00 - 23:59)',
                                           variable=self.radio_var, value=2)
        self.rd3_btn = tkinter.Radiobutton(self.rd_btn_frame, text='Непиковый период (00:00 - 5:59)',
                                           variable=self.radio_var, value=3)

        self.rd1_btn.pack()
        self.rd2_btn.pack()
        self.rd3_btn.pack()

        # 2 слой

        self.entry_name = tkinter.Label(self.entry_frame, text='Введите количество минут:')
        self.entry = tkinter.Entry(self.entry_frame)

        self.entry_name.pack(side='left')
        self.entry.pack(side='right')

        # 3 слой

        self.run_btn = tkinter.Button(self.cmn_btn_frame, text='Показать стоимость', command=self.show)
        self.quit_btn = tkinter.Button(self.cmn_btn_frame, text='Выйти', command=self.main_window.destroy)

        self.run_btn.pack(side='left')
        self.quit_btn.pack(side='right')

        self.rd_btn_frame.pack()
        self.entry_frame.pack()
        self.cmn_btn_frame.pack()

        tkinter.mainloop()

    def show(self):
        values = {1: 10, 2: 12, 3: 5}

        mb.showinfo('Общая стоимость',
                                    f'Ваши затраты = ${values[self.radio_var.get()] * int(self.entry.get()) * 0.01}')


my_gui = MyGUI()