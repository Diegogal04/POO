import tkinter as tk


class TerceraPagina:

	def __init__(self, root):
		
		self.main_window = root
		self.main_window.title("ANDOJI")
		self.main_window.geometry("300x300")
		self.main_window.iconbitmap(".\Imagenes\lucha.ico")
		self.main_window.resizable(False, False)

