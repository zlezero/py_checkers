import time
import winsound
import tkinter.ttk as tkk
from threading import Thread
from tkinter import *
from tkinter import messagebox

##Variables de l'interface graphique et de jeu

Label_NbrPionsJ1 = None
Label_NbrPionsJ2 = None
Label_TourActuel = None
Label_Timer = None
timeLeft = 180000

#Variable pour la personnalisation

Couleur_PionBlanc = "white"
Couleur_PionNoir = "brown"
Couleur_DamierNoir = "black"
Couleur_DameBlancCouleur = "ivory"
Couleur_DameNoirCouleur = "red"

## -- Toutes les différentes GUI --

class MainMenu(): #Classe représentant le menu principal
    
    def __init__(self, master): #Initialisation de l'interface et de la classe

        self.master = master
        self.frame = Frame(master)

        Root.title("Jeu de Dames - Menu Principal")
        
        self.Draw_Interface()
        
        self.frame.pack()
    
    def Draw_Interface(self):
        self.Thread_MainMenuSound = Thread(target = self.Play_Music) 
        self.Thread_MainMenuSound.start()
        self.PlayButton1V1 = Button(self.frame, text = "1 VS 1", width = 25, command = self.Open_GameWindow1V1)
        self.PlayButton1V1.pack()
        self.PlayButton1VIA = Button(self.frame, text = "1 VS IA", width = 25, command = self.Open_GameWindow1VIA)
        self.PlayButton1VIA.pack()
        self.OptionsButton = Button(self.frame, text = "Options", width = 25, command = self.Open_OptionsWindow)
        self.OptionsButton.pack()
        self.quitButton = Button(self.frame, text = 'Quitter', width = 25 , command = self.Close_Window)
        self.quitButton.pack()

    def Hide_Window(self):
        self.master.withdraw()

    def Play_Music(self):
        print("...")
        #winsound.PlaySound("lul.wav" ,winsound.SND_FILENAME)

    def Show_Window(self):
        self.master.update()
        self.master.deiconify()
        
    def Close_Window(self): #Fonction permettant de fermer la fenêtre
        self.master.destroy()
    
    def Open_GameWindow1V1(self): #Fonction ouvrant la fenêtre de jeu
        Root.title("Jeu de Dames - Jeu")
        self.Hide_Window()
        self.newWindow = Toplevel(self.master)
        self.app = Jeu(self.newWindow, 2)

    def Open_GameWindow1VIA(self): #Fonction ouvrant la fenêtre de jeu
        Root.title("Jeu de Dames - Jeu")
        self.Hide_Window()
        self.newWindow = Toplevel(self.master)
        self.app = Jeu(self.newWindow, 1)
    
    def Open_OptionsWindow(self): #Fonction ouvrant la fenêtre des options
        Root.title("Jeu de Dames - Options")
        self.Hide_Window()
        self.newWindow = Toplevel(self.master)
        self.app = Options(self.newWindow)

class Options(): #Classe représentant le menu des options
    
    def __init__(self, master): #Initialisation de l'interface et de la classe
        self.master = master
        self.Frame = Frame(master)

        self.Colors = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
          'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
          'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
          'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
          'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
          'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
          'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
          'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
          'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
          'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
          'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
          'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
          'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
          'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
          'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
          'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
          'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
          'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
          'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
          'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

        self.Draw_Interface()
        self.Frame.pack()

    def Draw_Interface(self):
        self.Label_Damier = Label(self.Frame, text = "Couleur damier : ")
        self.Label_Damier.pack()
        self.ComboBox_Damier = tkk.Combobox(self.Frame, values = self.Colors, state = "readonly")
        self.ComboBox_Damier.pack()  
        self.Label_InfoCouleurPionNoir = Label(self.Frame, text = "Couleur pion noir : ")
        self.Label_InfoCouleurPionNoir.pack()
        self.ComboBox_PionNoir = tkk.Combobox(self.Frame, values = self.Colors, state = "readonly")
        self.ComboBox_PionNoir.pack()     
        self.Label_InfoCouleurPionBlanc = Label(self.Frame, text = "Couleur pion blanc : ")
        self.Label_InfoCouleurPionBlanc.pack()
        self.ComboBox_PionBlanc = tkk.Combobox(self.Frame, values = self.Colors, state = "readonly")
        self.ComboBox_PionBlanc.pack()
        self.Label_DameBlanc = Label(self.Frame, text = "Couleur Dame Blanche : ")
        self.Label_DameBlanc.pack()
        self.ComboBox_DameBlanc = tkk.Combobox(self.Frame, values = self.Colors, state = "readonly")
        self.ComboBox_DameBlanc.pack()
        self.Label_DameNoir = Label(self.Frame, text = "Couleur Dame Noir : ")
        self.Label_DameNoir.pack()
        self.ComboBox_DameNoir = tkk.Combobox(self.Frame, values = self.Colors, state = "readonly")
        self.ComboBox_DameNoir.pack()
        self.Button_Save = Button(self.Frame, text = "Sauvegarder", command = self.Save)
        self.Button_Save.pack()
        self.Button_Return = Button(self.Frame, text = "Retourner au menu", command = self.Open_MainMenuWindow)
        self.Button_Return.pack()
        self.setDefaultColor()

    def setDefaultColor(self):
        global Couleur_DameBlancCouleur, Couleur_DameNoirCouleur, Couleur_DamierNoir, Couleur_PionBlanc, Couleur_PionNoir

        self.ComboBox_Damier.set(Couleur_DamierNoir)
        self.ComboBox_PionBlanc.set(Couleur_PionBlanc)
        self.ComboBox_PionNoir.set(Couleur_PionNoir)
        self.ComboBox_DameBlanc.set(Couleur_DameBlancCouleur)
        self.ComboBox_DameNoir.set(Couleur_DameNoirCouleur)

    def Save(self):

        global Couleur_DameBlancCouleur, Couleur_DameNoirCouleur, Couleur_DamierNoir, Couleur_PionBlanc, Couleur_PionNoir

        Couleur_DameBlancCouleur = self.ComboBox_DameBlanc.get()
        Couleur_DameNoirCouleur = self.ComboBox_DameNoir.get()
        Couleur_DamierNoir = self.ComboBox_Damier.get()
        Couleur_PionBlanc = self.ComboBox_PionBlanc.get()
        Couleur_PionNoir = self.ComboBox_PionNoir.get()
        self.Open_MainMenuWindow()

    def Open_MainMenuWindow(self):
        Root.title("Jeu de Dames - Menu Principal")
        self.Hide_Window()
        self.newWindow = Toplevel(self.master)
        self.app = MainMenu(self.newWindow)

    def Hide_Window(self):
        self.master.withdraw()

    def Show_Window(self):
        self.master.update()
        self.master.deiconify()

    def Close_Window(self): #Fonction permettant de fermer la fenêtre
        self.master.destroy()
        
class Jeu(): #Classe représentant l'interface du jeu de dames
    
    def __init__(self, master, nbrJoueurs): #Initialisation de l'interface et de la classe

        global timeLeft

        self.master = master
        self.frame = Frame(master)
         
        self.nbrJoueurs = nbrJoueurs

        self.can = Canvas(self.frame, width = 500, height = 500, bg = "ivory")
        self.can.pack(side = RIGHT, padx = 0, pady =0)

        self.can.bind('<Button-1>', self.mouse_down)

        self.draw_Interface()

        self.GEng = GameEngine(self.can)
        
        self.frame.pack()

        self.Update_Timer()

        if self.nbrJoueurs == 1:
            self.Label_Joueur2.config(text = "-- Joueur 2 (Ia) --")
            self.GEng.StartGame(1)
        else:
            self.GEng.StartGame(2)
    
    def draw_Interface(self): #Fonction dessinant l'interface principale
        
        global Label_NbrPionsJ1, Label_NbrPionsJ2, Label_TourActuel, timeLeft, Label_Timer
        
        #Stockage du texte
        
        self.nbrPionsRestantsJ1_Text = "Nombre de pions restants : 20"
        self.nbrPionsRestantsJ2_Text = "Nombre de pions restants : 20"
        self.tourActuel = "Equipe jouant : Blanc"
        
        #Texte.append(self.nbrPionsRestantsJ1_Text)
        #Texte.append(self.nbrPionsRestantsJ2_Text)
        
        # -- Affichage du texte --
        self.Label_Joueur1 = Label(self.frame, text = "-- Joueur 1 --")
        self.Label_Joueur1.pack()
        Label_NbrPionsJ1 = Label(self.frame, text = self.nbrPionsRestantsJ1_Text)
        Label_NbrPionsJ1.pack()
        self.Label_Joueur2 = Label(self.frame, text = "-- Joueur 2 --")
        self.Label_Joueur2.pack()
        Label_NbrPionsJ2 = Label(self.frame, text = self.nbrPionsRestantsJ2_Text)
        Label_NbrPionsJ2.pack()
        self.Label_Séparation = Label(self.frame, text = "-------------------")
        self.Label_Séparation.pack()
        Label_TourActuel = Label(self.frame, text = self.tourActuel)
        Label_TourActuel.pack()
        Label_Timer = Label(self.frame, text = "Temps restant : {}.{}".format(self.ConvertTime(timeLeft, False), self.ConvertTime(timeLeft, True)))
        Label_Timer.pack(pady = 10)
        
        #-- Affichage des boutons
        self.Button_ReturnToMenu = Button(self.frame, text = "Retourner au menu", command = self.Open_MainMenuWindow)
        self.Button_ReturnToMenu.pack(side = BOTTOM, pady =3)
        self.Button_Restart = Button(self.frame, text='Redémarrer', command = self.Restart_Game)
        self.Button_Restart.pack(side = BOTTOM, padx =3, pady =3)
        self.Button_SkipTour = Button(self.frame, text='Passer le tour', command = self.Skip_Turn)
        self.Button_SkipTour.pack(side = BOTTOM, padx =5, pady =5)
        

    def Hide_Window(self):
        self.master.withdraw()

    def Show_Window(self):
        self.master.update()
        self.master.deiconify()

    def Open_MainMenuWindow(self):
        Root.title("Jeu de Dames - Menu Principal")
        self.Hide_Window()
        self.newWindow = Toplevel(self.master)
        self.app = MainMenu(self.newWindow)

    def mouse_down(self, event): #Fonction s'activant en cas de clic de souris sur l'interface de jeu
        print("Mouse down at : x=", event.x, "y = ", event.y)
        self.GEng.selectPion_OnClick(event.x, event.y)
    
    def Restart_Game(self):
        print("Restarting game !") 
        self.Update_Timer()
        if self.nbrJoueurs == 1:
            self.GEng.StartGame(1)
        else:
            self.GEng.StartGame(2)

    def Skip_Turn(self):
        print("Skipping turn !")
        self.GEng.Tour(True, True)

    def Close_Window(self): #Fonction permettant de fermer la fenêtre
        self.master.destroy()

    def Update_Timer(self):
        global timeLeft, Label_Timer
        if timeLeft <= 0:
            self.Skip_Turn()
        timeLeft -= 1000
        Label_Timer.config(text = "Temps restant : {}.{}".format(self.ConvertTime(timeLeft, False), self.ConvertTime(timeLeft, True)))
        Label_Timer.after(1000, self.Update_Timer)
    
    def ConvertTime(self, timeLeft, toSeconds):
        if toSeconds == True:
            return int((timeLeft/1000)%60)
        else:
            return int((timeLeft/(1000*60))%60)



class Player():
    
    def __init__(self, NomJoueur, Equipe, nbrPions, isAi):
        self.NomJoueur = NomJoueur
        self.Equipe = Equipe
        self.nbrPions = nbrPions
        self.isAi = isAi
        self.Pions = ""

class Case():
    
    def __init__(self, Couleur, PosX, PosY, Status, Equipe):
        self.Couleur = Couleur
        self.PosX = PosX
        self.PosY = PosY
        self.Status = Status
        self.Equipe = Equipe
        
class GameEngine():
    
    def __init__(self, canvas):
        
        self.teamToPlay = "Noir"
        self.canvas = canvas        
        self.TableauDames = [None] * 100
        self.TableauJoueurs = [None] * 2
                
        self.isPionSelect = False
        self.pionSelect = 99
        self.CercleChoixPossible = []
        self.ListeCaseChoixPossible = []
        self.caseIdPionSelect = 0
        
        self.listePionGraphique = []
        
        self.BlancSkip = True
        self.NoirSkip = True

        self.priseMultiple = False
        self.CasePriseMultiple = 0

    def StartGame(self, nombreJoueurs): #Fonction se lançant au début de la partie
        print("Start / Restart Game")

        self.teamToPlay = "Noir"
        
        self.canvas.delete()
        self.GenerateTableauPion()
        self.GenerateTableauPlayer(nombreJoueurs)
        self.Refresh(True)
    
    def UpdateGui(self): #Fonction permettant de mettre à jour le texte de l'interface
        print("Updating GUI !")
        global Label_NbrPionsJ1, Label_NbrPionsJ2, Label_TourActuel
        Label_NbrPionsJ1.config(text= "Nombre de pions restants : {}".format(self.TableauJoueurs[0].nbrPions))
        Label_NbrPionsJ2.config(text= "Nombre de pions restants : {}".format(self.TableauJoueurs[1].nbrPions))
        Label_TourActuel.config(text= "Equipe jouant : {}".format(self.teamToPlay))
        
    def Refresh(self, SwitchTurn): #Fonction permettant de rafraichir le damier avec les nouvelles positions des pions


        #Anti-Lag
        self.delete("caseDamier1")
        self.delete("caseDamier2")
        for i in range(len(self.listePionGraphique)):
            self.canvas.delete(self.listePionGraphique[i])
        self.listePionGraphique = []

        self.showDamier()
        self.showTerrainFromPionPlace()

        if SwitchTurn == True:
            self.Tour(True, False)
    
    def IA(self):
        print("IA !")


    def Tour(self, newTurn, isSkip): #Fonction s'executant à la fin de chaque tour
        
        global timeLeft

        if self.TableauJoueurs[0].nbrPions == 0:
            messagebox.showinfo("Gagné !!!", "J2 Won")
        elif self.TableauJoueurs[1].nbrPions == 0:
            messagebox.showinfo("Gagné !!!", "J1 Won")

        self.isPionSelect = False
        self.pionSelect = 0
        self.deleteMoveGraphObject()

        if newTurn == True:

            if (self.teamToPlay == "Blanc" and self.BlancSkip == True) or (self.teamToPlay == "Blanc" and self.BlancSkip == False and self.isSkip == True):
                self.teamToPlay = "Noir"
            else:
                self.teamToPlay = "Blanc"

        if self.TableauJoueurs[0].isAi == True or self.TableauJoueurs[1].isAi == True:
            self.IA()

        timeLeft = 180000                   

        self.UpdateGui()
            

    def GenerateTableauPion(self): #Fonction gérant la position initiale des pions
        
        PosX = -25
        PosY = 25
        i = 0

        while i < 100:
            PosX += 50
            if i < 10 or (i >= 20 and i < 30):
                self.TableauDames[i] = Case("Null", PosX, PosY, "Null", "0")
                PosX += 50
                self.TableauDames[i+1] = Case("Noir", PosX, PosY, "Pion", "1")
            elif (i >= 10 and i <= 20) or (i >= 30 and i < 40):
                self.TableauDames[i] = Case("Noir", PosX, PosY, "Pion", "1")
                PosX += 50
                self.TableauDames[i+1] = Case("Null", PosX, PosY, "Null", "0")
            elif i >= 40 and i < 60:
                self.TableauDames[i] = Case("Null", PosX, PosY, "Null", "0")
                PosX += 50
                self.TableauDames[i+1] = Case("Null", PosX, PosY, "Null", "0")
            elif (i >= 60 and i < 70) or (i >= 80 and i < 90):
                self.TableauDames[i] = Case("Null", PosX, PosY, "Null", "0")
                PosX += 50
                self.TableauDames[i+1] = Case("Blanc", PosX, PosY, "Pion", "2")
            elif (i >= 70 and i <= 80) or i >= 90:
                self.TableauDames[i] = Case("Blanc", PosX, PosY, "Pion", "2")
                PosX += 50
                self.TableauDames[i+1] = Case("Null", PosX, PosY, "Null", "0")
            print("Pos X :", i,  self.TableauDames[i].PosX)
            print("Pos Y :", i, self.TableauDames[i].PosY)
            i += 2
            
            if i == 10 or i == 20 or i == 30 or i == 40 or i == 50 or i == 60 or i == 70 or i == 80 or i == 90:
                PosX =-25
                PosY += 50
    
    def GenerateTableauPlayer(self, numberPlayers):
        nombreJoueurs = numberPlayers
        if nombreJoueurs == 1:
            self.TableauJoueurs[0] = Player("Joueur 1", 1, 20, False)
            self.TableauJoueurs[1] = Player("Joueur 2 (Ia)", 2, 20, True)
        elif nombreJoueurs == 2:
            self.TableauJoueurs[0] = Player("Joueur 1", 1, 20, False)
            self.TableauJoueurs[1] = Player("Joueur 2", 2, 20, False)
    
    
    def movePion(self, PionSelect, Direction, CaseFinale): #Fonction gérant le déplacement des pions
        
        self.priseMultiple = False
        pionToMove = PionSelect
        CaseFinale = CaseFinale
        isMove = False
        pionDirection = Direction
        numberChange = 0
        
        #On vérifie si le pion existe
        if self.TableauDames[pionToMove].Status == "Null":
            print("Pion inexistant !")
            return
        
        #On vérifie si le pion peut se déplacer s'il est au bord du damier
        if pionToMove == 10 or pionToMove == 30 or pionToMove == 50 or pionToMove == 70 or pionToMove == 90:
            if pionDirection == "DiagGaucheBas" or pionDirection == "DiagGaucheHaut":
                print("Déplacement impossible bord du damier !")
                return
        elif pionToMove == 9 or pionToMove == 29 or pionToMove == 49 or pionToMove == 69 or pionToMove == 89:
            if pionDirection == "DiagDroiteBas" or pionDirection == "DiagDroiteHaut":
                print("Déplacement impossible bord du damier !")
                return
            
        #On change le nombre de case selon la direction
        if pionDirection == "DiagDroiteBas":
            print("Déplacement : Diagonale Droite Bas")
            numberChange = 11
        elif pionDirection == "DiagGaucheBas":
            print("Déplacement : Diagonale Gauche Bas")
            numberChange = 9
        elif pionDirection == "DiagDroiteHaut":
            print("Déplacement : Diagonale Droite Haut")
            numberChange = -9
        elif pionDirection == "DiagGaucheHaut":
            print("Déplacement : Diagonale Gauche Haut")
            numberChange = -11
        else:
            print("Direction inconnue !")
            return
        
        #Déplacement du pion

        if self.TableauDames[pionToMove].Status == "Dame":
            
            #Système pour bouger la dame du point de départ au point d'arrivée
            TempV = self.TableauDames[CaseFinale]
            TempOld = self.TableauDames[pionToMove]
            
            PosXNew = TempOld.PosX
            PosYNew = TempOld.PosY

            self.TableauDames[CaseFinale] = self.TableauDames[pionToMove]
            
            self.TableauDames[CaseFinale].PosX = TempV.PosX
            self.TableauDames[CaseFinale].PosY = TempV.PosY
            
            TempV.PosX = PosXNew
            TempV.PosY = PosYNew
            
            self.TableauDames[pionToMove] = TempV

            #Système pour prendre un pion si il y en a un sur le trajet

            elementToMultiply = 0

            for i in range(9):
                elementToMultiply += 1
                if CaseFinale - (numberChange * elementToMultiply) < 100 and CaseFinale - (numberChange * elementToMultiply) > 0:
                    if (self.TableauDames[CaseFinale - (numberChange * elementToMultiply)].Status == "Pion" or self.TableauDames[CaseFinale - (numberChange * elementToMultiply)].Status == "Dame") and self.TableauDames[CaseFinale - (numberChange * elementToMultiply)].Equipe != self.TableauDames[CaseFinale].Equipe:
                        
                        if self.TableauDames[CaseFinale - (numberChange * elementToMultiply)].Equipe == "1":
                            self.TableauJoueurs[0].nbrPions -= 1
                        else:
                            self.TableauJoueurs[1].nbrPions -= 1
                       
                        self.TableauDames[CaseFinale - (numberChange * elementToMultiply)].Status = "Null"
                        self.TableauDames[CaseFinale - (numberChange * elementToMultiply)].Couleur = "Null"
                        self.TableauDames[CaseFinale - (numberChange * elementToMultiply)].Equipe = "0"                 

                        isMove = True
                        break
                
        elif self.TableauDames[pionToMove + (numberChange)].Status == "Null": #Si l'endroit ou le pion doit aller est vide
        
            TempV = self.TableauDames[pionToMove + (numberChange)]
            TempOld = self.TableauDames[pionToMove]
            
            PosXNew = TempOld.PosX
            PosYNew = TempOld.PosY

            self.TableauDames[pionToMove + (numberChange)] = self.TableauDames[pionToMove]
            
            self.TableauDames[pionToMove + (numberChange)].PosX = TempV.PosX
            self.TableauDames[pionToMove + (numberChange)].PosY = TempV.PosY
            
            TempV.PosX = PosXNew
            TempV.PosY = PosYNew
            
            self.TableauDames[pionToMove] = TempV
            
            CaseFinale = pionToMove + (numberChange)

            print("DEBUG : New pos :", pionToMove + (numberChange))
            
        elif (self.TableauDames[pionToMove + (numberChange)].Equipe == "2" and self.TableauDames[pionToMove].Equipe == "1") or (self.TableauDames[pionToMove + (numberChange)].Equipe == "1" and self.TableauDames[pionToMove].Equipe == "2"): #On regarde si on peut prendre un pion
        
            if self.TableauDames[pionToMove + (numberChange * 2)].Status == "Null": #Si une case est libre après le pion
                
                #Initialisation des différentes variables

                TempPionOriginal = self.TableauDames[pionToMove]

                TempPionTake = self.TableauDames[pionToMove + (numberChange)]

                TempPionNewCase = self.TableauDames[pionToMove + (numberChange * 2)]
                
                PosX_PionOriginal = TempPionOriginal.PosX
                PosY_PionOriginal = TempPionOriginal.PosY

                PosX_PionTake = TempPionTake.PosX
                PosY_PionTake = TempPionTake.PosY

                PosX_PionNewCase = TempPionNewCase.PosX
                PosY_PionNewCase = TempPionNewCase.PosY

                #On bouge le pion qui mange l'autre

                self.TableauDames[pionToMove + (numberChange * 2)], self.TableauDames[pionToMove] = self.TableauDames[pionToMove], self.TableauDames[pionToMove + (numberChange * 2)]
                self.TableauDames[pionToMove + (numberChange * 2)].PosX = self.TableauDames[pionToMove].PosX
                self.TableauDames[pionToMove + (numberChange * 2)].PosY = self.TableauDames[pionToMove].PosY

                #On élimine le pion situé au centre

                self.TableauDames[pionToMove + (numberChange)].Status = "Null"
                self.TableauDames[pionToMove + (numberChange)].Couleur = "Null"

                if self.TableauDames[pionToMove + (numberChange)].Equipe == "1":
                    self.TableauJoueurs[0].nbrPions -= 1
                else:
                    self.TableauJoueurs[1].nbrPions -= 1

                self.TableauDames[pionToMove + (numberChange)].Equipe = "0"

                #On déplace la case vide sur la case de départ

                self.TableauDames[pionToMove].Status = "Null"
                self.TableauDames[pionToMove].Couleur = "Null"
                self.TableauDames[pionToMove].Equipe = "0"

                self.TableauDames[pionToMove].PosX = PosX_PionOriginal
                self.TableauDames[pionToMove].PosY = PosY_PionOriginal
                
                isMove = True
                CaseFinale = pionToMove + (numberChange * 2)

                print("DEBUG : New pos :", pionToMove + (numberChange * 2))
                print("Pion pris !")
                
            else: #Si un emplacement est indisponible on ne peut pas prendre le pion
                print("Impossible de prendre le pion !")
        else:
            print("Déplacement impossible !")
            return
        
        #On regarde si on peut transformer le pion en dame
        if isMove == False:
            self.CheckTransformatonDame(pionToMove + (numberChange))
        else:
            self.CheckTransformatonDame(pionToMove + (numberChange * 2))

            #On regarde si il y a possiblité de prise multiple après une prise

            self.priseMultiple = True
            self.isPionSelect = True
            self.pionSelect = CaseFinale
            self.CasePriseMultiple = CaseFinale

            if self.showPlaceToGo(CaseFinale) == "PionCanBeTake":
                self.Refresh(False)
                return

        self.priseMultiple = False

        self.Refresh(True)

    
    def CheckTransformatonDame(self, PionSelect): #Fonction qui regarde si les pions doivent se transformer en dames

        pionSelect = PionSelect
        
        if self.TableauDames[pionSelect].Status == "Pion":
            if (pionSelect > 90 and self.TableauDames[pionSelect].Equipe == "1") or (pionSelect < 10 and self.TableauDames[pionSelect].Equipe == "2"):
                self.TableauDames[pionSelect].Status = "Dame"
                self.listeDameCantMove.append(pionSelect)
    
    def showTerrainFromPionPlace(self): #Fonction qui affiche les pions en fonction du tableau

        global Couleur_PionBlanc, Couleur_PionNoir, Couleur_DameBlancCouleur, Couleur_DameNoirCouleur, Couleur_DamierNoir

        i = 0 
        x = 0
        cercleX = -25
        cercleY = 25    

        while i < len(self.TableauDames): #Selon le status de chaque pion dans le tableau on l'affiche graphiquement sur le damier           
            x = 0
            while x < 10:
                cercleX += 50
                if self.TableauDames[i].Status != "Null":
                    if self.TableauDames[i].Couleur == "Blanc" and self.TableauDames[i].Status == "Dame":
                        self.listePionGraphique.append(self.cercle(cercleX, cercleY, 25, Couleur_PionBlanc))
                        self.listePionGraphique.append(self.cercle(cercleX, cercleY, 20, Couleur_DameBlancCouleur))
                    elif self.TableauDames[i].Couleur == "Noir" and self.TableauDames[i].Status == "Dame":
                        self.listePionGraphique.append(self.cercle(cercleX, cercleY, 25, Couleur_PionNoir))
                        self.listePionGraphique.append(self.cercle(cercleX, cercleY, 20, Couleur_DameNoirCouleur))
                    elif self.TableauDames[i].Couleur == "Blanc":
                        self.listePionGraphique.append(self.cercle(cercleX, cercleY, 20, Couleur_PionBlanc))
                    elif self.TableauDames[i].Couleur == "Noir":
                        self.listePionGraphique.append(self.cercle(cercleX, cercleY, 20, Couleur_PionNoir))
                i += 1
                x += 1
            cercleX = -25
            cercleY += 50
            
    def showDamier(self): #Fonction qui trace un damier

        global Couleur_DamierNoir

        x = -100
        y = -50
        line = 0
        while line <= 10: #On boucle tant que toutes les lignes n'ont pas été tracées
            y = 0
            if line % 2 == 0: #Si le numéro de ligne est impaire on les places normalement
                while y < 500: #On boucle tant que l'on a pas fait chacune des lignes
                    while x < 500: #On boucle tant que l'on a pas fini chaque carré d'une ligne
                        self.canvas.create_rectangle(x+50, y, x+100, y + 50, fill = Couleur_DamierNoir, tags = "caseDamier1")
                        x += 100       
                    x = -100
                    y += 100
            else: #Sinon on les décales
                while y < 470: #On boucle tant que l'on a pas fait chacune des lignes
                    while x < 390: #On boucle tant que l'on a pas fini chaque carré d'une ligne
                        self.canvas.create_rectangle(x+100, y+50, x+150, y + 100, fill = Couleur_DamierNoir, tags = "caseDamier2")
                        x += 100
                    x = -100
                    y += 100
            line += 1
       
## Fonctions utilisée lorsque l'on clique 

    def selectPion_OnClick(self, PosX, PosY): #Fonction s'éxécutant en cas de click du joueur sur le damier
        
        #Suppression des formes géométriques si elles sont déjà créer
        self.deleteMoveGraphObject()   
          
        #Debug
        print("PosX % 100 = ", PosX % 100)
        print("PosY % 100 = ", PosY % 100)

        #On obtient l'id de la case en fonction d'où l'on a cliqué
        caseIdClicked = self.getCaseIdByPos(PosX, PosY)

        #Si un pion est déjà sélectionner on regarde où on peut l'envoyer
        if self.isPionSelect == True:

            if self.TableauDames[self.caseIdPionSelect].PosY < PosY :
                if self.TableauDames[self.caseIdPionSelect].PosX < PosX and caseIdClicked in self.ListeCaseChoixPossible:
                    self.movePion(self.pionSelect, "DiagDroiteBas", caseIdClicked)
                elif self.TableauDames[self.caseIdPionSelect].PosX > PosX and caseIdClicked in self.ListeCaseChoixPossible:
                    self.movePion(self.pionSelect, "DiagGaucheBas", caseIdClicked)
            else:
                if self.TableauDames[self.caseIdPionSelect].PosX < PosX and caseIdClicked in self.ListeCaseChoixPossible:
                    self.movePion(self.pionSelect, "DiagDroiteHaut", caseIdClicked)
                elif self.TableauDames[self.caseIdPionSelect].PosX > PosX and caseIdClicked in self.ListeCaseChoixPossible:
                    self.movePion(self.pionSelect, "DiagGaucheHaut", caseIdClicked) 

            if self.priseMultiple == False:
                self.isPionSelect = False
                self.pionSelect = 99
                return
        
        if self.priseMultiple == False or self.priseMultiple == True:

            self.pionSelect = 0

            print(caseIdClicked)

            if self.TableauDames[caseIdClicked].Couleur == self.teamToPlay:
                self.pionSelect = caseIdClicked
            else:
                self.pionSelect = 102
                self.isPionSelect = False
        
            if self.pionSelect < 101 and self.TableauDames[caseIdClicked].Status != "Null": 
         
                if (self.priseMultiple == True and self.CasePriseMultiple == self.pionSelect) or self.priseMultiple == False:
                    self.caseIdPionSelect = self.pionSelect
                    self.isPionSelect = True
            
                    self.canvas.create_rectangle(self.roundint(PosX, 50), self.roundint(PosY, 50), self.roundint(PosX, 50) + 50, self.roundint(PosY, 50) + 50 , outline = "yellow", width = 3, tags = "rectangleSelectPion")
            
                    self.showPlaceToGo(self.pionSelect)

    def getCaseIdByPos(self, PosX, PosY): #Fonction permettant d'obtenir l'id d'un pion en fonction de l'emplacement clické
        for i in range(len(self.TableauDames)):
            if ((PosX % 100) > 25 and (PosY % 100) > 25) or ((PosX % 100) > 25 and (PosY % 100) < 25):
                if (self.TableauDames[i].PosX == self.roundint(PosX, 25) or self.TableauDames[i].PosX == self.roundint(PosX, 25) + 25) and (self.TableauDames[i].PosY == self.roundint(PosY, 25) or self.TableauDames[i].PosY == self.roundint(PosY, 25) + 25):
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    return i
            elif (PosX % 100) < 25 and (PosY % 100) > 25:
                if self.TableauDames[i].PosX == self.roundint(PosX, 25) + 25 and self.TableauDames[i].PosY == self.roundint(PosY, 25):
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    return i
            elif (PosY % 100) < 25:
                if self.TableauDames[i].PosX == self.roundint(PosX, 25) + 25 and self.TableauDames[i].PosY == self.roundint(PosY, 25) + 25:
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    return i
            if (PosX % 100) < 25:
                if self.TableauDames[i].PosX == self.roundint(PosX, 25) + 25 and self.TableauDames[i].PosY == self.roundint(PosY, 25) + 25:
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    return i
            else:
                if self.TableauDames[i].PosX == self.roundint(PosX, 25) and self.TableauDames[i].PosY == self.roundint(PosY, 25):
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    return i
        return 99 #Si l'on ne trouve aucun pion

    def deleteMoveGraphObject(self): #Fonction qui permet de supprimer les éléments graphiques relatifs à la selection d'un pion
        self.delete("rectangleSelectPion")
        for i in range(len(self.CercleChoixPossible)):
            self.canvas.delete(self.CercleChoixPossible[i])

    def showPlaceToGo(self, pionSelect): #Montre les endroits possibles sur le damier
        
        pionSelect = pionSelect #Variable qui contiendra l'id du pion sélectionner
        canTakePion = False #Variable permettant de savoir si l'on peut prendre un pion

        listeInterdit = [0, 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 31, 33, 35, 37, 39, 40, 42, 44, 46, 48, 51, 53, 55, 57, 59, 60, 62, 64, 66, 68, 71, 73, 75, 77, 79, 80, 82, 84, 86, 88, 91, 93, 95, 97, 99] #Cases ou les pions ne pourront jamais aller
        listeCheck = [-11, -9, 9, 11]
        listeCheckDynamic = []

        self.CercleChoixPossible = [] #Tableau contenant les positions des cercles qui indiquent les choix possibles
        self.ListeCaseChoixPossible = []

        if self.TableauDames[pionSelect].Equipe == "1": #Si les blancs jouent on descend les pions vers le bas
            listeCheckDynamic.append(9)
            listeCheckDynamic.append(11)

        elif self.TableauDames[pionSelect].Equipe == "2": #Sinon on regarde vers le haut
            listeCheckDynamic.append(-9)
            listeCheckDynamic.append(-11)

        #Système de preview de déplacement des dames

        if self.TableauDames[pionSelect].Status == "Dame" and self.TableauDames[pionSelect] not in self.listeDameCantMove:
            for i in listeCheck:
                numberToMutiply = 1
                nbrPions = 0
                while numberToMutiply < 9:
                    if pionSelect + (i * numberToMutiply) < 99 and pionSelect + (i * numberToMutiply) > 0:
                        if self.TableauDames[pionSelect + (i * numberToMutiply)].Status == "Pion" or self.TableauDames[pionSelect + (i * numberToMutiply)].Status == "Dame":
                               nbrPions += 1
                        if self.TableauDames[pionSelect + (i * numberToMutiply)].Status == "Null" and pionSelect + (i * numberToMutiply) not in listeInterdit:
                            if nbrPions == 0 or nbrPions == 1:
                                self.CercleChoixPossible.append(self.canvas.create_oval(self.TableauDames[pionSelect + (i * numberToMutiply)].PosX - 5, self.TableauDames[pionSelect + (i * numberToMutiply)].PosY - 5, self.TableauDames[pionSelect + (i * numberToMutiply)].PosX + 5, self.TableauDames[pionSelect + (i * numberToMutiply)].PosY + 5, fill= "yellow"))
                                self.ListeCaseChoixPossible.append(pionSelect + (i * numberToMutiply)) 
                            else:
                                canTakePion = True
                    numberToMutiply += 1
            return
         
        #Système de preview des pions normaux

        for i in listeCheck: #On regarde si on peux manger un pion
               if pionSelect + (i * 2) < 100 and pionSelect + (i * 2) > 0:
                    if (self.TableauDames[pionSelect + (i)].Status == "Pion" or self.TableauDames[pionSelect + (i)].Status == "Dame") and self.TableauDames[pionSelect + (i * 2)].Status == "Null" and self.TableauDames[pionSelect + (i)].Equipe != self.TableauDames[pionSelect].Equipe and pionSelect + (i) not in listeInterdit and pionSelect + (i * 2) not in listeInterdit:   
                       self.CercleChoixPossible.append(self.canvas.create_oval(self.TableauDames[pionSelect + (i * 2)].PosX - 5, self.TableauDames[pionSelect + (i * 2)].PosY - 5, self.TableauDames[pionSelect + (i * 2)].PosX + 5, self.TableauDames[pionSelect + (i * 2)].PosY + 5, fill= "yellow"))
                       self.ListeCaseChoixPossible.append(pionSelect + (i * 2))
                       canTakePion = True
        
        if self.priseMultiple != True and canTakePion != True:
            for i in listeCheckDynamic:
                if pionSelect + (i) < 100 and pionSelect + (i) > 0:
                    if self.TableauDames[pionSelect + (i)].Status == "Null" and pionSelect + (i) not in listeInterdit:
                        self.CercleChoixPossible.append(self.canvas.create_oval(self.TableauDames[pionSelect + (i)].PosX - 5, self.TableauDames[pionSelect + (i)].PosY - 5,  self.TableauDames[pionSelect + (i)].PosX + 5, self.TableauDames[pionSelect + (i)].PosY + 5, fill= "yellow"))
                        self.ListeCaseChoixPossible.append(pionSelect + (i))

        if self.priseMultiple == True and self.ListeCaseChoixPossible != []:
            return "PionCanBeTake"
        elif self.priseMultiple == True:
            return "NoPionCanBeTake"
       
        self.listeDameCantMove = [] 
         
# --- Fonctions Graphiques et utilitaires ---

    def roundint(self, value, base=5): #Fonction permettant d'arrondir
        return int(value) - int(value) % int(base)
    
    def delete(self, MonTag): #Fonction permettant de supprimer des objets graphiques en fonction d'un tag
        self.canvas.delete(self.canvas.find_withtag(MonTag))

    def cercle(self, x, y, r, coul, tagsC = "cercle"): #Fonction permettant de tracer un cercle
        "tracé d ' un cercle de centre (x,y) et de rayon r"
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=coul, tags="cercleChoixPos")
    
    def Rectangle(self, x, y, coul): #Fonction permettant de tracer un rectangle
        self.canvas.create_rectangle(x + 20, x+20, y + 20, y+20, outline=coul)

        
## -- Programme Principal --

Root = Tk() #Variable principale

#Boucle principale
cls = MainMenu(Root)
Root.mainloop()
        

        
    
