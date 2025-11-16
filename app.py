import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
import os

from input_grade import Input_grade

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

        self.geometry('320x400')
        self.title('Correc_Cop')
        icon_image = tk.PhotoImage(file='Cocop_ico.png')
        self.iconphoto(True, icon_image)
        #Background
        bg = tk.Label( self, image = icon_image)
        bg.place(x = 0, y = 0)

        # Les buttons

        # Un cadre pour les 2 premiers bouttons
        frame = ttk.Frame(self)
        
        self.new_DS_button = ttk.Button(frame,
                text='Nouveau DS',
                command=self.new_DS)
        
        self.load_DS_button = ttk.Button(frame,
                text='Charger DS',
                command=self.load_DS)
        
        self.report_button = ttk.Button(self,
                text='BILAN',
                command=self.report)
        self.report_button.state(['disabled'])
        
        self.load_class_button = ttk.Button(self,
                text='Charger une classe',
                command=self.load_class)
        
        self.input_button = ttk.Button(self,
                text='Saisir les notes',
                command=self.input)
        self.input_button.state(['disabled'])

        listbox = tk.Listbox(self,
                            listvariable=self.class_list,
                            height=6,
                            selectmode=tk.BROWSE,
                            )
        
        v_scrollbar = ttk.Scrollbar(self,
                                    orient=tk.VERTICAL,
                                    command=listbox.yview
                                    )
        listbox['yscrollcommand'] = v_scrollbar.set
        listbox.bind('<<ListboxSelect>>', self.pupil_selected) #pour autoriser à saisir les notes si eleve selectionné
        listbox.bind('<Double-1>', self.input) # pour lancer la saisie de snotes par dble click sur nom
        label_eleve = ttk.Label(self, 
                            text='Élève:',
                            font = ("Palatino",14)
                        )
        label_DS = ttk.Label(self, 
                            textvariable = self.current_DS_affichage,
                            font = ("Palatino",14)
                        )
        
        #Placement des bouttons
        #Plus tard peut être sur une grille
        
        
        label_DS.pack(expand=True)
        frame.pack(expand=True)
        self.new_DS_button.pack(expand=True,side= tk.LEFT)
        self.load_DS_button.pack(expand=True)
        self.report_button.pack(expand=True)
        self.load_class_button.pack(expand=True)
        label_eleve.pack(expand = False, side=tk.LEFT,padx=10)
        listbox.pack(expand = False,side=tk.LEFT,pady=10)
        v_scrollbar.pack(side=tk.LEFT, fill=tk.Y,pady=10)
        self.input_button.pack(expand=True)
        

    #charge la config
    def load_config(self):
        try:
            with open('config.json') as fich:
                self.params  = json.load(fich)
        except:
            print("Pas de fichier config.cfg ou problème de lecture")
        self.class_list=tk.Variable(value=[])
        self.load_class(open_window = False)
        self.current_DS = self.params["last_DS"]
        self.current_DS_affichage = tk.Variable ( value = f"DS en cours d'édition: {self.current_DS}")

    # Les actions
    def new_DS(self):
        path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"),('All files', '*.*')),
                                              initialdir = os.path.realpath(os.path.dirname(__file__)))
        self.current_DS = os.path.basename(path)
        self.current_DS_affichage.set(f"DS en cours d'édition: {self.current_DS}")

    def load_DS(self):
        window = Window(self)
        window.grab_set()
    def report(self):
        window = Window(self)
        window.grab_set()
    def load_class(self,open_window = True):
        #select path
        if open_window:
            #Select file
            path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"),('All files', '*.*')),
                                              initialdir = os.path.realpath(os.path.dirname(__file__))) #initialdir=Path(sys.executable).parent
            if not(path): #If cancel is clicked
                return #Do nothing
        else:
            path = self.params["class_file"]
        with open(path,encoding='utf-8') as fichier:
            liste =[]
            for line in fichier:
                liste.append(line.strip('\n'))
            self.class_list.set(liste)
    def pupil_selected(self,event):
        #Alors on peut saisir les notes
        self.input_button.state(['!disabled'])
    def input(self,event=''):
        window = Input_grade(self)
        window.grab_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()