
from logging import RootLogger
from optparse import TitledHelpFormatter
import tkinter as tk

from paginaDos import SegundaPagina

class paginaUno:

	def __init__(self, root):
		
		self.main_window = root
		self.main_window.title("ANDOJI")
		self.main_window.geometry("300x300")
		#self.main_window.iconbitmap(".\Imagenes\lucha.ico")
		self.main_window.resizable(False, False)


		self.top = tk.Frame(self.main_window)
		self.mid = tk.Frame(self.main_window)
		self.bottom = tk.Frame(self.main_window)

		self.titulo = tk.Label(self.top, text='Bienvenido a ANDOJI!', font="Helvetica 15 bold")


		self.botonInicio = tk.Button(self.mid, text = "INICIO", padx=250, pady=25, bg= "SteelBlue2", command = self.crearVentanaNueva)
		self.botonSalida = tk.Button(self.bottom, text="Salir", padx=50, pady=15, command=root.destroy)

		self.botonInicio.pack(padx=100, pady=40)
		self.botonSalida.pack(side="bottom")
		self.titulo.pack(side = "top")

		self.top.pack()
		self.mid.pack()
		self.bottom.pack()
	
	def crearVentanaNueva(self):
		self.new_user_window = SegundaPagina(self.main_window)
		
if __name__ == '__main__':

	root = tk.Tk()
	my_gui = paginaUno(root)
	root.mainloop()
