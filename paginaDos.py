import tkinter as tk
from tkinter import ttk 
import tkinter.messagebox

from paginaTres import TerceraPagina

class SegundaPagina: 

    def __init__(self, root): 
        self.main_window = tk.Toplevel() 
        self.main_window.title('ANDOJI')
        self.main_window.geometry('600x300')

        self.tab_parent = ttk.Notebook(self.main_window)

        self.frm_bottom = tk.Frame(self.main_window)

        self.tab_subaru = tk.Frame(self.tab_parent)
        self.tab_kaksuka = tk.Frame(self.tab_parent)
        self.tab_pepinillo = tk.Frame(self.tab_parent)

        self.tab_parent.bind('<< Notebook Tabchange >>', self.mostrarTabSeleccionada)
        self.tab_parent.add(self.tab_subaru, text = 'Subaru')
        self.tab_parent.add(self.tab_kaksuka, text = 'Kaksuka')
        self.tab_parent.add(self.tab_pepinillo, text = 'Pepinillo')
        self.tab_parent.pack(expand = 1, fill = 'both')
        self.tab_parent.pack()

        self.CrearMenu()
        self.crearWidgetsSubaru()
        self.crearWidgetsKaksuka()
        self.crearWidgetPepinillo()

    def CrearMenu(self): 
        menu_barra = tk.Menu(self.main_window)

        inicio = tk.Menu(menu_barra, tearoff = 0)
        inicio.add_command(label = 'Volver a la pagina inicial', command = self.regresar)
        inicio.add_separator()
        inicio.add_command(label = 'Salir', command = self.salir)

        ayuda = tk.Menu(menu_barra, tearoff = 0)
        ayuda.add_command(label = 'Mande mensaje')

        menu_barra.add_cascade(label = 'Inicio', menu = inicio)
        menu_barra.add_cascade(label = 'Ayuda', menu = ayuda)

        self.main_window.config(menu = menu_barra)
    
    def mostrarTabSeleccionada(self, event): 
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, 'text')

        if tab_text == 'Subaru': 
            print('Subaru')

        if tab_text == 'Kaksuka': 
            print('kaksuka')

        if tab_text == 'Pepinillo': 
            print('Pepinillo')
            
    def crearWidgetsSubaru(self): 
        self.lbl_title = tk.Label(self.tab_subaru, text = 'SUBARU', font = ('Arial', 25))

        self.btn_nuevo_usuario = tk.Button(self.tab_subaru, text = 'Escoger su pesonaje', command = self.crearVentanaNueva)

        self.lbl_title.pack(padx = 90, pady = 10)
        self.btn_nuevo_usuario.pack(pady = 25)

    def crearWidgetsKaksuka(self): 
        self.lbl_title = tk.Label(self.tab_kaksuka, text = 'KAKSUKA', font = ('Arial', 25))

        self.btn_nuevo_usuario = tk.Button(self.tab_kaksuka, text = 'Escoger su personaje', command = self.crearVentanaNueva)

        self.lbl_title.pack(padx = 90, pady = 10)
        self.btn_nuevo_usuario.pack(pady = 25)

    def crearWidgetPepinillo(self): 
        self.lbl_title = tk.Label(self.tab_pepinillo, text = 'PEPINILLO', font = ('Arial', 25))

        self.btn_nuevo_usuario = tk.Button(self.tab_pepinillo, text = 'Escoger personaje', command = self.crearVentanaNueva)

        self.lbl_title.pack(padx = 90, pady = 10)
        self.btn_nuevo_usuario.pack(pady = 25)

    def crearVentanaNueva(self): 
        self.new_user_window = TerceraPagina(self.tab_parent)

    def salir(self): 
        resultado = tkinter.messagebox.askyesno(title = 'Salir', message = '¿Estas seguro que desea salir?')
        if resultado == True: 
            self.main_window.destroy()

    def regresar(self): 
        resultado2 = tkinter.messagebox.askyesno(title = 'Regresar', message = '¿Esta seguro que desea regresar a la página inicial?')
        if resultado2 == True:
            self.main_window.regresar()

if __name__ == '__main__':

    root = tk.Tk()
    my_segundaPagina = SegundaPagina(root)
    root.mainloop()

    
        


