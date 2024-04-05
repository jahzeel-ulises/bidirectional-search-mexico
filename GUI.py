import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from montion import motion

items = ['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 'Chiapas', 'Chihuahua', 'Ciudad de Mexico', 'Coahuila', 'Colima', 'Durango', 'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco', 'Mexico', 'Michoacan', 'Morelos', 'Nayarit', 'Nuevo Leon', 'Oaxaca', 'Puebla', 'Queretaro', 'Quintana Roo', 'San Luis Potosi', 'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatan', 'Zacatecas']

class Window():
    def __init__(self):
        #--------------------------Init window------------------------
        self.window=tk.Tk()
        self.window.title("Busqueda Bidireccional")
        self.window.resizable(width=False,height=False)
        #------------Header------------------------------------
        self.labelframe1=ttk.LabelFrame(self.window, text="Ingresar ciudad inicio y ciudad destino")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)

        #----------------Add components------------------------
        self.add_components()
        self.add_menu()

        self.window.mainloop()

    def add_components(self)->None:
        """Add all main widgets to the main window.

        Args:
            None
        Returns:
            None
        """
        #--------------------------Combox Initial-------------------------
        self.label1=ttk.Label(self.labelframe1, text="Ciudad inicio:")
        self.label1.grid(column=0, row=0, padx=5, pady=5, sticky="e")
        self.strInitial=tk.StringVar()
        self.combobox1=ttk.Combobox(self.labelframe1,state="readonly",values=items, textvariable=self.strInitial)
        self.combobox1.grid(column=1, row=0, padx=5, pady=5)

        #--------------------------Combox Final-------------------------
        self.label2=ttk.Label(self.labelframe1, text="Ciudad destino:")
        self.label2.grid(column=0, row=1, padx=5, pady=5, sticky="e")
        self.strFinal=tk.StringVar()
        self.combobox2=ttk.Combobox(self.labelframe1,state="readonly",values=items, textvariable=self.strFinal)
        self.combobox2.grid(column=1, row=1, padx=5, pady=5)

        #------------------Go Button--------------------------------------
        self.boton1=ttk.Button(self.labelframe1, text="Animar", command=self.animate)
        self.boton1.grid(column=1, row=2, padx=5, pady=5, sticky="we")

    def add_menu(self):
        """Create the top menu.

        Args:
            None
        Returns:
            None
        """
        self.menubar1 = tk.Menu(self.window)
        self.window.config(menu=self.menubar1)
        self.opciones1 = tk.Menu(self.menubar1, tearoff=0)
        self.opciones1.add_command(label="Acerca de...", command=self.about)
        self.menubar1.add_cascade(label="Opciones", menu=self.opciones1)    

    def animate(self)->None:
        """Validate the entrys of the combobox and start the animation if they´re correct.

        Args:
            None
        Returns:
            None
        """
        if self.strInitial.get()=="" or self.strFinal.get()=="":
            messagebox.showerror("Cuidado","No puede dejar los cuadros de entrada vacíos")
        elif self.strInitial.get()==self.strFinal.get():
            messagebox.showerror("Cuidado","Los estados inicial y destino son el mismo")
        else:
            motion(self.strInitial.get(),self.strFinal.get())

    def about(self):
        messagebox.showinfo("Informacion", "Desarrollado por Jahzeel Ulises Mendez Diaz\nClase: Busqueda de Soluciones e Inferencia Bayesiana.")

Window()

