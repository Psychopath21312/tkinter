from tkinter import *
import random as rand

class Main(Frame):
    def __init__(self,root):
        super().__init__(root)
but1 = Button(text='Сгенерировать число')
but1.place(x=10,y=10)

if __name__ == '__main__':
    root = Tk()
    app = Main(root)
    root.title('Генератор случайных чисел')
    root.geometry('800x600')
    root.mainloop()