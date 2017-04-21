import time
import random
import wave
import os
from tkinter import ttk as tkk
from threading import Thread
from tkinter import messagebox
from tkinter import *
from copy import deepcopy

##Variables de l'interface graphique et de jeu

Label_NbrPionsJ1 = None
Label_NbrPionsJ2 = None
Label_TourActuel = None
Label_Timer = None
Button_SkipTour = None

timeLeft = 180000

#Variables pour la personnalisation

Couleur_PionBlanc = "white"
Couleur_PionNoir = "brown"
Couleur_DamierNoir = "black"
Couleur_DameBlancCouleur = "ivory"
Couleur_DameNoirCouleur = "red"
Couleur_PionPreview = "yellow"

priseMultiple = False
hasGameFinished = False

Rules_PriseMultipleEnable = True
Rules_DamesEnable = True
Rules_PriseObligatoireEnable = True
Rules_Timer = True

Use_Texture = False

IA_Version = 1

## -- Toutes les différentes GUI --
class MainMenu(): #Classe représentant le menu principal
    
    def __init__(self, master): #Initialisation de l'interface et de la classe

        self.master = master
        self.Frame = Frame(master)

        Root.title("Jeu de Dames - Menu Principal")
               
        self.Draw_Interface()
            
    def Draw_Interface(self): #Fonction dessinant l'interface

        self.Thread_MainMenuSound = Thread(target = self.Play_Music) #Thread laançant la musique en arrière plan (n'est pas encore codé)
        self.Thread_MainMenuSound.start()

        self.master.geometry("487x341+479+86")
        self.master.configure(background="#d9d9d9")

        fontTitle = "-family {Segoe UI} -size 19 -weight bold -slant "  \
            "roman -underline 1 -overstrike 0"

        self.Frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame.configure(relief=GROOVE)
        self.Frame.configure(borderwidth="2")
        self.Frame.configure(relief=GROOVE)
        self.Frame.configure(background="#d9d9d9")
        self.Frame.configure(width=495)

        self.Label_Title = Label(self.Frame)
        self.Label_Title.place(relx=0.31, rely=0.01, height=21, width=183)
        self.Label_Title.configure(background="#d9d9d9")
        self.Label_Title.configure(disabledforeground="#a3a3a3")
        self.Label_Title.configure(font=fontTitle)
        self.Label_Title.configure(foreground="#000000")
        self.Label_Title.configure(text="JEU DE DAMES")
        self.Label_Title.configure(width=183)

        self.PlayButton1V1 = tkk.Button(self.Frame, command = self.Open_GameWindow1V1)
        self.PlayButton1V1.place(relx=0.24, rely=0.12, height=24, width=257)
        self.PlayButton1V1.configure(text="Joueur VS Joueur")

        self.PlayButton1VIA = tkk.Button(self.Frame, command = self.Open_GameWindow1VIA)
        self.PlayButton1VIA.place(relx=0.24, rely=0.25, height=24, width=257)
        self.PlayButton1VIA.configure(text="Joueur VS IA")

        self.Button_IAVSIA = tkk.Button(self.Frame, command = self.Open_GameWindow1VIA)
        self.Button_IAVSIA.place(relx=0.24, rely=0.38, height=24, width=257)
        self.Button_IAVSIA.configure(text="IA VS IA")

        self.Button_Multiplayer = tkk.Button(self.Frame, command = self.Open_MultiplayerWindow)
        self.Button_Multiplayer.place(relx=0.24, rely=0.51, height=24, width=257)
        self.Button_Multiplayer.configure(text = "Multijoueur")

        self.OptionsButton = tkk.Button(self.Frame, command = self.Open_OptionsWindow)
        self.OptionsButton.place(relx=0.24, rely=0.64, height=24, width=257)
        self.OptionsButton.configure(text="Options")

        self.Button_Rules = tkk.Button(self.Frame, command = self.ShowRules)
        self.Button_Rules.place(relx=0.24, rely=0.77, height=24, width=257)
        self.Button_Rules.configure(text="Règles")

        self.quitButton = tkk.Button(self.Frame, command = self.Close_Window)
        self.quitButton.place(relx=0.24, rely=0.89, height=24, width=257)
        self.quitButton.configure(text="Quitter")

    def ShowRules(self):
        messagebox.showinfo("Règles", "Un joueur doit éliminer tous les pions adverses. \n Si un de ses pions arrivent de l'autre coté du damier il devient une dame.", parent = self.master)

    def Hide_Window(self): #Fonction permettant de cacher la fenêtre
        self.master.withdraw()

    def Play_Music(self): #Fonction jouant permettant de lancer la musique
        print("")

    def Show_Window(self): #Fonction permettant de réafficher la fenêtre
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

    def Open_MultiplayerWindow(self):
        Root.title("Jeu de Dames - Multijoueur")
        self.Hide_Window()
        self.newWindow = Toplevel(self.master)
        self.app = Multijoueur(self.newWindow)

class Options(): #Classe représentant le menu des options
    
    def __init__(self, master): #Initialisation de l'interface et de la classe

        global Rules_DamesEnable, Rules_PriseMultipleEnable, Rules_PriseObligatoireEnable, Rules_Timer

        self.master = master
        self.Frame = Frame(master)
        self.style = ttk.Style()

        self.IaButton = IntVar()
       
        #Liste des différentes couleurs de tkinter
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

        self.setChkButton()
        self.Draw_Interface()
       
    def setChkButton(self):
        if Rules_DamesEnable:
            self.ChkDameEnable = 1
        else:
            self.ChkDameEnable = 0

        if Rules_PriseMultipleEnable:
            self.ChkPriseMultipleEnable = 1
        else:
            self.ChkPriseMultipleEnable = 0

        if Rules_PriseObligatoireEnable:
            self.ChkPriseObligatoireEnable = 1
        else:
            self.ChkPriseObligatoireEnable = 0

        if Rules_Timer:
            self.ChkTimerEnable = 1
        else:
            self.ChkTimerEnable = 0

    def Draw_Interface(self): #Fonction dessinant l'interface

        print("Drawing options interface...")

        #Configuration générale
        self.master.geometry("598x343+438+58")

        self.Frame.place(relx=0.0, rely=0.0, relheight=1.01, relwidth=1.01)
        self.Frame.configure(relief=GROOVE)
        self.Frame.configure(width=605)
        self.Frame.configure(borderwidth="2")
        self.Frame.configure(background="#d9d9d9")

        #Configuration des couleurs

        self.LabelFrame_Couleurs = LabelFrame(self.Frame)
        self.LabelFrame_Couleurs.place(relx=0.03, rely=0.06, relheight=0.74, relwidth=0.53)
        self.LabelFrame_Couleurs.configure(relief=GROOVE)
        self.LabelFrame_Couleurs.configure(foreground="black")
        self.LabelFrame_Couleurs.configure(text="Couleurs")
        self.LabelFrame_Couleurs.configure(background="#d9d9d9")                                                          
        self.LabelFrame_Couleurs.configure(highlightbackground="#d9d9d9")
        self.LabelFrame_Couleurs.configure(highlightcolor="black")
        self.LabelFrame_Couleurs.configure(width=320)
        
        self.Label_Damier = Label(self.LabelFrame_Couleurs)
        self.Label_Damier.place(relx=0.06, rely=0.12, height=21, width=97)
        self.Label_Damier.configure(background="#d9d9d9")
        self.Label_Damier.configure(disabledforeground="#a3a3a3")
        self.Label_Damier.configure(foreground="#000000")
        self.Label_Damier.configure(text="Couleur damier :")

        self.ComboBox_Damier = ttk.Combobox(self.LabelFrame_Couleurs, values = self.Colors)
        self.ComboBox_Damier.place(relx=0.06, rely=0.2, relheight=0.09, relwidth=0.38)
        self.ComboBox_Damier.configure(width=123)
        self.ComboBox_Damier.configure(state = "readonly")

        self.Label_Preview = Label(self.LabelFrame_Couleurs)
        self.Label_Preview.place(relx=0.53, rely=0.12, height=21, width=118)
        self.Label_Preview.configure(background="#d9d9d9")
        self.Label_Preview.configure(disabledforeground="#a3a3a3")
        self.Label_Preview.configure(foreground="#000000")
        self.Label_Preview.configure(text="Couleur du preview :")
        self.Label_Preview.configure(width=118)

        self.ComboBox_Preview = ttk.Combobox(self.LabelFrame_Couleurs, values = self.Colors)
        self.ComboBox_Preview.place(relx=0.53, rely=0.2, relheight=0.09, relwidth=0.38)
        self.ComboBox_Preview.configure(width=123)
        self.ComboBox_Preview.configure(state = "readonly")

        self.Label_CouleurPionNoir = Label(self.LabelFrame_Couleurs)
        self.Label_CouleurPionNoir.place(relx=0.06, rely=0.35, height=21 , width=108)
        self.Label_CouleurPionNoir.configure(background="#d9d9d9")
        self.Label_CouleurPionNoir.configure(disabledforeground="#a3a3a3")
        self.Label_CouleurPionNoir.configure(foreground="#000000")
        self.Label_CouleurPionNoir.configure(text="Couleur pion noir :")

        self.ComboBox_PionNoir = ttk.Combobox(self.LabelFrame_Couleurs, values = self.Colors)
        self.ComboBox_PionNoir.place(relx=0.06, rely=0.43, relheight=0.09, relwidth=0.38)
        self.ComboBox_PionNoir.configure(width=123)
        self.ComboBox_PionNoir.configure(state = "readonly")

        self.Label_CouleurPionBlanc = Label(self.LabelFrame_Couleurs)
        self.Label_CouleurPionBlanc.place(relx=0.53, rely=0.35, height=21, width=116)
        self.Label_CouleurPionBlanc.configure(background="#d9d9d9")
        self.Label_CouleurPionBlanc.configure(disabledforeground="#a3a3a3")
        self.Label_CouleurPionBlanc.configure(foreground="#000000")
        self.Label_CouleurPionBlanc.configure(text="Couleur pion blanc :")

        self.ComboBox_PionBlanc = ttk.Combobox(self.LabelFrame_Couleurs, values = self.Colors)
        self.ComboBox_PionBlanc.place(relx=0.53, rely=0.43, relheight=0.09, relwidth=0.38)
        self.ComboBox_PionBlanc.configure(width=123)
        self.ComboBox_PionBlanc.configure(state = "readonly")

        self.Label_DameBlanc = Label(self.LabelFrame_Couleurs)
        self.Label_DameBlanc.place(relx=0.06, rely=0.59, height=21, width=126)
        self.Label_DameBlanc.configure(background="#d9d9d9")
        self.Label_DameBlanc.configure(disabledforeground="#a3a3a3")
        self.Label_DameBlanc.configure(foreground="#000000")
        self.Label_DameBlanc.configure(text="Couleur dame blanche :")
        self.Label_DameBlanc.configure(width=126)

        self.ComboBox_DameBlanc = ttk.Combobox(self.LabelFrame_Couleurs, values = self.Colors)
        self.ComboBox_DameBlanc.place(relx=0.06, rely=0.67, relheight=0.09, relwidth=0.38)
        self.ComboBox_DameBlanc.configure(width=123)
        self.ComboBox_DameBlanc.configure(state = "readonly")

        self.Label_DameNoir = Label(self.LabelFrame_Couleurs)
        self.Label_DameNoir.place(relx=0.5, rely=0.59, height=21, width=134)
        self.Label_DameNoir.configure(background="#d9d9d9")
        self.Label_DameNoir.configure(disabledforeground="#a3a3a3")
        self.Label_DameNoir.configure(foreground="#000000")
        self.Label_DameNoir.configure(text="Couleur dame noir :")
        self.Label_DameNoir.configure(width=134)

        self.ComboBox_DameNoir = ttk.Combobox(self.LabelFrame_Couleurs, values = self.Colors)
        self.ComboBox_DameNoir.place(relx=0.53, rely=0.67, relheight=0.09, relwidth=0.38)
        self.ComboBox_DameNoir.configure(width=123)
        self.ComboBox_DameNoir.configure(state = "readonly")

        self.Button_Random = tkk.Button(self.LabelFrame_Couleurs, command = self.Random)
        self.Button_Random.place(relx=0.06, rely=0.82, height=24, width=278)
        self.Button_Random.configure(text="Aléatoire")
        self.Button_Random.configure(width=278)

        #Configuration des IA
        self.LabelFrame_Ia = LabelFrame(self.Frame)
        self.LabelFrame_Ia.place(relx=0.58, rely=0.06, relheight=0.19, relwidth=0.4)
        self.LabelFrame_Ia.configure(relief=GROOVE)
        self.LabelFrame_Ia.configure(foreground="black")
        self.LabelFrame_Ia.configure(text="Intelligence artificielle")
        self.LabelFrame_Ia.configure(background="#d9d9d9")
        self.LabelFrame_Ia.configure(highlightbackground="#d9d9d9")
        self.LabelFrame_Ia.configure(highlightcolor="black")
        self.LabelFrame_Ia.configure(width=240)

        self.RadioButton_Ia1 = Radiobutton(self.LabelFrame_Ia, variable = self.IaButton, value = 1)
        self.RadioButton_Ia1.place(relx=0.06, rely=0.38, relheight=0.38, relwidth=0.24)
        self.RadioButton_Ia1.configure(activebackground="#d9d9d9")
        self.RadioButton_Ia1.configure(activeforeground="#000000")
        self.RadioButton_Ia1.configure(background="#d9d9d9")
        self.RadioButton_Ia1.configure(disabledforeground="#a3a3a3")
        self.RadioButton_Ia1.configure(foreground="#000000")
        self.RadioButton_Ia1.configure(highlightbackground="#d9d9d9")
        self.RadioButton_Ia1.configure(highlightcolor="black")
        self.RadioButton_Ia1.configure(justify=LEFT)
        self.RadioButton_Ia1.configure(text="IA 1")

        self.RadioButton_Ia2 = Radiobutton(self.LabelFrame_Ia, variable = self.IaButton, value = 2)
        self.RadioButton_Ia2.place(relx=0.6, rely=0.38, relheight=0.38, relwidth=0.24)
        self.RadioButton_Ia2.configure(activebackground="#d9d9d9")
        self.RadioButton_Ia2.configure(activeforeground="#000000")
        self.RadioButton_Ia2.configure(background="#d9d9d9")
        self.RadioButton_Ia2.configure(disabledforeground="#a3a3a3")
        self.RadioButton_Ia2.configure(foreground="#000000")
        self.RadioButton_Ia2.configure(highlightbackground="#d9d9d9")
        self.RadioButton_Ia2.configure(highlightcolor="black")
        self.RadioButton_Ia2.configure(justify=LEFT)
        self.RadioButton_Ia2.configure(text="IA 2")

        #Configuration des règles
        self.LabelFrame_Regles = LabelFrame(self.Frame)
        self.LabelFrame_Regles.place(relx=0.58, rely=0.26, relheight=0.54 , relwidth=0.4)
        self.LabelFrame_Regles.configure(relief=GROOVE)
        self.LabelFrame_Regles.configure(foreground="black")
        self.LabelFrame_Regles.configure(text="Règles")
        self.LabelFrame_Regles.configure(background="#d9d9d9")
        self.LabelFrame_Regles.configure(highlightbackground="#d9d9d9")
        self.LabelFrame_Regles.configure(highlightcolor="black")
        self.LabelFrame_Regles.configure(width=240)

        self.CheckButton_Dame = Checkbutton(self.LabelFrame_Regles, command = self.CheckButtonDame_Tick)
        self.CheckButton_Dame.place(relx=0.08, rely=0.16, relheight=0.14, relwidth=0.27)
        self.CheckButton_Dame.configure(activebackground="#d9d9d9")
        self.CheckButton_Dame.configure(activeforeground="#000000")
        self.CheckButton_Dame.configure(background="#d9d9d9")
        self.CheckButton_Dame.configure(disabledforeground="#a3a3a3")
        self.CheckButton_Dame.configure(foreground="#000000")
        self.CheckButton_Dame.configure(highlightbackground="#d9d9d9")
        self.CheckButton_Dame.configure(highlightcolor="black")
        self.CheckButton_Dame.configure(justify=LEFT)
        self.CheckButton_Dame.configure(text="Dames")

        self.CheckButton_PriseMultiple = Checkbutton(self.LabelFrame_Regles, command = self.CheckButtonPriseMultiple_Tick)
        self.CheckButton_PriseMultiple.place(relx=0.5, rely=0.16, relheight=0.14, relwidth=0.42)
        self.CheckButton_PriseMultiple.configure(activebackground="#d9d9d9")
        self.CheckButton_PriseMultiple.configure(activeforeground="#000000")
        self.CheckButton_PriseMultiple.configure(background="#d9d9d9")
        self.CheckButton_PriseMultiple.configure(disabledforeground="#a3a3a3")
        self.CheckButton_PriseMultiple.configure(foreground="#000000")
        self.CheckButton_PriseMultiple.configure(highlightbackground="#d9d9d9")
        self.CheckButton_PriseMultiple.configure(highlightcolor="black")
        self.CheckButton_PriseMultiple.configure(justify=LEFT)
        self.CheckButton_PriseMultiple.configure(text="Prise multiple")

        self.CheckButton_PriseObligatoire = Checkbutton(self.LabelFrame_Regles, command = self.CheckButtonPriseObligatoire_Tick)
        self.CheckButton_PriseObligatoire.place(relx=0.08, rely=0.32, relheight=0.14, relwidth=0.45)
        self.CheckButton_PriseObligatoire.configure(activebackground="#d9d9d9")
        self.CheckButton_PriseObligatoire.configure(activeforeground="#000000")
        self.CheckButton_PriseObligatoire.configure(background="#d9d9d9")
        self.CheckButton_PriseObligatoire.configure(disabledforeground="#a3a3a3")
        self.CheckButton_PriseObligatoire.configure(foreground="#000000")
        self.CheckButton_PriseObligatoire.configure(highlightbackground="#d9d9d9")
        self.CheckButton_PriseObligatoire.configure(highlightcolor="black")
        self.CheckButton_PriseObligatoire.configure(justify=LEFT)
        self.CheckButton_PriseObligatoire.configure(text="Prise obligatoire")

        self.CheckButton_Timer = Checkbutton(self.LabelFrame_Regles, command = self.CheckButtonTimer_Tick)
        self.CheckButton_Timer.place(relx=0.53, rely=0.32, relheight=0.14, relwidth=0.47)
        self.CheckButton_Timer.configure(activebackground="#d9d9d9")
        self.CheckButton_Timer.configure(activeforeground="#000000")
        self.CheckButton_Timer.configure(background="#d9d9d9")
        self.CheckButton_Timer.configure(disabledforeground="#a3a3a3")
        self.CheckButton_Timer.configure(foreground="#000000")
        self.CheckButton_Timer.configure(highlightbackground="#d9d9d9")
        self.CheckButton_Timer.configure(highlightcolor="black")
        self.CheckButton_Timer.configure(justify=LEFT)
        self.CheckButton_Timer.configure(text="Timer")


        #Configuration des principaux boutons
        self.Button_Return = tkk.Button(self.Frame, command = self.Open_MainMenuWindow)
        self.Button_Return.place(relx=0.03, rely=0.9, height=24, width=567)
        self.Button_Return.configure(text="Retourner au menu")
        self.Button_Return.configure(width=567)

        self.Button_Save = tkk.Button(self.Frame, command = self.Save)
        self.Button_Save.place(relx=0.03, rely=0.81, height=24, width=567)
        self.Button_Save.configure(text="Sauvegarder")
        self.Button_Save.configure(width=567)

        self.setDefaultColor()
        self.setIaButton()
        self.setRulesButton()
    
    def setDefaultColor(self): #Fonction mettant les couleurs par défaut aux listes déroulantes

        global Couleur_DameBlancCouleur, Couleur_DameNoirCouleur, Couleur_DamierNoir, Couleur_PionBlanc, Couleur_PionNoir, Couleur_PionPreview

        self.ComboBox_Damier.set(Couleur_DamierNoir)
        self.ComboBox_PionBlanc.set(Couleur_PionBlanc)
        self.ComboBox_PionNoir.set(Couleur_PionNoir)
        self.ComboBox_DameBlanc.set(Couleur_DameBlancCouleur)
        self.ComboBox_DameNoir.set(Couleur_DameNoirCouleur)
        self.ComboBox_Preview.set(Couleur_PionPreview)

    def setIaButton(self):

        global IA_Version

        if IA_Version == 1:
            self.RadioButton_Ia1.select()
            self.RadioButton_Ia2.deselect()
        else:
            self.RadioButton_Ia1.deselect()
            self.RadioButton_Ia2.select()

    def setRulesButton(self):
        global Rules_DamesEnable, Rules_PriseMultipleEnable, Rules_PriseObligatoireEnable

        if Rules_DamesEnable:
            self.CheckButton_Dame.select()
        else:
            self.CheckButton_Dame.deselect()

        if Rules_PriseMultipleEnable:
            self.CheckButton_PriseMultiple.select()
        else:
            self.CheckButton_PriseMultiple.deselect()

        if Rules_PriseObligatoireEnable:
            self.CheckButton_PriseObligatoire.select()
        else:
            self.CheckButton_PriseObligatoire.deselect()

        if Rules_Timer:
            self.CheckButton_Timer.select()
        else:
            self.CheckButton_Timer.deselect()
    
    def Save(self): #Fonction sauvegardant les couleurs choisies

        global Couleur_DameBlancCouleur, Couleur_DameNoirCouleur, Couleur_DamierNoir, Couleur_PionBlanc, Couleur_PionNoir, Couleur_PionPreview, IA_Version, Rules_DamesEnable, Rules_PriseMultipleEnable, Rules_PriseObligatoireEnable, Rules_Timer

        #Sauvegarde des couleurs
        Couleur_DameBlancCouleur = self.ComboBox_DameBlanc.get()
        Couleur_DameNoirCouleur = self.ComboBox_DameNoir.get()
        Couleur_DamierNoir = self.ComboBox_Damier.get()
        Couleur_PionBlanc = self.ComboBox_PionBlanc.get()
        Couleur_PionNoir = self.ComboBox_PionNoir.get()
        Couleur_PionPreview = self.ComboBox_Preview.get()

        #Sauvegarde de la version de l'IA
        if self.IaButton.get() == 2 or self.IaButton.get() == 1:
             IA_Version = self.IaButton.get()
        else:
            IA_Version = 1
                    
        #Sauvegarde des règles

        if self.ChkDameEnable == 1:
            Rules_DamesEnable = True
        else:
            Rules_DamesEnable = False   

        if self.ChkPriseMultipleEnable == 1:
            Rules_PriseMultipleEnable = True
        else:
            Rules_PriseMultipleEnable = False

        if self.ChkPriseObligatoireEnable == 1:
            Rules_PriseObligatoireEnable = True
        else:
            Rules_PriseObligatoireEnable = False

        if self.ChkTimerEnable == 1:
            Rules_Timer = True
        else:
            Rules_Timer = False

        self.Open_MainMenuWindow()

    def Random(self): #Fonction choisissant des couleurs aléatoires

        self.ComboBox_DameBlanc.set(random.choice(self.Colors))
        self.ComboBox_DameNoir.set(random.choice(self.Colors))
        self.ComboBox_Damier.set(random.choice(self.Colors))
        self.ComboBox_PionBlanc.set(random.choice(self.Colors))
        self.ComboBox_PionNoir.set(random.choice(self.Colors))
        self.ComboBox_Preview.set(random.choice(self.Colors))

    def CheckButtonDame_Tick(self):
        if self.ChkDameEnable == 1:
            self.ChkDameEnable = 0
        else:
            self.ChkDameEnable = 1

    def CheckButtonPriseObligatoire_Tick(self):
        if self.ChkPriseObligatoireEnable == 1:
            self.ChkPriseObligatoireEnable = 0
        else:
            self.ChkPriseObligatoireEnable = 1

    def CheckButtonPriseMultiple_Tick(self):
        if self.ChkPriseMultipleEnable == 1:
            self.ChkPriseMultipleEnable = 0
        else:
            self.ChkPriseMultipleEnable = 1

    def CheckButtonTimer_Tick(self):
        if self.ChkTimerEnable == 1:
            self.ChkTimerEnable = 0
        else:
            self.ChkTimerEnable = 1

    def Open_MainMenuWindow(self): #Fonction ouvrant le menu principal

        Root.title("Jeu de Dames - Menu Principal")
        self.Hide_Window()
        self.newWindow = Toplevel(self.master)
        self.app = MainMenu(self.newWindow)

    def Hide_Window(self): #Fonction permettant de cacher la fenêtre
        self.master.withdraw()

    def Show_Window(self): #Fonction permettant de réafficher la fenêtre
        self.master.update()
        self.master.deiconify()

    def Close_Window(self): #Fonction permettant de fermer la fenêtre
        self.master.destroy()



class Multijoueur():

    def __init__(self, master):
        self.master = master

        self.isHost = False
        self.Ip = ""
        self.Pseudo = ""

        self.Draw_Interface()

    def Draw_Interface(self):

        self.master.geometry("482x119+427+96")
        self.master.configure(background="#d9d9d9")

        self.Labelframe_Config = LabelFrame(self.master)
        self.Labelframe_Config.place(relx=0.02, rely=0.0, relheight=0.97, relwidth=0.52)
        self.Labelframe_Config.configure(relief=GROOVE)
        self.Labelframe_Config.configure(foreground="black")
        self.Labelframe_Config.configure(text="Configuration")
        self.Labelframe_Config.configure(background="#d9d9d9")
        self.Labelframe_Config.configure(width=250)

        self.Entry_Ip = ttk.Entry(self.Labelframe_Config)
        self.Entry_Ip.place(relx=0.35, rely=0.14, relheight=0.20, relwidth=0.58)
        self.Entry_Ip.configure(width=146)
        self.Entry_Ip.configure(cursor="ibeam")

        self.Label_Ip = ttk.Label(self.Labelframe_Config)
        self.Label_Ip.place(relx=0.04, rely=0.15, height=19, width=76)
        self.Label_Ip.configure(background="#d9d9d9")
        self.Label_Ip.configure(foreground="#000000")
        self.Label_Ip.configure(relief=FLAT)
        self.Label_Ip.configure(text="Adresse IP :")

        self.Checkbutton_Host = Checkbutton(self.Labelframe_Config, command = self.CheckBoxHost_Tick)
        self.Checkbutton_Host.place(relx=0.02, rely=0.42, relheight=0.22, relwidth=0.32)
        self.Checkbutton_Host.configure(activebackground="#d9d9d9")
        self.Checkbutton_Host.configure(activeforeground="#000000")
        self.Checkbutton_Host.configure(background="#d9d9d9")
        self.Checkbutton_Host.configure(disabledforeground="#a3a3a3")
        self.Checkbutton_Host.configure(foreground="#000000")
        self.Checkbutton_Host.configure(highlightbackground="#d9d9d9")
        self.Checkbutton_Host.configure(highlightcolor="black")
        self.Checkbutton_Host.configure(justify=LEFT)
        self.Checkbutton_Host.configure(text="Etre l'hôte")

        self.Label_MyIp = ttk.Label(self.Labelframe_Config)
        self.Label_MyIp.place(relx=0.02, rely=0.69, height=19, width=216)
        self.Label_MyIp.configure(background="#d9d9d9")
        self.Label_MyIp.configure(foreground="#000000")
        self.Label_MyIp.configure(relief=FLAT)
        self.Label_MyIp.configure(text="Mon adresse IP : 127.0.0.1")

        self.Labelframe_ConfigPlayer = LabelFrame(self.master)
        self.Labelframe_ConfigPlayer.place(relx=0.56, rely=0.0, relheight=0.46, relwidth=0.41)
        self.Labelframe_ConfigPlayer.configure(relief=GROOVE)
        self.Labelframe_ConfigPlayer.configure(foreground="black")
        self.Labelframe_ConfigPlayer.configure(text="Joueur")
        self.Labelframe_ConfigPlayer.configure(background="#d9d9d9")
        self.Labelframe_ConfigPlayer.configure(width=200)

        self.Label_Pseudo = ttk.Label(self.Labelframe_ConfigPlayer)
        self.Label_Pseudo.place(relx=0.05, rely=0.2, height=19, width=56)
        self.Label_Pseudo.configure(background="#d9d9d9")
        self.Label_Pseudo.configure(foreground="#000000")
        self.Label_Pseudo.configure(text="Pseudo :")

        self.Entry_Pseudo = ttk.Entry(self.Labelframe_ConfigPlayer)
        self.Entry_Pseudo.place(relx=0.33, rely=0.18, relheight=0.55, relwidth=0.63)
        self.Entry_Pseudo.configure(cursor="ibeam")

        self.Button_Launch = ttk.Button(self.master, command = self.Launch_Multiplayer)
        self.Button_Launch.place(relx=0.56, rely=0.5, height=25, width=196)
        self.Button_Launch.configure(text="Lancer")

        self.Button_Return = ttk.Button(self.master, command = self.Open_MainMenuWindow)
        self.Button_Return.place(relx=0.56, rely=0.75, height=25, width=196)
        self.Button_Return.configure(text="Retourner au menu")

    def Launch_Multiplayer(self):
        if self.Entry_Ip.get() == "" and self.isHost == False:
            messagebox.showerror("Erreur", "Vous devez indiquer une adresse IP !", parent = self.master)
        elif self.Entry_Pseudo.get() == "":
            messagebox.showerror("Erreur", "Vous devez entrer un pseudo !", parent = self.master)
        else:
            print("Lancement du multijoueur...")
            self.Pseudo = self.Entry_Pseudo.get()
            self.Ip = self.Entry_Ip.get()
            if self.isHost:
                self.Launch_Host()
            else:
                self.Launch_Client()

    def Launch_Host(self):
        print("Launching host...")

    def Launch_Client(self):
        print("Launching client...")



    def ResetUi(self):
        self.Checkbutton_Host.deselect()
    
    def CheckBoxHost_Tick(self):
        if self.isHost == 0:
            self.isHost = 1
        else:
            self.isHost = 0

        if self.isHost == 1:
            self.Entry_Ip.configure(state = DISABLED)
        else:
            self.Entry_Ip.configure(state = ACTIVE)

    def Open_MainMenuWindow(self): #Fonction ouvrant le menu principal
        self.ResetUi()
        Root.title("Jeu de Dames - Menu Principal")
        self.Hide_Window()
        self.newWindow = Toplevel(self.master)
        self.app = MainMenu(self.newWindow)

    def Hide_Window(self): #Fonction permettant de cacher la fenêtre
        self.master.withdraw()


class Jeu(): #Classe représentant l'interface du jeu de dames
    
    def __init__(self, master, nbrJoueurs): #Initialisation de l'interface et de la classe

        global timeLeft

        self.master = master
        self.frame = Frame(master)
         
        self.nbrJoueurs = nbrJoueurs

        self.can = Canvas(self.frame, width = 500, height = 500, bg = "ivory")
        self.can.pack(side = RIGHT, padx = 0, pady =0)

        self.can.bind('<Button-1>', self.mouse_down) #On attribue le clic de la souris au canvas

        self.draw_Interface()

        self.GEng = GameEngine(self.can, self.master)
        
        self.frame.pack()

        self.Update_Timer() #On lance le timer du jeu

        if self.nbrJoueurs == 1:
            self.Label_Joueur2.config(text = "-- Joueur 2 (Ia) --")
            self.GEng.StartGame(1)
        else:
            self.GEng.StartGame(2)
    
    def draw_Interface(self): #Fonction dessinant l'interface principale
        
        global Label_NbrPionsJ1, Label_NbrPionsJ2, Label_TourActuel, timeLeft, Label_Timer, Button_SkipTour
        
        #Stockage du texte
        
        self.nbrPionsRestantsJ1_Text = "Nombre de pions restants : 20"
        self.nbrPionsRestantsJ2_Text = "Nombre de pions restants : 20"
        self.tourActuel = "Equipe jouant : Blanc"
        
        # -- Affichage du texte --
        self.Label_Joueur1 = Label(self.frame, text = "-- Joueur 1 --")
        self.Label_Joueur1.pack()
        Label_NbrPionsJ1 = Label(self.frame, text = self.nbrPionsRestantsJ1_Text)
        Label_NbrPionsJ1.pack()
        self.Label_Joueur2 = Label(self.frame, text = "-- Joueur 2 --")
        self.Label_Joueur2.pack()
        Label_NbrPionsJ2 = Label(self.frame, text = self.nbrPionsRestantsJ2_Text)
        Label_NbrPionsJ2.pack()
        self.Label_Separation = Label(self.frame, text = "-------------------")
        self.Label_Separation.pack()
        Label_TourActuel = Label(self.frame, text = self.tourActuel)
        Label_TourActuel.pack()
        Label_Timer = Label(self.frame, text = "Temps restant : {}.{}".format(self.ConvertTime(timeLeft, False), self.ConvertTime(timeLeft, True)))
        Label_Timer.pack(pady = 10)
        
        #-- Affichage des boutons
        self.Button_ReturnToMenu = tkk.Button(self.frame, text = "Retourner au menu", command = self.Open_MainMenuWindow)
        self.Button_ReturnToMenu.pack(side = BOTTOM, pady =3)
        self.Button_Restart = tkk.Button(self.frame, text='Redémarrer', command = self.Restart_Game)
        self.Button_Restart.pack(side = BOTTOM, padx =3, pady =3)
        Button_SkipTour = tkk.Button(self.frame, text='Passer le tour', command = self.Skip_Turn)
        Button_SkipTour.pack(side = BOTTOM, padx =5, pady =5)
        

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
    
    def Restart_Game(self): #Fonction redémarrant la partie
        global priseMultiple
        if priseMultiple == False:
            print("Restarting game !") 
            self.Update_Timer()
            if self.nbrJoueurs == 1:
                self.GEng.StartGame(1)
            else:
                self.GEng.StartGame(2)

    def Skip_Turn(self): #Fonction permettant de sauter son tour en jeu
        global priseMultiple
        if priseMultiple == False:
            print("Skipping turn !")
            self.GEng.Tour(True, True, True)

    def Close_Window(self): #Fonction permettant de fermer la fenêtre
        self.master.destroy()

    def Update_Timer(self): #Fonction mettant à jour le timer de jeu et l'interface si le jeu est fini
        global timeLeft, Label_Timer, hasGameFinished, Root, Rules_Timer

        if hasGameFinished == False and Rules_Timer == True:
            if timeLeft <= 0:
                self.Skip_Turn()
            timeLeft -= 1000
            Label_Timer.config(text = "Temps restant : {}.{}".format(self.ConvertTime(timeLeft, False), self.ConvertTime(timeLeft, True)))

        Root.after(1000, self.Update_Timer)
    
    def ConvertTime(self, timeLeft, toSeconds):
        if toSeconds == True:
            return int((timeLeft/1000)%60)
        else:
            return int((timeLeft/(1000*60))%60)



class Player(): #Classe représentant un joueur
    
    def __init__(self, NomJoueur, Equipe, nbrPions, isAi):

        self.NomJoueur = NomJoueur
        self.Equipe = Equipe
        self.nbrPions = nbrPions
        self.isAi = isAi
        self.Pions = ""

class Case(): #Classe représentant une case du damier
    
    def __init__(self, Couleur, PosX, PosY, Status, Equipe):
        self.Couleur = Couleur
        self.PosX = PosX
        self.PosY = PosY
        self.Status = Status
        self.Equipe = Equipe
        
class GameEngine(): #Classe représentant le moteur du jeu
    
    def __init__(self, canvas, master):

        global priseMultiple

        self.teamToPlay = "Blanc" #Variable de l'équipe en train de jouer

        self.canvas = canvas        
        self.master = master

        self.TableauPions = [None] * 100 #Tableau de tout les pions du damier
        self.TableauJoueurs = [None] * 2 #Tableau des 2 joueurs
                
        self.isPionSelect = False #Si un pion est sélectionné
        self.pionSelect = 99 #L'id du pion sélectionné

        self.CercleChoixPossible = [] #Liste contenant les objets des cercles de choix possible
        self.RectanglePriseObligatoire = [] #Liste contenant les rectangles de la prise obligatoire afin de pouvoir les supprimer
        self.listePionGraphique = [] #Stockage des pions pour l'Anti-Lag

        self.ListeCaseChoixPossible = [] #Liste contenant les numéros des cases possibles
        self.listePionCanTake = [] #Liste des pions qui peuvent en prendre d'autre
        self.listePionWhoCanTake = []  #Pareil
        self.ListePionsPossibleToMove = []

        self.hasAlreadyCheckedTake = False #Si on a déjà regardé la prise obligatoire
        self.caseIdPionSelect = 0 #Id de la case du pion sélectionné
      
        self.priseMultiple = priseMultiple #On regarde si on est dans une situation de prise multiple
        self.CasePriseMultiple = 0 #Case finale pour la prise multiple

    def StartGame(self, nombreJoueurs): #Fonction se lançant au début de la partie

        global Rules_DamesEnable, Rules_PriseMultipleEnable, Rules_PriseObligatoireEnable, Button_SkipTour, hasGameFinished, timeLeft

        print("Démarrage / Redémarrage du jeu")

        print("Règles : ")
        print("Prise multiple : ", Rules_PriseMultipleEnable)
        print("Prise obligatoire : ", Rules_PriseObligatoireEnable)
        print("Dames : ", Rules_DamesEnable)

        self.teamToPlay = "Blanc" #On force à jouer les blancs en cas de redémarrage
        Button_SkipTour.configure(state = ACTIVE)
        hasGameFinished = False

        self.canvas.delete() #On efface tout

        #On génère par défaut les pions et les joueurs
        self.GenerateTableauPion() 
        self.GenerateTableauPlayer(nombreJoueurs)

        #On met à jour l'ensemble
        self.Refresh(False)
    
    def UpdateGui(self): #Fonction permettant de mettre à jour le texte de l'interface

        print("Mise à jour de l'interface !")

        global Label_NbrPionsJ1, Label_NbrPionsJ2, Label_TourActuel

        #On met à jour le nombre de pions de chaque équipe ainsi que l'équipe jouant actuellement
        Label_NbrPionsJ1.config(text= "Nombre de pions restants : {}".format(self.TableauJoueurs[0].nbrPions))
        Label_NbrPionsJ2.config(text= "Nombre de pions restants : {}".format(self.TableauJoueurs[1].nbrPions))
        Label_TourActuel.config(text= "Equipe jouant : {}".format(self.teamToPlay))
        
    def Refresh(self, SwitchTurn): #Fonction permettant de rafraichir le damier avec les nouvelles positions des pions


        #Anti-Lag / On supprime le maximum pour redéssiner ensuite
        self.delete("caseDamier1")
        self.delete("caseDamier2")
        self.canvas.delete(ALL)

        #On réaffiche le damier et les pions à leurs nouvelle position
        self.showDamier()
        self.showTerrainFromPionPlace()

        #Si c'est un nouveau tour on en change sinon on actualise juste
        if SwitchTurn == True:
            self.Tour(True, False, True)
        else:
            self.Tour(False, False, False)
    
    def IA(self):
        global IA_Version

        if IA_Version == 1:
            self.IA_1()
        else:
            self.IA_2()

    def IA_1(self):
        print("IA 1 !")
        pionWhoCanMove = []
        
        
        pionToMove = random.choice(pionWhoCanMove)


        self.movePion(pionToMove, "DiagGaucheBas", pionToMove + 11, False)
            
        
    #Fonctions utilitaires pour l'IA 1

    def maxMinBoard(self, currentDepth, bestMove):
        best_move = bestMove
        best_board = None

        if best_move == float("-inf"):
            moves = ""


    def GetMoves(self, team):
        if team == "Blanc" or team == "Noir":
            pionWhoCanMove = []
            for i in range(len(self.TableauPions)):
                if self.TableauPions[i].Couleur == team:
                    self.showPlaceToGo(i, False)
            return self.ListePionsPossibleToMove


    def isWin(self):
        if self.TableauJoueurs[0].nbrPions == 0 or self.TableauJoueurs[1].nbrPions == 0:
            return True
        else:
            return False
            
    def IA_2(self):
        print("IA 2 !")

        listeInterdit = [0, 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 31, 33, 35, 37, 39, 40, 42, 44, 46, 48, 51, 53, 55, 57, 59, 60, 62, 64, 66, 68, 71, 73, 75, 77, 79, 80, 82, 84, 86, 88, 91, 93, 95, 97, 99] #Cases ou les pions ne pourront jamais aller

        self.selectPion_OnClick(0, 0) #On refresh le tableau de prise obligatoire

        pionCanMove = self.GetMoves("Noir")

        print(pionCanMove)

        pionSelect = random.choice(pionCanMove) 

        self.showPlaceToGo(pionSelect, True)

        caseSelect = random.choice(self.ListeCaseChoixPossible)

        while self.TableauPions[pionSelect].Couleur != "Noir" and caseSelect not in listeInterdit:
            pionSelect = random.choice(pionCanMove) 

        self.movePion(pionSelect, "DiagGaucheBas", caseSelect, False)

        self.Tour(True, False, False)

    def Tour(self, newTurn, isSkip, playIa): #Fonction s'executant à la fin de chaque tour
        
        global timeLeft, hasGameFinished, Button_SkipTour

        self.hasAlreadyCheckedTake = False
        self.ListePionsPossibleToMove = []

        if self.TableauJoueurs[0].nbrPions == 0 or self.TableauJoueurs[1].nbrPions == 0:
            hasGameFinished = True
            Button_SkipTour.configure(state = DISABLED)
            if self.TableauJoueurs[0].nbrPions == 0:
                messagebox.showinfo("Gagné !!!", "J2 a gagné !", parent = self.master)
            elif self.TableauJoueurs[1].nbrPions == 0:
                messagebox.showinfo("Gagné !!!", "J1 a gagné !", parent = self.master)


        self.isPionSelect = False
        self.pionSelect = 0
        self.deleteMoveGraphObject()

        if (self.TableauJoueurs[0].isAi == True or self.TableauJoueurs[1].isAi == True) and playIa == True:
            self.IA()

        if newTurn == True:

            if (self.teamToPlay == "Blanc") or (self.teamToPlay == "Blanc" and self.isSkip == True):
                self.teamToPlay = "Noir"
            else:
                self.teamToPlay = "Blanc"

        timeLeft = 180000                   
        self.UpdateGui()
            

    def GenerateTableauPion(self): #Fonction gérant la position initiale des pions
        
        PosX = -25
        PosY = 25
        i = 0

        while i < 100:
            PosX += 50
            if i < 10 or (i >= 20 and i < 30):
                self.TableauPions[i] = Case("Null", PosX, PosY, "Null", "0")
                PosX += 50
                self.TableauPions[i+1] = Case("Noir", PosX, PosY, "Pion", "1")
            elif (i >= 10 and i <= 20) or (i >= 30 and i < 40):
                self.TableauPions[i] = Case("Noir", PosX, PosY, "Pion", "1")
                PosX += 50
                self.TableauPions[i+1] = Case("Null", PosX, PosY, "Null", "0")
            elif i >= 40 and i < 60:
                self.TableauPions[i] = Case("Null", PosX, PosY, "Null", "0")
                PosX += 50
                self.TableauPions[i+1] = Case("Null", PosX, PosY, "Null", "0")
            elif (i >= 60 and i < 70) or (i >= 80 and i < 90):
                self.TableauPions[i] = Case("Null", PosX, PosY, "Null", "0")
                PosX += 50
                self.TableauPions[i+1] = Case("Blanc", PosX, PosY, "Pion", "2")
            elif (i >= 70 and i <= 80) or i >= 90:
                self.TableauPions[i] = Case("Blanc", PosX, PosY, "Pion", "2")
                PosX += 50
                self.TableauPions[i+1] = Case("Null", PosX, PosY, "Null", "0")
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
    
    
    def movePion(self, PionSelect, Direction, CaseFinale, switchTurn): #Fonction gérant le déplacement des pions

        global priseMultiple, Rules_PriseMultipleEnable

        self.priseMultiple = False
        pionToMove = PionSelect
        CaseFinale = CaseFinale
        isMove = False
        pionDirection = Direction
        numberChange = 0
        
        #On vérifie si le pion existe
        if self.TableauPions[pionToMove].Status == "Null":
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

        self.PlaySound("Data/Sounds/Move.wav")

        self.canvas.focus()
        self.canvas.move(self.canvas.find_closest(self.TableauPions[PionSelect].PosX, self.TableauPions[PionSelect].PosY), self.TableauPions[CaseFinale].PosX - self.TableauPions[PionSelect].PosX, self.TableauPions[CaseFinale].PosY - self.TableauPions[PionSelect].PosY)

        #Déplacement du pion

        TempV = self.TableauPions[CaseFinale]
        TempOld = self.TableauPions[pionToMove]

        PosXNew = TempOld.PosX
        PosYNew = TempOld.PosY

        self.TableauPions[CaseFinale] = self.TableauPions[pionToMove]
        self.TableauPions[CaseFinale].PosX = TempV.PosX
        self.TableauPions[CaseFinale].PosY = TempV.PosY

        TempV.PosX = PosXNew
        TempV.PosY = PosYNew

        self.TableauPions[pionToMove] = TempV

        if self.TableauPions[CaseFinale].Status == "Dame":

            elementToMultiply = 0

            for i in range(9):

                elementToMultiply += 1
                caseActuelle = CaseFinale - (numberChange * elementToMultiply)
                if caseActuelle < 100 and caseActuelle > 0:
                    if (self.TableauPions[caseActuelle].Status != "Null" and self.TableauPions[caseActuelle].Equipe != self.TableauPions[CaseFinale].Equipe):
                        
                        if self.TableauPions[caseActuelle].Equipe == "1":
                            self.TableauJoueurs[0].nbrPions -= 1
                        else:
                            self.TableauJoueurs[1].nbrPions -= 1
                       
                        self.TableauPions[caseActuelle].Status = "Null"
                        self.TableauPions[caseActuelle].Couleur = "Null"
                        self.TableauPions[caseActuelle].Equipe = "0"                 

                        isMove = True
                        break

        elif self.TableauPions[CaseFinale].Status != "Null" and self.TableauPions[CaseFinale].Equipe != self.TableauPions[pionToMove + (numberChange)].Equipe:
            
              self.TableauPions[pionToMove + (numberChange)].Status = "Null"
              self.TableauPions[pionToMove + (numberChange)].Couleur = "Null"
              self.TableauPions[pionToMove + (numberChange)].Equipe = 0

              if self.TableauPions[CaseFinale].Equipe == "1":
                  self.TableauJoueurs[1].nbrPions -= 1
              else:
                  self.TableauJoueurs[0].nbrPions -= 1

              isMove = True

              CaseFinale = pionToMove + (numberChange * 2)

        #On regarde si on peut transformer le pion en dame

        if isMove == False:
            self.CheckTransformatonDame(pionToMove + (numberChange))
        else:

            #On regarde si il y a possiblité de prise multiple après une prise

            if Rules_PriseMultipleEnable:
                self.priseMultiple = True
                priseMultiple = self.priseMultiple
                self.isPionSelect = True
                self.pionSelect = CaseFinale
                self.CasePriseMultiple = CaseFinale

                if self.showPlaceToGo(CaseFinale, False) == "PionCanBeTake":
                    self.Refresh(False)
                    return

            self.CheckTransformatonDame(pionToMove + (numberChange * 2))

        self.priseMultiple = False
        priseMultiple = self.priseMultiple

        if switchTurn:
            self.Refresh(True)
        else:
            self.Refresh(False)
   
    def CheckTransformatonDame(self, PionSelect): #Fonction qui regarde si les pions doivent se transformer en dames

        global Rules_DamesEnable

        pionSelect = PionSelect
        if Rules_DamesEnable:
            if self.TableauPions[pionSelect].Status == "Pion":
                if (pionSelect >= 90 and self.TableauPions[pionSelect].Equipe == "1") or (pionSelect <= 9 and self.TableauPions[pionSelect].Equipe == "2"):
                    self.TableauPions[pionSelect].Status = "Dame"
    
    def showTerrainFromPionPlace(self): #Fonction qui affiche les pions en fonction du tableau

        global Couleur_PionBlanc, Couleur_PionNoir, Couleur_DameBlancCouleur, Couleur_DameNoirCouleur, Couleur_DamierNoir, Use_Texture

        i = 0 
        x = 0
        cercleX = -25
        cercleY = 25    

        self.listePionGraphique = []

        while i < len(self.TableauPions): #Selon le status de chaque pion dans le tableau on l'affiche graphiquement sur le damier           
            x = 0
            while x < 10: #Pour chaque case d'une ligne
                cercleX += 50
                if self.TableauPions[i].Status != "Null":
                    if self.TableauPions[i].Couleur == "Blanc" and self.TableauPions[i].Status == "Dame":
                        if Use_Texture == False:
                            self.listePionGraphique.append(self.cercle(cercleX, cercleY, 25, Couleur_PionBlanc))
                            self.listePionGraphique.append(self.cercle(cercleX, cercleY, 20, Couleur_DameBlancCouleur))
                        else:
                            self.listePionGraphique.append(self.Create_Image(cercleX, cercleY, image = os.path.dirname(os.path.realpath(__file__)) + "\Data\Graphics\Pion.png"))
                    elif self.TableauPions[i].Couleur == "Noir" and self.TableauPions[i].Status == "Dame":
                        if Use_Texture == False:
                            self.listePionGraphique.append(self.cercle(cercleX, cercleY, 25, Couleur_PionNoir))
                            self.listePionGraphique.append(self.cercle(cercleX, cercleY, 20, Couleur_DameNoirCouleur))
                        else:
                            self.listePionGraphique.append(self.Create_Image(cercleX, cercleY, image = os.path.dirname(os.path.realpath(__file__)) + "\Data\Graphics\Pion.png"))
                    elif self.TableauPions[i].Couleur == "Blanc":
                        if Use_Texture == False:
                            self.listePionGraphique.append(self.cercle(cercleX, cercleY, 20, Couleur_PionBlanc))
                        else:
                            self.listePionGraphique.append(self.Create_Image(cercleX, cercleY, image = "\Pion.gif"))
                    elif self.TableauPions[i].Couleur == "Noir":
                        if Use_Texture == False:
                            self.listePionGraphique.append(self.cercle(cercleX, cercleY, 20, Couleur_PionNoir))
                        else:
                            self.listePionGraphique.append(self.Create_Image(cercleX, cercleY, image = "\Pion.gif"))
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
        
        global Rules_PriseObligatoireEnable

        #Suppression des formes géométriques si elles sont déjà créer
        self.deleteMoveGraphObject()   
          
        #Debug
        #print("PosX % 100 = ", PosX % 100)
        #print("PosY % 100 = ", PosY % 100)
     
        #On obtient l'id de la case en fonction d'où l'on a cliqué
        caseIdClicked = self.getCaseIdByPos(PosX, PosY)

        #Si un pion est déjà sélectionner on regarde où on peut l'envoyer
        if self.isPionSelect == True:

            if self.TableauPions[self.caseIdPionSelect].PosY < PosY :
                if self.TableauPions[self.caseIdPionSelect].PosX < PosX and caseIdClicked in self.ListeCaseChoixPossible:
                    self.movePion(self.pionSelect, "DiagDroiteBas", caseIdClicked, True)
                elif self.TableauPions[self.caseIdPionSelect].PosX > PosX and caseIdClicked in self.ListeCaseChoixPossible:
                    self.movePion(self.pionSelect, "DiagGaucheBas", caseIdClicked, True)
            else:
                if self.TableauPions[self.caseIdPionSelect].PosX < PosX and caseIdClicked in self.ListeCaseChoixPossible:
                    self.movePion(self.pionSelect, "DiagDroiteHaut", caseIdClicked, True)
                elif self.TableauPions[self.caseIdPionSelect].PosX > PosX and caseIdClicked in self.ListeCaseChoixPossible:
                    self.movePion(self.pionSelect, "DiagGaucheHaut", caseIdClicked, True) 

            if self.priseMultiple == False:
                self.isPionSelect = False
                self.pionSelect = 99
                return
                
        if Rules_PriseObligatoireEnable:
            if self.hasAlreadyCheckedTake != True and self.priseMultiple == False:
                self.listePionWhoCanTake = self.checkIfPionCanBeTake()

            if self.listePionWhoCanTake != [] and self.priseMultiple == False:
                self.deleteMoveGraphObject()
                if caseIdClicked not in self.listePionWhoCanTake:
                    for i in self.listePionWhoCanTake:
                        print("Create rectangle...")
                        self.RectanglePriseObligatoire = []            
                        self.RectanglePriseObligatoire.append(self.canvas.create_rectangle(self.roundint(self.TableauPions[i].PosX, 50), self.roundint(self.TableauPions[i].PosY, 50), self.roundint(self.TableauPions[i].PosX, 50) + 50, self.roundint(self.TableauPions[i].PosY, 50) + 50 , outline = "red", width = 3, tags = "rectanglePionObligatoire"))           
                    return
        

        self.pionSelect = 0

        print(caseIdClicked)

        if self.TableauPions[caseIdClicked].Couleur == self.teamToPlay:
            self.pionSelect = caseIdClicked
        else:
            self.pionSelect = 102
            self.isPionSelect = False
        
        if self.pionSelect < 101 and self.TableauPions[caseIdClicked].Status != "Null": 
         
            if (self.priseMultiple == True and self.CasePriseMultiple == self.pionSelect) or self.priseMultiple == False:
                self.caseIdPionSelect = self.pionSelect
                self.isPionSelect = True
            
                self.canvas.create_rectangle(self.roundint(PosX, 50), self.roundint(PosY, 50), self.roundint(PosX, 50) + 50, self.roundint(PosY, 50) + 50 , outline = "yellow", width = 3, tags = "rectangleSelectPion")
            
                self.showPlaceToGo(self.pionSelect, True)

    def checkIfPionCanBeTake(self):
        print("Check pion obligatoire..")
        self.listePionCanTake = []
        self.checkObligatoire = True
        for i in range(len(self.TableauPions)):
            if self.TableauPions[i].Couleur == self.teamToPlay and (self.TableauPions[i].Status == "Pion" or self.TableauPions[i].Status == "Dame"):
                if self.showPlaceToGo(i, False):
                    self.listePionCanTake.append(i)
        self.hasAlreadyCheckedTake = True
        self.checkObligatoire = False
        return self.listePionCanTake

    def getCaseIdByPos(self, PosX, PosY): #Fonction permettant d'obtenir l'id d'un pion en fonction de l'emplacement clické
        PosXMod = PosX % 100
        PosYmod = PosY % 100
        for i in range(len(self.TableauPions)):
            if ((PosXMod) > 25 and (PosYmod) > 25) or ((PosXMod) > 25 and (PosYmod) < 25) or ((PosXMod) < 25 and (PosYmod) > 25):
                if (self.TableauPions[i].PosX == self.roundint(PosX, 25) or self.TableauPions[i].PosX == self.roundint(PosX, 25) + 25) and (self.TableauPions[i].PosY == self.roundint(PosY, 25) or self.TableauPions[i].PosY == self.roundint(PosY, 25) + 25):
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    return i
            elif (PosXMod) < 25 and (PosYmod) > 25:
                if self.TableauPions[i].PosX == self.roundint(PosX, 25) + 25 and self.TableauPions[i].PosY == self.roundint(PosY, 25):
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    return i
            elif (PosYmod) < 25:
                if self.TableauPions[i].PosX == self.roundint(PosX, 25) + 25 and self.TableauPions[i].PosY == self.roundint(PosY, 25) + 25:
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    return i
            if (PosXMod) < 25:
                if self.TableauPions[i].PosX == self.roundint(PosX, 25) + 25 and self.TableauPions[i].PosY == self.roundint(PosY, 25) + 25:
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    return i
            else:
                if self.TableauPions[i].PosX == self.roundint(PosX, 25) and self.TableauPions[i].PosY == self.roundint(PosY, 25):
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    return i
        return 99 #Si l'on ne trouve aucun pion

    def deleteMoveGraphObject(self): #Fonction qui permet de supprimer les éléments graphiques relatifs à la selection d'un pion
        self.delete("rectangleSelectPion")
        self.delete("rectanglePionObligatoire")
        for i in range(len(self.CercleChoixPossible)):
            self.canvas.delete(self.CercleChoixPossible[i])
        for i in range(len(self.RectanglePriseObligatoire)):
            self.canvas.delete(self.RectanglePriseObligatoire[i])

    def showPlaceToGo(self, pionSelect, drawCircle): #Montre les endroits possibles sur le damier

        global Couleur_PionPreview

        pionSelect = pionSelect #Variable qui contiendra l'id du pion sélectionner
        canTakePion = False #Variable permettant de savoir si l'on peut prendre un pion

        listeInterdit = [0, 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 31, 33, 35, 37, 39, 40, 42, 44, 46, 48, 51, 53, 55, 57, 59, 60, 62, 64, 66, 68, 71, 73, 75, 77, 79, 80, 82, 84, 86, 88, 91, 93, 95, 97, 99] #Cases ou les pions ne pourront jamais aller
        listeCheck = [-9, -11, 9, 11]
        listeCheckDynamic = []
        
        listePionsPossiblesDame = []

        self.CercleChoixPossible = [] #Tableau contenant les positions des cercles qui indiquent les choix possibles
        self.ListeCaseChoixPossible = []

        if self.TableauPions[pionSelect].Equipe == "1": #Si les blancs jouent on descend les pions vers le bas

            listeCheckDynamic.append(9)
            listeCheckDynamic.append(11)

        elif self.TableauPions[pionSelect].Equipe == "2": #Sinon on regarde vers le haut
            listeCheckDynamic.append(-9)
            listeCheckDynamic.append(-11)

        #Système de preview de déplacement des dames

        if self.TableauPions[pionSelect].Status == "Dame":

            for i in listeCheck: #On regarde chaque diagonale
                numberToMultiply = -1 #Nombre à multiplier
                nbrPions = 0
                while numberToMultiply > -9: #On regarde sur toutes les cases de la diagonale
                    caseActuelle = pionSelect + (i * (numberToMultiply))
                    if caseActuelle < 100 and caseActuelle > 0:
                        if self.TableauPions[caseActuelle].Status != "Null": #Si l'on rencontre un pion
                            if self.TableauPions[caseActuelle].Couleur != self.teamToPlay: #S'il est ennemi 
                                nbrPions +=1 
                            else: #Sinon s'il est allié
                                nbrPions += 2

                        if nbrPions == 1 and self.TableauPions[caseActuelle].Status == "Null" and caseActuelle not in listeInterdit: #Si un pion
                            listePionsPossiblesDame.append(caseActuelle)
                            canTakePion = True
                    
                    numberToMultiply -= 1

            if canTakePion:
                for i in listePionsPossiblesDame:
                    if drawCircle:
                        self.CercleChoixPossible.append(self.canvas.create_oval(self.TableauPions[i].PosX - 5, self.TableauPions[i].PosY - 5, self.TableauPions[i].PosX + 5, self.TableauPions[i].PosY + 5, fill = Couleur_PionPreview))
                    self.ListeCaseChoixPossible.append(i) 
            else:
                for i in listeCheck:
                    numberToMultiply = 1
                    nbrPions = 0
                    while numberToMultiply < 9:
                        caseActuelle = pionSelect + (i * (numberToMultiply))
                        if caseActuelle < 100 and caseActuelle > 0:
                            if self.TableauPions[caseActuelle].Status != "Null":
                                nbrPions += 1

                            if self.TableauPions[caseActuelle].Status == "Null" and nbrPions == 0 and caseActuelle not in listeInterdit:
                                if drawCircle:
                                    self.CercleChoixPossible.append(self.canvas.create_oval(self.TableauPions[caseActuelle].PosX - 5, self.TableauPions[caseActuelle].PosY - 5, self.TableauPions[caseActuelle].PosX + 5, self.TableauPions[caseActuelle].PosY + 5, fill = Couleur_PionPreview))
                                self.ListeCaseChoixPossible.append(caseActuelle) 
                        numberToMultiply += 1

        #Système de preview des pions normaux

        if self.TableauPions[pionSelect].Status == "Pion":
            for i in listeCheck: #On regarde si on peux manger un pion
                   if pionSelect + (i * 2) < 100 and pionSelect + (i * 2) > 0:
                        if (self.TableauPions[pionSelect + (i)].Status == "Pion" or self.TableauPions[pionSelect + (i)].Status == "Dame") and self.TableauPions[pionSelect + (i * 2)].Status == "Null" and self.TableauPions[pionSelect + (i)].Equipe != self.TableauPions[pionSelect].Equipe and pionSelect + (i) not in listeInterdit and pionSelect + (i * 2) not in listeInterdit:   
                           if drawCircle:
                                self.CercleChoixPossible.append(self.canvas.create_oval(self.TableauPions[pionSelect + (i * 2)].PosX - 5, self.TableauPions[pionSelect + (i * 2)].PosY - 5, self.TableauPions[pionSelect + (i * 2)].PosX + 5, self.TableauPions[pionSelect + (i * 2)].PosY + 5, fill= Couleur_PionPreview))
                           self.ListeCaseChoixPossible.append(pionSelect + (i * 2))
                           self.ListePionsPossibleToMove.append(pionSelect)
                           canTakePion = True
        
        if self.priseMultiple != True and canTakePion != True and self.TableauPions[pionSelect].Status == "Pion":
            for i in listeCheckDynamic:
                if pionSelect + (i) < 100 and pionSelect + (i) > 0:
                    if self.TableauPions[pionSelect + (i)].Status == "Null" and pionSelect + (i) not in listeInterdit:
                       if drawCircle:
                            self.CercleChoixPossible.append(self.canvas.create_oval(self.TableauPions[pionSelect + (i)].PosX - 5, self.TableauPions[pionSelect + (i)].PosY - 5,  self.TableauPions[pionSelect + (i)].PosX + 5, self.TableauPions[pionSelect + (i)].PosY + 5, fill= Couleur_PionPreview))
                       self.ListeCaseChoixPossible.append(pionSelect + (i))
                       self.ListePionsPossibleToMove.append(pionSelect)

        if self.priseMultiple == True and self.ListeCaseChoixPossible != [] and canTakePion == True:
            return "PionCanBeTake"
        elif self.priseMultiple == True:
            return "NoPionCanBeTake"
               
        if canTakePion:
            return True
        else:
            return False
    
    def PlaySound(self, FileName):
        print("Playing sound !")
        
        file = FileName

        if sys.platform.startswith('win'): #Si on est sous windows on lance le son

            from winsound import PlaySound, SND_FILENAME, SND_ASYNC
            PlaySound(file, SND_FILENAME|SND_ASYNC)

        elif sys.platform.find('linux')>-1: #Sinon on lance avec la librairie linux

            from wave import open as waveOpen
            from ossaudiodev import open as ossOpen

            s = waveOpen('tada.wav','rb')
            (nc,sw,fr,nf,comptype, compname) = s.getparams( )
            dsp = ossOpen('/dev/dsp','w')
            try:
                print("..")
                from ossaudiodev import AFMT_S16_NE

            except ImportError:
                if byteorder == "little":
                    AFMT_S16_NE = ossaudiodev.AFMT_S16_LE
                else:
                    AFMT_S16_NE = ossaudiodev.AFMT_S16_BE

            dsp.setparameters(AFMT_S16_NE, nc, fr)
            data = s.readframes(nf)
            s.close()
            dsp.write(data)
            dsp.close()  

# --- Fonctions Graphiques et utilitaires ---

    def roundint(self, value, base=5): #Fonction permettant d'arrondir
        return int(value) - int(value) % int(base)
    
    def delete(self, MonTag): #Fonction permettant de supprimer des objets graphiques en fonction d'un tag
        self.canvas.delete(self.canvas.find_withtag(MonTag))

    def cercle(self, x, y, r, coul, tagsC = "cercle"): #Fonction permettant de tracer un cercle
        return self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=coul, tags="cercleChoixPos")
    
    def Rectangle(self, x, y, coul): #Fonction permettant de tracer un rectangle
        self.canvas.create_rectangle(x + 20, x+20, y + 20, y+20, outline=coul)

    def Create_Image(self, x, y, image):
        ImageU = PhotoImage(file = os.path.dirname(os.path.realpath(__file__)) + image)
        return self.canvas.create_image(x, y, image = ImageU)

        
## -- Programme Principal --

Root = Tk() #Variable principale

#Boucle principale
cls = MainMenu(Root)
Root.mainloop()