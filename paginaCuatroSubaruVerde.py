import tkinter as tk
from paginaAcariciar import Acariciar
from paginaCinco import QuintaPagina
from paginaAlimentar import Alimentar
import os 
from pathlib import Path

from paginaAlimentar import Alimentar
from paginaBañar import Bañar
from paginaAcariciar import Acariciar
from paginaDormir import Dormir
from paginaPasear import Pasear
from paginaBaño import Baño
from paginaDormir import Dormir
from paginaSacrificar import Sacrificar

directorioRaiz = Path(__file__).resolve().parent

class CuartaPagina:
    def __init__(self, root): 
        self.main_window = root
        self.main_window.title('ANDOJI')
        self.main_window.geometry('600x300')

        self.right = tk.Frame(self.main_window)
        self.left = tk.Frame(self.main_window)

        self.img = tk.PhotoImage(file=os.path.join(directorioRaiz, 'Imagenes', 'Subaru.png'))
      
        self.canvas = tk.Canvas(self.left, width=290, height=200, bg="green")
        self.canvas.create_image(0, 0, image=self.img, anchor="nw")
        self.label = tk.Label(self.left, text="Subaru")
		
        self.canvas.pack()
        self.label.pack()

  

        self.botonAlimentar = tk. Button(self.right, text = "Alimentar", padx=30, pady=5, command=self.Ventanaalimentar)#.place(x=90,y=0)
        self.botonBañar = tk. Button(self.right, text = "Bañar", padx=41, pady=5, command = self.VentanaBañar)
        self.botonAcariciar = tk. Button(self.right, text = "Acariciar", padx=33, pady=5, command = self.VentanaAcariciar)
        self.botonPasear = tk. Button(self.right, text = "Pasear", padx=39, pady=5, command = self.VentanaPasear)
        self.botonBaño = tk. Button(self.right, text = "Ir al baño", padx=32, pady=5, command = self.VentanaBaño)
        self.botonDormir = tk. Button(self.right, text = "Dormir", padx=38, pady=5, command = self.VentanaDormir)
        self.botonSacrificar = tk. Button(self.right, text = "Sacrificar", padx=33, pady=5, command = self.VentanaSacrificar)

        self.botonAlimentar.pack(side="top")
        self.botonBañar.pack(side="top")
        self.botonAcariciar.pack(side="top")
        self.botonPasear.pack(side="top")
        self.botonBaño.pack(side="top")
        self.botonDormir.pack(side="top")
        self.botonSacrificar.pack(side="top")

        self.right.place(x=450, y=20)
        self.left.place(x=100, y=50)

    def Ventanaalimentar(self):
        self.new_user_window = Alimentar(self.main_window)

    def VentanaBañar(self): 
        self.new_user_window = Bañar(self.main_window)

    def VentanaAcariciar(self): 
        self.new_user_window = Acariciar(self.main_window)

    def VentanaPasear(self): 
        self.new_user_window = Pasear(self.main_window)

    def VentanaBaño(self): 
        self.new_user_window = Baño(self.main_window)

    def VentanaDormir(self):
        self.new_user_window = Dormir(self.main_window)

    def VentanaSacrificar(self): 
        self.new_user_window = Sacrificar(self.main_window)

    def crearVentanaNueva(self):
	    self.new_user_window = QuintaPagina(self.main_window)


if __name__ == '__main__':

	root = tk.Tk()
	my_gui = CuartaPagina(root)
	root.mainloop()