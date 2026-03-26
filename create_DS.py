import tkinter as tk
from tkinter import ttk
PARTIES = ['I','II','III','IV','V','VI','VII','VIII','IX','X']
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

class Noeud():
    def __init__(self,parent,name,data = None):
        self.parent = parent
        self.children = []
        self.name = name
        self.data = data # ça peut être le barême
    def add_child(self,child):
        self.children.append(child)
        child.parent = self
    def create_child(self, name, data = None):
        child = Noeud(self,name,data)
        self.children.append(child)
    def rmv_child(self,child):
        if child in self.children:
            self.children.remove(child)
        else:
            print("le noeud à enlever n'existe pas")

class Arbre():
    def __init__(self):
        self.root = Noeud(parent=None,name = "Root")
    def print(self):
        self.parcours_print(self.root,0)
    def parcours_print(self,noeud : Noeud,profondeur):
        if noeud.data is not None:
            data = f"sur {noeud.data} points"
        else:
            data = ""
        if profondeur > 1:
            joli="|   "*(profondeur-1)
        else:
            joli=""
        if profondeur>0:
            print(joli+noeud.name+" "+data)
        if noeud.children:
            for child in noeud.children:
                self.parcours_print(child,profondeur+1)
    def get_question_list(self):
        return self.parcours_enprof(self.root)
    def parcours_enprof(self,noeud: Noeud):
        if noeud.children:
            liste=[]
            for child in noeud.children:
                liste.extend(self.parcours_enprof(child))
            return liste     
        else:
            return [noeud.name]





class Create_DS(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('900x250')
        self.title('Nouveau DS')
        self.validate_DS_button = ttk.Button(self,
                text='Valider',
                command=self.export_tree)
        self.validate_DS_button.pack(expand=True,pady=5,side=tk.BOTTOM)
        #Le nb de parties
        frame = tk.Frame(self)
        label = tk.Label(frame,text='Nombre de parties  ',font=("Palatino",14))
        self.n_parties = tk.StringVar(value = 1)
        self.choose_nparties = ttk.Spinbox(frame,from_=1,to=10,
                                           textvariable = self.n_parties,
                                           wrap = True,
                                           command = self.init_parties)
        label.pack(side=tk.LEFT)
        self.choose_nparties.pack(expand=True)
        frame.pack()

        self.spinbox_parties_list=[]
        self.spinbox_exos_list=[]
        self.label_parties_list=[]
        self.label_exos_list=[]

        self.cadre_parties=tk.Frame(self)
        titre = ttk.Label(self.cadre_parties,text="Nombre d'exos par partie ",font=("Palatino",14))
        titre.pack(pady=5,side=tk.TOP)

        self.cadre_exos=tk.Frame(self)
        titre = ttk.Label(self.cadre_exos,text="Nombre de questions par exo ",font=("Palatino",14))
        titre.pack(pady=5)
        
        sep = ttk.Separator(self, orient=tk.HORIZONTAL)
        sep.pack(side=tk.TOP, fill=tk.X, pady=5)
        self.cadre_parties.pack()
        sep = ttk.Separator(self, orient=tk.HORIZONTAL)
        sep.pack(side=tk.TOP, fill=tk.X, pady=5)
        self.cadre_exos.pack()
        self.init_parties()
        
    def init_parties(self):
        
        for i,spinbox in enumerate(self.spinbox_parties_list):
            spinbox.destroy()
            self.label_parties_list[i].destroy()
        self.spinbox_parties_list = []
        self.label_parties_list=[]
        self.nb_exos=[]
        for i in range(int(self.n_parties.get())):
            val = tk.StringVar(value=1)
            self.nb_exos.append(val)
            self.spinbox_parties_list.append(ttk.Spinbox(self.cadre_parties,from_=1,to=10,
                                           textvariable = val,
                                           wrap = True,
                                           width = 3,
                                           command = self.init_exos))
            self.label_parties_list.append(ttk.Label(self.cadre_parties,text=PARTIES[i]+' ',font=("Palatino",14)))
        for i,spinbox in enumerate(self.spinbox_parties_list):
            self.label_parties_list[i].pack(side=tk.LEFT,fill = None,padx=5)#,side=tk.LEFT
            spinbox.pack(side=tk.LEFT,fill = None,padx=1)#side=tk.BOTTOM
        self.cadre_parties.pack()
        self.init_exos()
    def init_exos(self):
        for i,spinbox in enumerate(self.spinbox_exos_list):
            spinbox.destroy()
            self.label_exos_list[i].destroy()
        self.spinbox_exos_list = []
        self.label_exos_list=[]
        for num_partie,spinbox in enumerate(self.spinbox_parties_list):
            for j in range(int(spinbox.get())):
                val = tk.StringVar(value=1)
                self.label_exos_list.append(ttk.Label(self.cadre_exos,text=PARTIES[num_partie]+  f' {j+1})',font=("Palatino",14)))
                self.spinbox_exos_list.append(ttk.Spinbox(self.cadre_exos,from_=1,to=len(ALPHABET),
                                           textvariable = val,
                                           width = 3,
                                           wrap = True))
        for i,spinbox in enumerate(self.spinbox_exos_list):
            self.label_exos_list[i].pack(side=tk.LEFT,fill = None,padx=5)
            spinbox.pack(side=tk.LEFT,fill = None,padx=1)
    def export_tree(self):
        arbre = Arbre()
        for i in range(int(self.n_parties.get())):
            arbre.root.create_child(PARTIES[i])
        for i in range(len(self.nb_exos)): #liste du nb d'exos par partie
            partie = arbre.root.children[i]
            for j in range(int(self.nb_exos[i].get())): #nb d'exos de la partie i
                partie.create_child(f"{j+1}.")
        offset = 0 # pour se décaler dans la liste des exos en fonction des parties
        for i in range(len(self.nb_exos)): #liste du nb d'exos par partie
            partie = arbre.root.children[i]
            nb_exo_partie = int(self.nb_exos[i].get())
            for j in range(nb_exo_partie):
                exo = partie.children[j]
                nb_questions = int(self.spinbox_exos_list[j+offset].get())
                for k in range(nb_questions):
                    exo.create_child(ALPHABET[k]+")")
            offset += nb_exo_partie
        arbre.print()


if __name__ == "__main__":
    arbre_test = Arbre()
    arbre_test.root.create_child("I")
    arbre_test.root.create_child("II")
    arbre_test.root.children[0].create_child("1.")
    arbre_test.root.children[0].create_child("2.")
    arbre_test.root.children[0].create_child("3.")
    arbre_test.root.children[0].children[0].create_child("a)",0.5)
    arbre_test.root.children[0].children[0].create_child("b)",2)
    arbre_test.root.children[0].children[1].create_child("a)",1)
    arbre_test.root.children[0].children[1].create_child("b)",3)
    arbre_test.root.children[0].children[2].create_child("a)",1)
    arbre_test.root.children[1].create_child("1.")
    arbre_test.root.children[1].create_child("2.")
    arbre_test.root.children[1].create_child("3.", 1)
    arbre_test.root.children[1].children[0].create_child("a)",0.5)
    arbre_test.root.children[1].children[1].create_child("a)",2)
    arbre_test.print()
    print(arbre_test.get_question_list())