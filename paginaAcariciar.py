import tkinter as tk
import os 
from pathlib import Path

directorioRaiz = Path(__file__).resolve().parent

class Acariciar:
    def __init__(self, root): 
        self.main_window = tk.Toplevel() 
        self.main_window.title('ANDOJI')
        self.main_window.geometry('200x150')

        self.img = tk.PhotoImage(file=os.path.join(directorioRaiz, 'Imagenes', 'Acariciar.png'))

        self.canvas = tk.Canvas(self.main_window, width=90, height=90, bg="green")
        self.canvas.create_image(0, 0, image=self.img, anchor="nw")
        self.label = tk.Label(self.main_window, text="Esta acariciando a pepinillo ...")
		
        self.canvas.pack()
        self.label.pack()


if __name__ == '__main__':

	root = tk.Tk()
	my_gui = Acariciar(root)
	root.mainloop()