from tkinter import *
from utils import save_cfg, load_cfg, create_cfg


class Settings(Frame):
    def __init__(self, master, parent):
        super().__init__(master)
        self.save_log_fr = Frame(self)
        self.save_log_l = Label(self.save_log_fr)
        self.save_log_box = Checkbutton(self.save_log_fr)
        self.save_log_check = IntVar()
        self.dumped = load_cfg()

        self.load_default_b = Button(self)

        self.submit_b = Button(self)
        self.load_settings()
        self.setup()

    def save_settings(self, event=0):
        dic = {
            'save_logs': self.save_log_check.get()
        }
        save_cfg(dic)

    def load_settings(self):
        self.dumped = load_cfg()
        self.save_log_check.set(self.dumped['save_logs'])

    def load_defaults(self):
        create_cfg()
        self.load_settings()

    def setup(self):
        self.config()
        self.save_log_l.config(text='Сохранять Логи')
        self.save_log_box.config(variable=self.save_log_check)
        self.submit_b.config(text='Применить', command=self.save_settings)
        self.load_default_b.config(text='По Умолчанию', command=self.load_defaults)

        def placer():
            self.save_log_fr.pack(padx=25, pady=10, side=TOP, anchor=SW)
            self.save_log_l.pack(side=LEFT)
            self.save_log_box.pack(side=RIGHT)
            self.submit_b.pack(side=BOTTOM)
            self.load_default_b.pack(side=BOTTOM, anchor=NE)

        def binder():
            pass

        placer()
        binder()
