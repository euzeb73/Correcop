import tkinter as tk
from tkinter import ttk

"""

TODO (Plus tard): importer parties et alphabet du fichier config.json
"""

PARTIES = ['I','II','III','IV','V','VI','VII','VIII','IX','X']
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

class Noeud():
    def __init__(self,parent,name,data = None):
        self.parent = parent 
        self.children = []
        self.name = name
        if name != 'Root':
            if parent.fullname:
                self.fullname = parent.fullname+' ' +name
            else:
                self.fullname = name
        else:
            self.fullname = ''
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
    def arbre_to_json(self):
        pass
    def get_question_list(self):
        """
        Renvoie la liste des question et la liste des data (barême)
        """
        return self.parcours_enprof(self.root)
    def parcours_enprof(self,noeud : Noeud):
        """
        Fonction récursive de parcour de l'arbre qui renvoie la liste des noms des noeuds et des data
        """
        if noeud.children:
            listeq = []
            listedata = []
            for child in noeud.children:
                listeq.extend(self.parcours_enprof(child)[0])
                listedata.extend(self.parcours_enprof(child)[1])
            return listeq,listedata     
        else:
            return [noeud.fullname],[noeud.data]
    def add_bareme(self,bareme):
        """
        Modifie les data des feuilles (questions) avec la liste des valeurs dans bareme
        ATENTION : détruit la liste bareme
        Pas de test pour voir si on a bien autant de notes que de feuilles (questions)
        """
        self.add_bareme_recurs(self.root,bareme)
    def add_bareme_recurs(self,noeud : Noeud,bareme):
        if noeud.children:
            for child in noeud.children:
                self.add_bareme_recurs(child,bareme)
        else:
            note = bareme.pop(0)
            noeud.data = note
            






class Create_DS(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('900x250')
        self.title('Nouveau DS')
        self.validate_DS_button = ttk.Button(self,
                text='Valider et passer au barême',
                command=self.enter_bareme)
        self.validate_DS_button.pack(expand=True,pady=5,side=tk.BOTTOM)
        # self.cancel = ttk.Button(self,
        #         text='Annuler et recommencer',
        #         command=self.init_parties)
        # self.cancel.pack(expand=True,pady=5,side=tk.BOTTOM)
        
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
        """
        Initialise et prépare pour entrer le nb de parties, exos, questions
        """
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
        """
        Initialise et prépare pour rentrer le nb d'exos et de questions (apppelé par init_parties)
        """
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
        """ Crée l'arbre de DS d'après les valeurs rentrées"""
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
        return arbre

    def enter_bareme(self):
        arbre = self.export_tree()
        window = Bareme(self,arbre)
        window.grab_set()


class Bareme(tk.Toplevel):
    def __init__(self, parent, arbre : Arbre):
        super().__init__(parent)
        self.arbre = arbre
        self.geometry('900x250')
        self.title('Barême')
        self.validate_bareme_button = ttk.Button(self,
                text='Valider le barême',
                command=self.validate)
        self.validate_bareme_button.pack(expand=True,pady=5,side=tk.BOTTOM)
        self.validate_bareme_button.state(['disabled'])
        questions, bareme = self.arbre.parcours_enprof(self.arbre.root) # pour l'instant bareme est probablement rempli de None
        ################
        # TODO : utiliser le résultat de vibe pour insérer un tableau questio baremen éditable
        ################

    def bareme_is_OK(self):
        """
        Test si le barême est OK (des nombres partout)
        A appeler on change des spinbox ou autre.
        """
        return True
    def validate(self):
        """
        A executer quand on a fini de rentrer le bareme
        """
        pass





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
    bareme=[1,2,3,4,5,6,7,8]
    arbre_test.add_bareme(bareme)
    print(arbre_test.get_question_list())
    arbre_test.print()