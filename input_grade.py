import tkinter as tk
from tkinter import ttk
import ttkwidgets
import glob
from gif import Gif

# TODO:
# Faire une place dans la fenetre pour des appréciations perso:
# Genre horreur ou arrrrrrghhh, bien, non homogène, c'est du cours ! avec éventuellement Gif et son 



class Input_grade(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('500x800')
        self.title('Saisie des notes')

        #Les gifs
        self.load_gifs()
        self.animation = None
        self.nb_times_gif_played = 3

        #Clavier
        self.bind('<Key>',self.key_handler)

        # Les buttons

        # Un cadre pour les 2 premiers bouttons
        frame = ttk.Frame(self)
        
        self.nextq_button = ttk.Button(frame,
                text='Question suivante',
                command=self.nextq)
        
        self.prevq_button = ttk.Button(frame,
                text='Question précédente',
                command=self.prevq)
        
        self.prevq_button.pack(side= tk.LEFT)
        self.nextq_button.pack()

        #Le Slider de notes
        style = ttk.Style(self)        
        style.configure("my.Horizontal.TScale" ,sliderlength = 150)
        self.grade_button = ttkwidgets.TickScale(self,from_ =0, to=1,resolution=0.25, tickinterval=0.25,style="my.Horizontal.TScale")
        self.grade_button.set(0.5)
        print(self.grade_button.__getattribute__('_resolution'))
        print(self.grade_button.get())
        
        # Le label qui contiendra le gif
        self.img_label = ttk.Label(self)

        # Un cadre pour les bouttons commantaires
        frame2 = ttk.Frame(self)
        
        self.jpp = ttk.Button(frame2,
                text='Jpp',
                command=lambda :self.animate_gif('jpp'))
        
        self.non = ttk.Button(frame2,
                text='NON !',
                command=lambda :self.animate_gif('non'))
        
        self.oui = ttk.Button(frame2,
                text='OUI !',
                command=lambda :self.animate_gif('oui'))
        
        self.jpp.pack(side= tk.LEFT)
        self.non.pack(side= tk.LEFT)
        self.oui.pack()
        # self.report_button = ttk.Button(self,
        #         text='BILAN',
        #         command=self.report)
        # self.report_button.state(['disabled'])
        
        # self.load_class_button = ttk.Button(self,
        #         text='Charger une classe',
        #         command=self.load_class)
        
        # self.input_button = ttk.Button(self,
        #         text='Saisir les notes',
        #         command=self.input)
        # self.input_button.state(['disabled'])

        # Placement des bouttons
        frame.pack(expand=True)
        self.grade_button.pack(fill='x')
        self.img_label.pack()
        frame2.pack(expand=True)
        ttk.Button(self,
                text='Fin de la saisie',
                command=self.end).pack(expand=True)

    def adjust_grade_button(self,min,max,step):
        self.grade_button.__setattr__('_start',min)

    def load_gifs(self):
        self.gifs_dic ={}
        list = glob.glob('./gifs/*.gif')
        for file in list:
            self.gifs_dic[file[7:-4]]=Gif(file)
        print(self.gifs_dic)
        self.current_gif = ''

    def animate_gif(self,gif_name):
        if self.current_gif == gif_name:
            gif = self.gifs_dic[gif_name]
            if gif.nb_played < self.nb_times_gif_played:
                self.img_label.config(image= gif.current_frame)
                gif.next_frame()
                self.animation = self.after(75,self.animate_gif,gif_name)
            else:
                self.after_cancel(self.animation)
                gif.reset()
        else:
            if self.animation is not None:
                self.after_cancel(self.animation)
            self.current_gif = gif_name
            self.animate_gif(gif_name)

    
    def nextq(self):
        pass
    def prevq(self):
        pass
    def key_handler(self,event):
        if event.keysym == 'Right':
            self.nextq()
        if event.keysym == 'Left':
            self.prevq()
    def end(self):
        self.destroy()