from tkinter import *
import random as rand

class Main(Frame):
    def __init__(self,root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        global btn1
        btn1 = Button(text='Сгенерировать число', command=self.click_btn)
        btn1.pack()

    def click_btn(self):
        global btn1
        btn1['text'] = str(rand.randint(0, 100))
        

if __name__ == '__main__':
    root = Tk()
    app = Main(root)
    root.title('Генератор случайных чисел')
    root.geometry('800x600')
    app.mainloop()