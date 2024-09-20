from tkinter import *

class Main(Frame):
    def __init__(self,root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        self.Dx = ''
        self.math = ''

        self.check = Label(text='', width=60, font=('Arial', 12, 'bold'), bg='#d7d7d7')

        self.btn_one = Button(text='1', width=5, height=5, command=self.click_one)
        self.btn_two = Button(text='2', width=5, height=5, command=self.click_two)
        self.btn_three = Button(text='3', width=5, height=5, command=self.click_three)
        self.btn_four = Button(text='4', width=5, height=5, command=self.click_four)
        self.btn_five = Button(text='5', width=5, height=5, command=self.click_five)
        self.btn_six = Button(text='6', width=5, height=5, command=self.click_six)
        self.btn_seven = Button(text='7', width=5, height=5, command=self.click_seven)
        self.btn_eight = Button(text='8', width=5, height=5, command=self.click_eight)
        self.btn_nine = Button(text='9', width=5, height=5, command=self.click_nine)
        self.btn_nil = Button(text='0', width=5, height=5, command=self.click_nil)

        self.btn_sum = Button(text='+', width=7, height=5, command=self.click_sum)
        self.btn_dif = Button(text='-', width=7, height=5, command=self.click_dif)

        self.result = Button(text='=', width=5, height=5, command=self.result_bt)

        self.del_bt = Button(text='<---', width=30, height=5, command=self.del_check)

        self.check.grid(column=2, row=1)
        self.btn_one.grid(column=1, row=2)
        self.btn_two.grid(column=2, row=2)
        self.btn_three.grid(column=3, row=2)
        self.btn_four.grid(column=1, row=3)
        self.btn_five.grid(column=2, row=3)
        self.btn_six.grid(column=3, row=3)
        self.btn_seven.grid(column=1, row=4)
        self.btn_eight.grid(column=2, row=4)
        self.btn_nine.grid(column=3, row=4)
        self.btn_nil.grid(column=1, row=5)
        self.btn_sum.grid(column=2, row=5)
        self.btn_dif.grid(column=3, row=5)
        self.result.grid(column=1, row=6)
        self.del_bt.grid(column=2, row=6)

    def click_one(self):
        if self.math == '0':
            self.Dx = ''; self.math = ''
        self.math += '1'
        self.Dx += '1'
        display = self.Dx
        for i in range(len(self.Dx), 0, -3):
            display = f'{display[:i]} {display[i:]}'
        self.check['text'] = display

    def click_two(self):
        if self.math == '0':
            self.Dx = ''; self.math = ''
        self.math += '2'
        self.Dx += '2'
        display = self.Dx
        for i in range(len(self.Dx), 0, -3):
            display = f'{display[:i]} {display[i:]}'
        self.check['text'] = display

    def click_three(self):
        if self.math == '0':
            self.Dx = ''; self.math = ''
        self.math += '3'
        self.Dx += '3'
        display = self.Dx
        for i in range(len(self.Dx), 0, -3):
            display = f'{display[:i]} {display[i:]}'
        self.check['text'] = display

    def click_four(self):
        if self.math == '0':
            self.Dx = ''; self.math = ''
        self.math += '4'
        self.Dx += '4'
        display = self.Dx
        for i in range(len(self.Dx), 0, -3):
            display = f'{display[:i]} {display[i:]}'
        self.check['text'] = display

    def click_five(self):
        if self.math == '0':
            self.Dx = ''; self.math = ''
        self.math += '5'
        self.Dx += '5'
        display = self.Dx
        for i in range(len(self.Dx), 0, -3):
            display = f'{display[:i]} {display[i:]}'
        self.check['text'] = display

    def click_six(self):
        if self.math == '0':
            self.Dx = ''; self.math = ''
        self.math += '6'
        self.Dx += '6'
        display = self.Dx
        for i in range(len(self.Dx), 0, -3):
            display = f'{display[:i]} {display[i:]}'
        self.check['text'] = display

    def click_seven(self):
        if self.math == '0':
            self.Dx = ''; self.math = ''
        self.math += '7'
        self.Dx += '7'
        display = self.Dx
        for i in range(len(self.Dx), 0, -3):
            display = f'{display[:i]} {display[i:]}'
        self.check['text'] = display

    def click_eight(self):
        if self.math == '0':
            self.Dx = ''; self.math = ''
        self.math += '8'
        self.Dx += '8'
        display = self.Dx
        for i in range(len(self.Dx), 0, -3):
            display = f'{display[:i]} {display[i:]}'
        self.check['text'] = display

    def click_nine(self):
        if self.math == '0':
            self.Dx = ''; self.math = ''
        self.math += '9'
        self.Dx += '9'
        display = self.Dx
        for i in range(len(self.Dx), 0, -3):
            display = f'{display[:i]} {display[i:]}'
        self.check['text'] = display

    def click_nil(self):
        if self.math == '0':
            self.Dx = ''
        self.math += '0'
        self.Dx += '0'
        display = self.Dx
        for i in range(len(self.Dx), 0, -3):
            display = f'{display[:i]} {display[i:]}'
        self.check['text'] = display

    def click_sum(self):
        self.Dx = ''
        if self.math != '':
            self.math += ' + '
            self.check['text'] += ' + '

    def click_dif(self):
        self.Dx = ''
        if self.math != '':
            self.math += ' - '
            self.check['text'] += ' - '

    def result_bt(self):
        self.math = str(eval(self.math))
        resul = self.math
        if int(resul) >= 0:
            for i in range(len(resul), 0, -3):
                resul = f'{resul[:i]} {resul[i:]}'
        elif int(resul) < 0:
            magic = str(int(resul) * -1)
            for i in range(len(magic), 0, -3):
                resul = f'{resul[:i+1]} {resul[i+1:]}'
        self.check['text'] = resul
        self.Dx = resul
        

    def del_check(self):
        self.Dx, self.math = '', ''
        self.check['text'] = ''

if __name__ == '__main__':
    root = Tk()
    root.title('Калькулятор')
    root.geometry('800x700')
    app = Main(root)
    root.resizable(False, False)
    app.mainloop()