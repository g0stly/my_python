# Задание 4

import tkinter
import tkinter.messagebox


class MyGUI:
    d = {1: 'Замена масла - $30.00', 2: 'Смазочные работы - $20.00', 3: 'Промывка радиатора - $40.00',
         4: 'Замена жидкости в трансмиссии - $100.00', 5: 'Осмотр - $35.00',
         6: 'Замена глушителя выхлопа - $200.00', 7: 'Перестановка шин - $20.00'}

    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.resizable(False, False)

        self.cb_frame = tkinter.Frame(self.main_window)
        self.btn_frame = tkinter.Frame(self.main_window)

        # вышло не очень читаемо, но места занимает определенно меньше

        for var in MyGUI.d:
            exec('self.cb_var' + str(var) + '= tkinter.IntVar()')
            exec('self.cb_var' + str(var) + '.set(0)')
            exec('self.cb' + str(var) +
                 f' = tkinter.Checkbutton(self.cb_frame, text="{MyGUI.d[var]}", variable=self.cb_var' + str(var) + ')')
            exec('self.cb' + str(var) + '.pack()')

        self.value_button = tkinter.Button(self.btn_frame, text='Показать стоимость', command=self.show_value)
        self.quit_button = tkinter.Button(self.btn_frame, text='Выйти', command=self.main_window.destroy)

        self.value_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.cb_frame.pack()
        self.btn_frame.pack()

        tkinter.mainloop()

    # в этом месте сократить не получилось.
    # не понял, как использовать метод get() внутри exec().

    def show_value(self):

        total = 0

        if self.cb_var1.get() == 1:
            total += 30

        if self.cb_var2.get() == 1:
            total += 20

        if self.cb_var3.get() == 1:
            total += 40

        if self.cb_var4.get() == 1:
            total += 100

        if self.cb_var5.get() == 1:
            total += 35

        if self.cb_var6.get() == 1:
            total += 200

        if self.cb_var7.get() == 1:
            total += 20

        tkinter.messagebox.showinfo('Общая стоимость', f'Ваши затраты = ${total}.00')


my_gui = MyGUI()
