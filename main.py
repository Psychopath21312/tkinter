from tkinter import *
import random as rand

class Main(Frame):
    def __init__(self,root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        self.check = Label(text='')

        self.btn_one = Button(text='1', command=self.click_one)
        self.btn_two = Button(text='2', command=self.click_two)
        self.btn_three = Button(text='3', command=self.click_three)
        self.btn_four = Button(text='4', command=self.click_four)
        self.btn_five = Button(text='5', command=self.click_five)
        self.btn_six = Button(text='6', command=self.click_six)
        self.btn_seven = Button(text='7', command=self.click_seven)
        self.btn_eight = Button(text='8', command=self.click_eight)
        self.btn_nine = Button(text='9', command=self.click_nine)
        self.btn_nil = Button(text='0', command=self.click_nil)

        self.btn_sum = Button(text='+', command=self.click_sum)
        self.btn_dif = Button(text='-', command=self.click_dif)

        self.result = Button(text='=', command=self.result_bt)

        self.del_bt = Button(text='<---', command=self.del_check)

        self.check.pack()
        self.btn_one.pack()
        self.btn_two.pack()
        self.btn_three.pack()
        self.btn_four.pack()
        self.btn_five.pack()
        self.btn_six.pack()
        self.btn_seven.pack()
        self.btn_eight.pack()
        self.btn_nine.pack()
        self.btn_nil.pack()
        self.btn_sum.pack()
        self.btn_dif.pack()
        self.result.pack()
        self.del_bt.pack()

    def click_one(self):
        self.check['text'] += '1'

    def click_two(self):
        self.check['text'] += '2'

    def click_three(self):
        self.check['text'] += '3'

    def click_four(self):
        self.check['text'] += '4'

    def click_five(self):
        self.check['text'] += '5'

    def click_six(self):
        self.check['text'] += '6'

    def click_seven(self):
        self.check['text'] += '7'

    def click_eight(self):
        self.check['text'] += '8'

    def click_nine(self):
        self.check['text'] += '9'

    def click_nil(self):
        self.check['text'] += '0'

    def click_sum(self):
        if self.check['text'] != '':
            self.check['text'] += ' + '

    def click_dif(self):
        if self.check['text'] != '':
            self.check['text'] += ' - '

    def result_bt(self):
        self.check['text'] = str(eval(self.check['text']))

    def del_check(self):
        self.check['text'] = ''
        
if __name__ == '__main__':
    root = Tk()
    app = Main(root)
    root.title('Калькулятор')
    root.geometry('800x600')
    app.mainloop()