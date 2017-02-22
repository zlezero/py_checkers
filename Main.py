import tkinter as tk
from tkinter import *
from GameEngine import *
        
## -- Toutes les différentes GUI --

class MainMenu(): #Classe représentant le menu principal
    
    def __init__(self, master): #Initialisation de l'interface et de la classe
        self.master = master
        self.frame = Frame(master)
        Root.title("Jeu de Dames - Menu Principal")
        self.PlayButton = Button(self.frame, text = "Jouer", width = 25, command = self.Open_GameWindow)
        self.PlayButton.pack()
        self.OptionsButton = Button(self.frame, text = "Options", width = 25, command = self.Open_OptionsWindow)
        self.OptionsButton.pack()
        self.quitButton = Button(self.frame, text = 'Quitter', width = 25 , command = self.Close_Window)
        self.quitButton.pack()
        self.frame.pack()
    
    def Close_Window(self): #Fonction permettant de fermer la fenêtre
        self.master.destroy()
    
    def Open_GameWindow(self): #Fonction ouvrant la fenêtre de jeu
        Root.title("Jeu de Dames - Jeu")
        self.newWindow = Toplevel(self.master)
        self.app = Jeu(self.newWindow)
    
    def Open_OptionsWindow(self): #Fonction ouvrant la fenêtre des options
        Root.title("Jeu de Dames - Options")
        self.newWindow = Toplevel(self.master)
        self.app = Options(self.newWindow)

class Options(): #Classe représentant le menu des options
    
    def __init__(self, master): #Initialisation de l'interface et de la classe
        self.master = master
        self.Frame = Frame(master)
    
    def Close_Window(self): #Fonction permettant de fermer la fenêtre
        self.master.destroy()
        
class Jeu(): #Classe représentant l'interface du jeu de dames
    
    def __init__(self, master): #Initialisation de l'interface et de la classe
        self.master = master
        self.frame = Frame(master)
        
        
        self.can = Canvas(self.frame, width = 500, height = 500, bg = "ivory")
        self.can.pack(side = RIGHT, padx = 0, pady =0)
        self.can.bind('<Button-1>', self.mouse_down)
        
        self.GEng = GameEngine(self.can)
        
        self.draw_Interface()
        
        self.frame.pack()
    
    def draw_Interface(self): #Fonction dessinant l'interface principale
    
        # -- Affichage du texte --
        self.Label_Joueur1 = Label(self.frame, text = "-- Joueur 1 --")
        self.Label_Joueur1.pack()
        self.Label_NbrPionsJ1 = Label(self.frame, text = "Nombre de pions restants : 20")
        self.Label_NbrPionsJ1.pack()
        self.Label_Joueur2 = Label(self.frame, text = "-- Joueur 2 --")
        self.Label_Joueur2.pack()
        self.Label_NbrPionsJ2 = Label(self.frame, text = "Nombre de pions restants : 20")
        self.Label_NbrPionsJ2.pack()
        
        #-- Affichage des boutons
        self.Button_Start = Button(self.frame, text='Redémarrer', command = self.GEng.StartGame(2))
        self.Button_Start.pack(side = BOTTOM, padx =3, pady =3)
    
    def mouse_down(self, event): #Fonction s'activant en cas de clic de souris sur l'interface de jeu
        print("mouse down at : x=", event.x, "y = ", event.y)
        self.GEng.selectPion_OnClick(event.x, event.y)
        
    def Close_Window(): #Fonction permettant de fermer la fenêtre
        self.master.destroy()
        
        
## -- Programme Principal --

Root = Tk() #Variable principale

#Boucle principale
cls = MainMenu(Root)
Root.mainloop()
        

        
    
