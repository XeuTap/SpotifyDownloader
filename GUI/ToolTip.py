from tkinter import *
from utils import limit_text_perline


class ToolTip(Frame):
    """Класс всплывающей текстовой подсказки"""
    def __init__(self, master, caller, text=''):
        """caller - вызывающий виджет, text - содержимое подсказки"""
        super().__init__(master)
        self.custom_width = 150
        self.custom_height = 350
        self.caller = caller  # Триггер
        self.offset_x = self.caller.winfo_x() # Положение триггера на виджете
        self.offset_y = self.caller.winfo_y()
        self.tip = Label(self)
        self.text = StringVar()
        redacted_text = limit_text_perline(text) # Отредактированый текст
        self.custom_height = 14 + 14 * redacted_text[1]
        self.text.set(redacted_text[0])
        self.setup()

    def setup(self):
        self.config(width=self.custom_width, height=self.custom_height)
        self.tip.config(textvariable=self.text, bd=1, bg='grey')

        def placer():
            self.tip.place(relx=0, rely=0, relwidth=1, relheight=1,)

        def binder():
            self.bind('<Leave>', self.hide)
        placer()
        binder()

    def show(self):
        """Отображает виджет"""
        self.offset_x = self.caller.winfo_x()
        self.offset_y = self.caller.winfo_y()
        self.place(x=self.offset_x, y=self.offset_y)

    def hide(self, event):
        self.place_forget()
