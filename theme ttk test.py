# import tkinter , tkinter.ttk


# FNC_Theme = lambda event : tkinter.ttk.Style ( ).theme_use ( BOX_Choix.get ( ) )


# TKI_Principal = tkinter.Tk ( )


# BOX_Choix = tkinter.ttk.Combobox ( TKI_Principal , values = tkinter.ttk.Style ( ).theme_names ( ) )

# BOX_Choix.bind ( "<<ComboboxSelected>>" , FNC_Theme )

# BOX_Choix.set ( tkinter.ttk.Style ( ).theme_use ( ) )


# tkinter.ttk.Label ( TKI_Principal , text = "\n Test de changement \n" , relief = "solid" ).pack ( padx = 5 , pady = 5 )

# tkinter.ttk.Checkbutton ( TKI_Principal , text = "Coche" ).pack ( )

# tkinter.ttk.Radiobutton ( TKI_Principal , text = "Radio" ).pack ( )

# tkinter.ttk.Scale ( TKI_Principal , orient = "horizontal" ).pack ( padx = 5 , pady = 5 )

# tkinter.ttk.Scrollbar ( TKI_Principal , orient = "horizontal" ).pack ( fill = "both" , padx = 5 , pady = 5 )

# BOX_Choix.pack ( padx = 5 , pady = 5 )

# tkinter.Button ( TKI_Principal , text = "Quitter" , command = TKI_Principal.destroy ).pack ( )


# FNC_Theme ( None )


# TKI_Principal.mainloop ( )
import tkinter as tk
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk

window = ThemedTk(theme="yaru")
ttk.Button(window, text="Quit", command=window.destroy).pack()
ttk.Label ( window , text = "\n Test de changement \n" , relief = "solid" ).pack ( padx = 5 , pady = 5 )

ttk.Checkbutton ( window , text = "Coche" ).pack ( )

ttk.Radiobutton ( window , text = "Radio" ).pack ( )

ttk.Scale ( window , orient = "horizontal" ).pack ( padx = 5 , pady = 5 )

ttk.Scrollbar ( window , orient = "horizontal" ).pack ( fill = "both" , padx = 5 , pady = 5 )
BOX_Choix = ttk.Combobox ( window , values = ttk.Style ( ).theme_names ( ) )
BOX_Choix.pack ( padx = 5 , pady = 5 )

tk.Button ( window , text = "Quitter" , command = window.destroy ).pack ( )

window.mainloop()
