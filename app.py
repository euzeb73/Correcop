import tkinter as tk
from tkinter import ttk

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Eleve')

        ttk.Button(self,
                text='Close',
                command=self.destroy).pack(expand=True)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.load_config()

        self.geometry('300x200')
        self.title('Correc_Cop')
        icon_image = tk.PhotoImage(file='Cocop_ico.png')
        self.iconphoto(True, icon_image)

        # Les buttons
        self.new_DS_button = ttk.Button(self,
                text='Nouveau DS',
                command=self.new_DS)
        
        self.new_DS_button.state(['disabled'])
        self.load_DS_button = ttk.Button(self,
                text='Charger DS',
                command=self.load_DS)
        
        self.report_button = ttk.Button(self,
                text='BILAN',
                command=self.report)
        
        self.load_class_button = ttk.Button(self,
                text='Charger une classe',
                command=self.input)
        
        self.input_button = ttk.Button(self,
                text='Saisir les notes',
                command=self.input)

        listbox = tk.Listbox(self,
                            listvariable=self.class_list,
                            height=3,
                            selectmode=tk.BROWSE,
                            )
        
        v_scrollbar = ttk.Scrollbar(self,
                                    orient=tk.VERTICAL,
                                    command=listbox.yview
                                    )
        listbox['yscrollcommand'] = v_scrollbar.set
        label = ttk.Label(self, 
                            text='Élève:'
                        )
        
        #Placement des bouttons
        self.new_DS_button.pack(expand=True)
        self.load_DS_button.pack(expand=True)
        self.report_button.pack(expand=True)
        self.load_class_button.pack(expand=True)
        self.input_button.pack(expand=True)
        label.pack(expand = False, side=tk.LEFT,padx=10)
        listbox.pack(expand = False,side=tk.LEFT)
        v_scrollbar.pack(side=tk.LEFT)

    #chage la config
    def load_config(self):
        try:
            fich=open('config.cfg')
            self.class_list=[]
            for line in fich:
                self.class_list.append(line)
            self.class_list=tk.Variable(self.class_list)
        except:
            "Pas de fichier config.cfg"
        
        

    # Les actions
    def new_DS(self):
        window = Window(self)
        window.grab_set()
    def load_DS(self):
        window = Window(self)
        window.grab_set()
    def report(self):
        window = Window(self)
        window.grab_set()
    def load_class(self):
        window = Window(self)
        window.grab_set()
    def input(self):
        window = Window(self)
        window.grab_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()