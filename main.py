from tkinter import *

class Main(Frame):
    def __init__(self,root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        self.hand = ''

        self.check = Label(text='', width=60, height='4', font=('Arial', 12, 'bold'), bg='#d7d7d7')

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
        self.hand += '1'
        one = self.hand
        for i in range(len(one)+1, 1, -1):
            if i % 3 == 0:
                one = f'{one[:i]} {one[i:]}'
        self.check['text'] = one

    def click_two(self):
        self.hand += '2'
        two = self.hand
        for i in range(len(two)+1, 1, -1):
            if i % 3 == 0:
                two = f'{two[:i]} {two[i:]}'
        self.check['text'] = two

    def click_three(self):
        self.hand += '3'
        three = self.hand
        for i in range(len(three)+1, 1, -1):
            if i % 3 == 0:
                three = f'{three[:i]} {three[i:]}'
        self.check['text'] = three

    def click_four(self):
        self.hand += '4'
        four = self.hand
        for i in range(len(four)+1, 1, -1):
            if i % 3 == 0:
                four = f'{four[:i]} {four[i:]}'
        self.check['text'] = four

    def click_five(self):
        self.hand += '5'
        five = self.hand
        for i in range(len(five)+1, 1, -1):
            if i % 3 == 0:
                five = f'{five[:i]} {five[i:]}'
        self.check['text'] = five

    def click_six(self):
        self.hand += '6'
        six = self.hand
        for i in range(len(six)+1, 1, -1):
            if i % 3 == 0:
                six = f'{six[:i]} {six[i:]}'
        self.check['text'] = six

    def click_seven(self):
        self.hand += '7'
        seven = self.hand
        for i in range(len(seven)+1, 1, -1):
            if i % 3 == 0:
                seven = f'{seven[:i]} {seven[i:]}'
        self.check['text'] = seven

    def click_eight(self):
        self.hand += '8'
        eight = self.hand
        for i in range(len(eight)+1, 1, -1):
            if i % 3 == 0:
                eight = f'{eight[:i]} {eight[i:]}'
        self.check['text'] = eight

    def click_nine(self):
        self.hand += '9'
        nine = self.hand
        for i in range(len(nine)+1, 1, -1):
            if i % 3 == 0:
                nine = f'{nine[:i]} {nine[i:]}'
        self.check['text'] = nine

    def click_nil(self):
        self.hand += '0'
        nil = self.hand
        for i in range(len(nil)+1, 1, -1):
            if i % 3 == 0:
                nil = f'{nil[:i]} {nil[i:]}'
        self.check['text'] = nil

    def click_sum(self):
        if self.hand != '':
            self.hand += ' + '
            self.check['text'] += ' + '

    def click_dif(self):
        if self.hand != '':
            self.hand += ' - '
            self.check['text'] += ' - '

    def result_bt(self):
        self.hand = str(eval(self.hand))
        resul = self.hand
        for i in range(len(resul)+1, 1, -1):
            if i % 3 == 0:
                resul = f'{resul[:i]} {resul[i:]}'
                self.check['text'] = resul

    def del_check(self):
        self.check['text'] = ''

if __name__ == '__main__':
    root = Tk()
    root.title('Калькулятор')
    root.geometry('800x600')
    app = Main(root)
    app.mainloop()