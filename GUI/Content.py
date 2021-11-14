from tkinter import Frame, Label, Button, S

import requests

from GUI.BottBar import BottBar
from GUI.PlaylistHolder import PlaylistHolder
from spotify import auth
from GUI.ToolTip import ToolTip
from GUI.Settings import Settings


class Content(Frame):
	def __init__(self, master):
		super().__init__(master)
		self.master = master
		self.bar = BottBar(master, self)  # Нижние кнопки
		self.playlist = PlaylistHolder(self.master, self)  # Ассоциация фрейма с плейлистом
		self.settings = Settings(master, self)

		self.title = Label(self)
		self.do_b = Button(self)

		self.setup()
		self.place(relx=0, rely=0, relwidth=1, relheight=1)

	def do_auth(self):
		try:
			auth()
			self.do_b.configure(text="Authorized")
		except requests.exceptions.ConnectionError:
			print('Internet Troubles, try again')
			self.do_b.configure(text='Internet Troubles, try again')

	def setup(self):
		"""Метод для конфигурации виджетов"""

		def placer():
			self.do_b.place(relx=.35, rely=.8, relwidth=.3)
			self.title.place(relx=.5, rely=.2, relwidth=.8, anchor=S)

		self.do_b.configure(text="Authorize", font='Times 12', command=self.do_auth)
		self.title.config(text='Spotify Parser', fg='red', font='Times 18')
		placer()

	def bar_lift(self, event=0):
		"""Обертка для поднятия виджета"""
		if not event == 0:
			self.bar.lift()
		else:
			print('Runs only by event')

	def show_playlist(self):
		"""Функция для отображения списка плейлистов"""
		self.master.bind('<<AlwaysOnTop>>', self.bar_lift)  # Эвент должен вызываться при каждой смене фрейма
		self.playlist.place(relx=0, rely=0, relheight=1, relwidth=1)
		self.playlist.lift()
		self.bar.lift()

	def show_home(self):
		self.lift()
		self.bar.lift()

	def show_settings(self):
		self.master.bind('<<AlwaysOnTop>>', self.bar_lift)  # Эвент должен вызываться при каждой смене фрейма
		self.settings.place(relx=0, rely=0, relheight=.92, relwidth=1)
		self.settings.lift()
		self.bar.lift()
