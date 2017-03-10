import time
from tkinter import *

##Variables de l'interface graphique et de jeu

Label_NbrPionsJ1 = None
Label_NbrPionsJ2 = None
Label_TourActuel = None
Label_Timer = None
timeLeft = 180000

## -- Toutes les différentes GUI --

class MainMenu(): #Classe représentant le menu principal
    
    def __init__(self, master): #Initialisation de l'interface et de la classe

        self.master = master
        self.frame = Frame(master)

        Root.title("Jeu de Dames - Menu Principal")
        
        self.Draw_Interface()
        
        self.frame.pack()
    
    def Draw_Interface(self):
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
        self.TableauCaseChoixPossible = []
        self.caseIdPionSelect = 0
        
        self.listePionGraphique = []
        
        self.BlancSkip = True
        self.NoirSkip = True

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
    
    
    def movePion(self, PionSelect, Direction): #Fonction gérant le déplacement des pions
        
        pionToMove = PionSelect
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
            print("lul")
        
        if self.TableauDames[pionToMove + (numberChange)].Status == "Null": #Si l'endroit ou le pion doit aller est vide
        
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
                
                print("DEBUG : New pos :", pionToMove + (numberChange * 2))
                print("Pion pris !")
                
            else: #Si un emplacement est indisponible on ne peut pas prendre le pion
                print("Impossible de prendre le pion !")
        else:
            print("Déplacement impossible !")
            return
        
        if isMove == False:
            self.CheckTransformatonDame(pionToMove + (numberChange))
            if self.showPlaceToGo(pionToMove + (numberChange), True) == "PionCanBeTake":
                self.Refresh(False)
        else:
            self.CheckTransformatonDame(pionToMove + (numberChange * 2))
            if self.showPlaceToGo((pionToMove + (numberChange * 2)), True) == "PionCanBeTake":
                self.Refresh(False)
        

        self.Refresh(True)
    
    def CheckTransformatonDame(self, PionSelect): #Fonction qui regarde si les pions doivent se transformer en dames

        pionSelect = PionSelect
        
        if self.TableauDames[pionSelect].Status == "Pion":
            if (pionSelect > 90 and self.TableauDames[pionSelect].Equipe == "1") or (pionSelect < 11 and self.TableauDames[pionSelect].Equipe == "2"):
                self.TableauDames[pionSelect].Status = "Dame"
    
    def showTerrainFromPionPlace(self): #Fonction qui affiche les pions en fonction du tableau
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
                        self.listePionGraphique.append(self.cercle(cercleX, cercleY, 25, "red"))
                        self.listePionGraphique.append(self.cercle(cercleX, cercleY, 20, "ivory"))
                    elif self.TableauDames[i].Couleur == "Noir" and self.TableauDames[i].Status == "Dame":
                        self.listePionGraphique.append(self.cercle(cercleX, cercleY, 25, "red"))
                        self.listePionGraphique.append(self.cercle(cercleX, cercleY, 20, "brown"))
                    elif self.TableauDames[i].Couleur == "Blanc":
                        self.listePionGraphique.append(self.cercle(cercleX, cercleY, 20, "ivory"))
                    elif self.TableauDames[i].Couleur == "Noir":
                        self.listePionGraphique.append(self.cercle(cercleX, cercleY, 20, "brown"))                  
                i += 1
                x += 1
            cercleX = -25
            cercleY += 50
            
    def showDamier(self): #Fonction qui trace un damier
        x = -100
        y = -50
        line = 0
        while line <= 10: #On boucle tant que toutes les lignes n'ont pas été tracées
            y = 0
            if line % 2 == 0: #Si le numéro de ligne est impaire on les places normalement
                while y < 500: #On boucle tant que l'on a pas fait chacune des lignes
                    while x < 500: #On boucle tant que l'on a pas fini chaque carré d'une ligne
                        self.canvas.create_rectangle(x+50, y, x+100, y + 50, fill='black', tags = "caseDamier1")
                        x += 100       
                    x = -100
                    y += 100
            else: #Sinon on les décales
                while y < 470: #On boucle tant que l'on a pas fait chacune des lignes
                    while x < 390: #On boucle tant que l'on a pas fini chaque carré d'une ligne
                        self.canvas.create_rectangle(x+100, y+50, x+150, y + 100, fill='black', tags = "caseDamier2")
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

            #if PosY > self.caseIdPionSelect
            if self.TableauDames[self.caseIdPionSelect].PosY < PosY :
                if self.TableauDames[self.caseIdPionSelect].PosX < PosX and caseIdClicked in self.TableauCaseChoixPossible:
                    self.movePion(self.pionSelect, "DiagDroiteBas")
                elif self.TableauDames[self.caseIdPionSelect].PosX > PosX and caseIdClicked in self.TableauCaseChoixPossible:
                    self.movePion(self.pionSelect, "DiagGaucheBas")
            else:
                if self.TableauDames[self.caseIdPionSelect].PosX < PosX and caseIdClicked in self.TableauCaseChoixPossible:
                    self.movePion(self.pionSelect, "DiagDroiteHaut")
                elif self.TableauDames[self.caseIdPionSelect].PosX > PosX and caseIdClicked in self.TableauCaseChoixPossible:
                    self.movePion(self.pionSelect, "DiagGaucheHaut") 

            self.isPionSelect = False
            self.pionSelect = 99
            return
            
        self.pionSelect = 0

        print(self.getCaseIdByPos(PosX, PosY))

        if self.TableauDames[caseIdClicked].Couleur == self.teamToPlay:
            self.pionSelect = caseIdClicked
        else:
            self.pionSelect = 102
            self.isPionSelect = False
        
        if self.pionSelect < 101 and self.TableauDames[caseIdClicked].Status != "Null":            
            self.caseIdPionSelect = self.pionSelect
            self.isPionSelect = True
            
            self.canvas.create_rectangle(self.roundint(PosX, 50), self.roundint(PosY, 50), self.roundint(PosX, 50) + 50, self.roundint(PosY, 50) + 50 , outline = "yellow", width = 3, tags = "rectangleSelectPion")
            
            self.showPlaceToGo(self.pionSelect, False)

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
        return 99

    def deleteMoveGraphObject(self):
        self.delete("rectangleSelectPion")
        for i in range(len(self.CercleChoixPossible)):
            self.canvas.delete(self.CercleChoixPossible[i])

    def showPlaceToGo(self, pionSelect, checkMultiPrise): #Montre les endroits possibles sur le damier
        
        
        pionSelect = pionSelect #Variable qui contiendra l'id du pion sélectionner
        
        listeInterdit = [0, 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 31, 33, 35, 37, 39, 40, 42, 44, 46, 48, 51, 53, 55, 57, 59, 60, 62, 64, 66, 68, 71, 73, 75, 77, 79, 80, 82, 84, 86, 88, 91, 93, 95, 97, 99] #Cases ou les pions ne pourront jamais aller
        
        listeCheck = [-11, -9, 9, 11]

        self.CercleChoixPossible = [] #Tableau contenant les positions des cercles qui indiquent les choix possibles
        self.TableauCaseChoixPossible = []

        if self.TableauDames[pionSelect].Equipe == "1": #Si les blancs jouent on descend les pions vers le bas
            numberChange2 = 9           
            numberChange1 = 11

        elif self.TableauDames[pionSelect].Equipe == "2": #Sinon on regarde vers le haut
            numberChange1 = -9
            numberChange2 = -11
            
        #Système de preview de déplacement des dames

        if self.TableauDames[pionSelect].Status == "Dame":
            for i in listeCheck:
                numberToMutiply = 1
                nbrPions = 0
                while numberToMutiply < 8:
                    if pionSelect + (i * numberToMutiply) < 99 and pionSelect + (i * numberToMutiply) > 1:
                        if self.TableauDames[pionSelect + (i * numberToMutiply)].Status == "Null" and pionSelect + (i * numberToMutiply) not in listeInterdit:
                            if nbrPions == 0 or nbrPions == 1:
                                self.CercleChoixPossible.append(self.canvas.create_oval(self.TableauDames[pionSelect + (i * numberToMutiply)].PosX - 5, self.TableauDames[pionSelect + (i * numberToMutiply)].PosY - 5, self.TableauDames[pionSelect + (i * numberToMutiply)].PosX + 5, self.TableauDames[pionSelect + (i * numberToMutiply)].PosY + 5, fill= "yellow"))
                                self.TableauCaseChoixPossible.append(pionSelect + (i * numberToMutiply))    
                                if self.TableauDames[pionSelect + (i * (numberToMutiply - 1))].Status == "Pion" or self.TableauDames[pionSelect + (i * (numberToMutiply - 2))].Status == "Pion":
                                    nbrPions += 2
                    numberToMutiply += 1
            return
         
        #Système de preview des pions normaux

        for i in listeCheck: #On regarde si on peux manger un pion
               if pionSelect + (i * 2) < 100 and pionSelect + (i * 2) > 1:
                    if self.TableauDames[pionSelect + (i)].Status == "Pion" and self.TableauDames[pionSelect + (i * 2)].Status == "Null" and self.TableauDames[pionSelect + (i)].Equipe != self.TableauDames[pionSelect].Equipe and pionSelect + (i) not in listeInterdit and pionSelect + (i * 2) not in listeInterdit:   
                       self.CercleChoixPossible.append(self.canvas.create_oval(self.TableauDames[pionSelect + (i * 2)].PosX - 5, self.TableauDames[pionSelect + (i * 2)].PosY - 5, self.TableauDames[pionSelect + (i * 2)].PosX + 5, self.TableauDames[pionSelect + (i * 2)].PosY + 5, fill= "yellow"))
                       self.TableauCaseChoixPossible.append(pionSelect + (i * 2))

        if checkMultiPrise != True:

            if pionSelect + (numberChange1) < 100 or pionSelect + (numberChange2) < 100 and pionSelect + (numberChange1) > 0 or pionSelect + (numberChange2) > 0:
            
                if self.TableauDames[pionSelect + (numberChange1)].Status == "Null" and (pionSelect + numberChange1) not in listeInterdit: #Si la case est vide

                    self.CercleChoixPossible.append(self.canvas.create_oval(self.TableauDames[pionSelect + (numberChange1)].PosX - 5, self.TableauDames[pionSelect + (numberChange1)].PosY - 5,  self.TableauDames[pionSelect + (numberChange1)].PosX + 5, self.TableauDames[pionSelect + (numberChange1)].PosY + 5, fill= "yellow"))
                
                    self.TableauCaseChoixPossible.append(pionSelect + (numberChange1))
                                
                if (self.TableauDames[pionSelect + (numberChange2)].Status == "Null" and (pionSelect + numberChange2) not in listeInterdit): #Si la case est vide
                
                    self.CercleChoixPossible.append(self.canvas.create_oval(self.TableauDames[pionSelect + (numberChange2)].PosX - 5, self.TableauDames[pionSelect + (numberChange2)].PosY - 5, self.TableauDames[pionSelect + (numberChange2)].PosX + 5, self.TableauDames[pionSelect + (numberChange2)].PosY + 5, fill= "yellow"))
               
                    self.TableauCaseChoixPossible.append(pionSelect + (numberChange2))


        if checkMultiPrise == True and self.TableauCaseChoixPossible != []:
            return "PionCanBeTake"
        elif checkMultiPrise == True:
            return "NoPionCanBeTake"
         
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
        

        
    
