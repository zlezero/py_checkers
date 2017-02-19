class Player():
    
    def __init__(self, NomJoueur, Equipe, Pions):
        self.NomJoueur = NomJoueur
        self.Equipe = Equipe
        self.Pions = Pions
        

class Pion():
    
    def __init__(self, Couleur, PosX, PosY, Status, Equipe):
        self.Couleur = Couleur
        self.PosX = PosX
        self.PosY = PosY
        self.Status = Status
        self.Equipe = Equipe

class Case():
    def __init__(self, PosX, PosY, Status):
        self.PosX = PosX
        self.PosY = PosY
        self.Status = Status
        
class GameEngine():
    
    def __init__(self, canvas):
        
        self.teamToPlay = "Black"
        self.canvas = canvas
        
        # self.TableauDames = [Case(25, 25, "Null"), Case(75, 25, Pion("Blanc", 75, 25, "Pion", "1")), Case(25, 25, "Null"), Case(125, 25, Pion("Blanc", 125, 25, "Pion", "1")), Case(25,             25, "Null"), Case(175, 25, Pion("Blanc", 175, 25, "Pion", "1")), Case(25, 25, "Null"), Case(225, 25, Pion("Blanc", 225, 25, "Pion", "1")), Case(25, 25, "Null"), Case(275, 25, Pion("Blanc", 275, 25, "Pion", "1")), #0 to 9
        #                      Case(75, 75, Pion("Blanc", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(125, 75, Pion("Blanc", 125, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Blanc", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Blanc", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Blanc", 75, 75, "Pion", "1")), Case(25, 25, "Null"), #10 to 19
        #                      Case(25, 25, "Null"), Case(75, 75, Pion("Blanc", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Blanc", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Blanc", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Blanc", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Blanc", 75, 75, "Pion", "1")), #20 to 29
        #                      Case(75, 75, Pion("Blanc", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Blanc", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Blanc", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Blanc", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Blanc", 75, 75, "Pion", "1")), Case(25, 25, "Null"), #30 to 39        
        #                      
        #                      Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), #40 to 49
        #                      Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), Case(25, 25, "Null"), #50 to 59   #0 = Vide
        #                      
        #                      Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), #60 to 69   #1 = Pion Noir
        #                      Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), #70 to 79   #2 = Pion Noir                                                                            
        #                      Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), #80 to 89   #3 = Dame Noirhe
        #                      Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null"), Case(75, 75, Pion("Noir", 75, 75, "Pion", "1")), Case(25, 25, "Null")] #90 to 99   #4 = Dame Noire

       
        
        self.TableauDames = [Pion("Null", 25, 25, "Null", "0"), Pion("Blanc", 75, 25, "Pion", "1"), Pion("Null", 125, 25, "Null", "0"), Pion("Blanc", 175, 25, "Pion", "1"), Pion("Null",           225, 25, "Null", "0"), Pion("Blanc", 275, 25, "Pion", "1"), Pion("Null", 325, 25, "Null", "0"), Pion("Blanc", 375, 25, "Pion", "1"), Pion("Null", 425, 25, "Null", "0"), Pion("Blanc", 475, 25, "Pion", "1"), #0 à 9
                             Pion("Blanc", 25, 75, "Pion", "1"), Pion("Null", 75, 75, "Null", "0"), Pion("Blanc", 125, 75, "Pion", "1"), Pion("Null", 175, 75, "Null", "0"), Pion("Blanc", 225, 75, "Pion", "1"), Pion("Null", 275, 75, "Null", "0"), Pion("Blanc", 325, 75, "Pion", "1"), Pion("Null", 375, 75, "Null", "0"), Pion("Blanc", 425, 75, "Pion", "1"), Pion("Null", 475, 75, "Null", "0"), #10 à 19
                             Pion("Null", 25, 75, "Null", "0"), Pion("Blanc", 75, 25, "Pion", "1"), Pion("Null", 25, 75, "Null", "0"), Pion("Blanc", 75, 25, "Pion", "1"), Pion("Null", 25, 75, "Null", "0"), Pion("Blanc", 75, 25, "Pion", "1"), Pion("Null", 25, 75, "Null", "0"), Pion("Blanc", 75, 25, "Pion", "1"), Pion("Null", 25, 75, "Null", "0"), Pion("Blanc", 75, 25, "Pion", "1"), #20 à 29
                             Pion("Blanc", 75, 25, "Pion", "1"), Pion("Null", 25, 75, "Null", "0"), Pion("Blanc", 75, 25, "Pion", "1"), Pion("Null", 25, 75, "Null", "0"), Pion("Blanc", 75, 25, "Pion", "1"), Pion("Null", 25, 75, "Null", "0"), Pion("Blanc", 75, 25, "Pion", "1"), Pion("Null", 25, 75, "Null", "0"), Pion("Blanc", 75, 25, "Pion", "1"), Pion("Null", 25, 75, "Null", "0"), #30 à 39
                             Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), #40 à 49
                             Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), Pion("Null", 25, 75, "Null", "0"), #50 à 59
                             Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), #60 à 69
                             Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), #70 à 79
                             Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), #80 à 89
                             Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0"), Pion("Noir", 75, 75, "Pion", "2"), Pion("Null", 25, 75, "Null", "0")] #90 à 99
        
        
    def StartGame(self, nombreJoueurs):
        self.Refresh()
    
    def Refresh(self):
        self.showDamier()
        self.showTerrainFromPionPlace()
    
    def movePion(PionSelect, Direction):
        
        pionToMove = PionSelect
        pionDirection = Direction
        numberChange = 0
        
        #On vérifie si le pion existe
        if self.TableauDames[pionToMove] == 0:
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
        if self.TableauDames[pionToMove + (numberChange)] == 0: #Si l'endroit ou le pion doit aller est vide
            if self.TableauDames[pionToMove] == 1: #On bouge le pion en fonction de son équipe
                self.TableauDames[pionToMove + (numberChange)] = 1
            else:
                self.TableauDames[pionToMove + (numberChange)] = 2
            self.TableauDames[pionToMove] = 0
            print("DEBUG : New pos :", pionToMove + (numberChange))
        elif self.TableauDames[pionToMove + (numberChange)] == 2 and self.TableauDames[pionToMove] == 1: #On regarde si on peut prendre un pion
            if self.TableauDames[pionToMove + (numberChange * 2)] == 0: #Si une case est libre après le pion
                self.TableauDames[pionToMove + (numberChange * 2)] = 1 #On bouge le pion
                self.TableauDames[pionToMove + (numberChange)] = 0 #On élimine le pion adverse
                self.TableauDames[pionToMove] = 0 #On supprime le pion de son emplacement d'origine
                print("DEBUG : New pos :", pionToMove + (numberChange * 2))
                print("Pion pris !")
            else: #Si un emplacement est indisponible on ne peut pas prendre le pion
                print("Impossible de prendre le pion !")
        elif self.TableauDames[pionToMove + (numberChange)] == 1 and self.TableauDames[pionToMove] == 2:
            if self.TableauDames[pionToMove + (numberChange * 2)] == 0:
                self.TableauDames[pionToMove + (numberChange * 2)] = 2            
                self.TableauDames[pionToMove + (numberChange)] = 0
                self.TableauDames[pionToMove] = 0
                print("DEBUG : New pos :", pionToMove + (numberChange * 2))
                print("Pion pris !")
            else:
                print("Impossible de prendre le pion !")
        else:
            print("Déplacement impossible !")
        
        
        
        self.showTerrain()
        self.showTerrainFromPionPlace()
    
    
    def showTerrainFromPionPlace(self): #Fonction qui affiche les pions en fonction du tableau
        i = 0 
        x = 0
        cercleX = -25
        cercleY = 25    
        while i < len(self.TableauDames):
            x = 0
            while x < 10:
                cercleX += 50
                if self.TableauDames[i].Status != "Null":
                    if self.TableauDames[i].Couleur == "Blanc" and self.TableauDames[i].Status == "Dame":
                        self.cercle(cercleX, cercleY, 25, "blue")
                        self.cercle(cercleX, cercleY, 20, "yellow")
                    elif self.TableauDames[i].Couleur == "Noir" and self.TableauDames[i].Status == "Dame":
                        self.cercle(cercleX, cercleY, 25, "blue")
                        self.cercle(cercleX, cercleY, 20, "green")
                    elif self.TableauDames[i].Couleur == "Blanc":
                        self.cercle(cercleX, cercleY, 20, "yellow")
                    elif self.TableauDames[i].Couleur == "Noir":
                        self.cercle(cercleX, cercleY, 20, "green")
                    
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
                        self.canvas.create_rectangle(x+50, y, x+100, y + 50, fill='black')
                        x += 100       
                    x = -100
                    y += 100
            else: #Sinon on les décales
                while y < 470: #On boucle tant que l'on a pas fait chacune des lignes
                    while x < 390: #On boucle tant que l'on a pas fini chaque carré d'une ligne
                        self.canvas.create_rectangle(x+100, y+50, x+150, y + 100, fill='black')
                        x += 100
                    x = -100
                    y += 100
            line += 1
        
    def Reset():
        self.TableauDames = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, #0 to 10
                        1, 0, 1, 0, 1, 0, 1, 0, 1, 0, #10 to 20
                        0, 1, 0, 1, 0, 1, 0, 1, 0, 1, #20 to 30
                        1, 0, 1, 0, 1, 0, 1, 0, 1, 0, #30 to 40
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, #40 to 50
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, #50 to 60
                        0, 2, 0, 2, 0, 2, 0, 2, 0, 2, #60 to 70
                        2, 0, 2, 0, 2, 0, 2, 0, 2, 0, #70 to 80
                        0, 2, 0, 2, 0, 2, 0, 2, 0, 2, #80 to 90
                        2, 0, 2, 0, 2, 0, 2, 0, 2, 0] #90 to 100
    
    def Tour():
        teamToPlay = "Black"
        showTerrain()
        x = 0
        while x == 0:
            if teamToPlay == "Black":
                teamToPlay = "White"
            else:
                teamToPlay = "Black"
            canPlay = True
            if teamToPlay == "Black":
                print("L'équipe noire joue !")
            else:
                print("L'équipe blanche joue !")
            while canPlay:
                idPion = int(input("Entrez l'id du pion a jouer :"))
                if teamToPlay == "Black":
                    if self.TableauDames[idPion] != 1:
                        print("Vous ne pouvez pas jouer ceci !")
                    else:
                        canPlay = False
                else:
                    if self.TableauDames[idPion] != 2:
                        print("Vous ne pouvez pas jouer ceci !")
                    else:
                        canPlay = False
            canPlay = True
            while canPlay:
                Direction = input("Entrez la direction DiagDroiteHaut/DiagGaucheHaut/DiagDroiteBas/DiagGaucheBas :")
                if Direction == "DiagDroiteHaut" or Direction == "DiagGaucheGaut" or Direction == "DiagDroiteBas" or Direction == "DiagGaucheBas":
                    movePion(idPion, Direction)
                    canPlay = False
                    showTerrainFromPionPlace()
                    x = 1
                else:
                    print("Direction inconnue !")
    
    def GetWinner():
        nbrWhite = 0
        nbrBlack = 0
        for i in range(len(self.TableauDames)):
            if self.TableauDames[i] == 1:
                nbrBlack += 1
            elif self.TableauDames[i] == 2:
                nbrWhite += 1
        if nbrWhite == 0:
            print("Black Win !")
            return "BWin"
        elif nbrBlack == 0:
            print("White Win !")
            return "WWin"
        else:
            return False
            
    
    def showTerrain():
        tableauTemp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        i = 0
        removeId = 0
        while i < len(self.TableauDames):
            x = 0  
            while x < 10:
                if self.TableauDames[i] == 0:
                    tableauTemp[i - removeId] = "O"
                elif self.TableauDames[i] == 1:
                    tableauTemp[i - removeId] = "B"
                elif self.TableauDames[i] == 2:
                    tableauTemp[i - removeId] = "W"
                i += 1
                x += 1
            removeId += 10
            print(tableauTemp)
    
    def selectPion_OnClick(self, PosX, PosY):
        print(PosX)
        print(PosY)
        self.Rectangle(PosX, PosY, "blue")


# --- Fonctions Graphiques ---

    def cercle(self, x, y, r, coul): #Fonction permettant de tracer un cercle
        "tracé d ' un cercle de centre (x,y) et de rayon r"
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=coul)
    
    def Rectangle(self, x, y, coul): #Fonction permettant de tracer un rectangle
        self.canvas.create_rectangle(x, x, y, y, outline=coul)



