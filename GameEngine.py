from tkinter import messagebox

class Player():
    
    def __init__(self, NomJoueur, Equipe, nbrPions, isAi):
        self.NomJoueur = NomJoueur
        self.Equipe = Equipe
        self.nbrPions = nbrPions
        self.isAi = isAi
        self.Pions = ""

class Pion():
    
    def __init__(self, Couleur, PosX, PosY, Status, Equipe):
        self.Couleur = Couleur
        self.PosX = PosX
        self.PosY = PosY
        self.Status = Status
        self.Equipe = Equipe
        
class GameEngine():
    
    def __init__(self, canvas, texte):
        
        self.teamToPlay = "Noir"
        self.canvas = canvas        
        self.TableauDames = [None] * 100
        self.TableauJoueurs = [None] * 2
        
        self.Texte = texte
        
        self.isPionSelect = False
        self.pionSelect = 99
        self.CercleChoixPossible = []
        self.TableauCaseChoixPossible = []
    
    def StartGame(self, nombreJoueurs):
        print("Start / Restart Game")
        self.canvas.delete()
        self.GenerateTableauDames()
        self.GenerateTableauPlayer(nombreJoueurs)
        self.Refresh()
    
    def UpdateGui(self):        
        print("Refresh !")
    
    def Refresh(self):
        self.UpdateGui()
        self.showDamier()
        self.showTerrainFromPionPlace()
        self.Tour(True)
    
    
    def Tour(self, newTurn):
        if self.TableauJoueurs[0].nbrPions == 0:
            messagebox.showinfo("Gagné !!!", "J2 Won")
        elif self.TableauJoueurs[1].nbrPions == 0:
            messagebox.showinfo("Gagné !!!", "J1 Won")
            
        if newTurn == True:
            if self.teamToPlay == "Blanc":
                self.teamToPlay = "Noir"
            else:
                self.teamToPlay = "Blanc"

    def GenerateTableauDames(self):
        
        PosX = -25
        PosY = 25
        i = 0
        
        while i < 100:
            PosX += 50
            if i < 10 or (i >= 20 and i < 30):
                self.TableauDames[i] = Pion("Null", PosX, PosY, "Null", "0")
                PosX += 50
                self.TableauDames[i+1] = Pion("Blanc", PosX, PosY, "Pion", "1")
            elif (i >= 10 and i <= 20) or (i >= 30 and i < 40):
                self.TableauDames[i] = Pion("Blanc", PosX, PosY, "Pion", "1")
                PosX += 50
                self.TableauDames[i+1] = Pion("Null", PosX, PosY, "Null", "0")
            elif i >= 40 and i < 60:
                self.TableauDames[i] = Pion("Null", PosX, PosY, "Null", "0")
                PosX += 50
                self.TableauDames[i+1] = Pion("Null", PosX, PosY, "Null", "0")
            elif (i >= 60 and i < 70) or (i >= 80 and i < 90):
                self.TableauDames[i] = Pion("Null", PosX, PosY, "Null", "0")
                PosX += 50
                self.TableauDames[i+1] = Pion("Noir", PosX, PosY, "Pion", "2")
            elif (i >= 70 and i <= 80) or i >= 90:
                self.TableauDames[i] = Pion("Noir", PosX, PosY, "Pion", "2")
                PosX += 50
                self.TableauDames[i+1] = Pion("Null", PosX, PosY, "Null", "0")
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
    
    
    def movePion(self, PionSelect, Direction):
        
        pionToMove = PionSelect
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
        
        if self.TableauDames[pionToMove + (numberChange)].Status == "Null": #Si l'endroit ou le pion doit aller est vide
        
            TempV = self.TableauDames[pionToMove + (numberChange)]
            TempOld = self.TableauDames[pionToMove]
            
            self.TableauDames[pionToMove + (numberChange)] = self.TableauDames[pionToMove]
            
            self.TableauDames[pionToMove + (numberChange)].PosX = TempV.PosX
            self.TableauDames[pionToMove + (numberChange)].PosY = TempV.PosY
            
            TempV.PosX = TempOld.PosX
            TempV.PosY = TempOld.PosY
            
            self.TableauDames[pionToMove] = TempV
            
            print("DEBUG : New pos :", pionToMove + (numberChange))
            
        elif self.TableauDames[pionToMove + (numberChange)].Equipe == 2 and self.TableauDames[pionToMove].Equipe == 1: #On regarde si on peut prendre un pion
        
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
            return
        
        
        
        self.Refresh()
    
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
                        self.cercle(cercleX, cercleY, 20, "ivory")
                    elif self.TableauDames[i].Couleur == "Noir" and self.TableauDames[i].Status == "Dame":
                        self.cercle(cercleX, cercleY, 25, "blue")
                        self.cercle(cercleX, cercleY, 20, "green")
                    elif self.TableauDames[i].Couleur == "Blanc":
                        self.cercle(cercleX, cercleY, 20, "ivory")
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



## Fonctions utilisée lorsque l'on clique 

    def selectPion_OnClick(self, PosX, PosY): 
        
        
        self.delete("rectangleSelectPion")
        for i in range(len(self.CercleChoixPossible)):
            self.canvas.delete(self.CercleChoixPossible[i])

        
        print("PosX % 100 = ", PosX % 100)
        print("PosY % 100 = ", PosY % 100)
        
        if self.isPionSelect == True:
            for i in range(len(self.TableauCaseChoixPossible)):
                if ((PosX % 100) > 25 and (PosY % 100) > 25) or ((PosX % 100) > 25 and (PosY % 100) < 25):
                    if (self.TableauCaseChoixPossible[i].PosX == self.roundint(PosX, 25) or self.TableauCaseChoixPossible[i].PosX == self.roundint(PosX, 25) + 25):
                        if self.TableauCaseChoixPossible[i].PosX % 100 < PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 > PosY % 100:
                            self.movePion(self.pionSelect, "DiagGaucheBas")
                            break
                        elif self.TableauCaseChoixPossible[i].PosX % 100 < PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 < PosY % 100:
                            self.movePion(self.pionSelect, "DiagGaucheHaut")
                            break
                        elif self.TableauCaseChoixPossible[i].PosX % 100 > PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 > PosY % 100:
                            self.movePion(self.pionSelect, "DiagDroiteBas")
                            break
                        elif self.TableauCaseChoixPossible[i].PosX % 100 > PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 < PosY % 100:
                            self.movePion(self.pionSelect, "DiagDroiteHaut")
                            break
                       
                            
                elif (PosX % 100) < 25 and (PosY % 100) > 25:
                    if ((PosX % 100) > 25 and (PosY % 100) > 25) or ((PosX % 100) > 25 and (PosY % 100) < 25):
                        if (self.TableauCaseChoixPossible[i].PosX == self.roundint(PosX, 25) or self.TableauCaseChoixPossible[i].PosX == self.roundint(PosX, 25) + 25):
                            if self.TableauCaseChoixPossible[i].PosX % 100 < PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 > PosY % 100:
                                self.movePion(self.pionSelect, "DiagGaucheBas")
                                break
                            elif self.TableauCaseChoixPossible[i].PosX % 100 < PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 < PosY % 100:
                                self.movePion(self.pionSelect, "DiagGaucheHaut")
                                break
                            elif self.TableauCaseChoixPossible[i].PosX % 100 > PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 > PosY % 100:
                                self.movePion(self.pionSelect, "DiagDroiteBas")
                                break
                            elif self.TableauCaseChoixPossible[i].PosX % 100 > PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 < PosY % 100:
                                self.movePion(self.pionSelect, "DiagDroiteHaut")
                                break
                elif (PosY % 100) < 25:
                    if ((PosX % 100) > 25 and (PosY % 100) > 25) or ((PosX % 100) > 25 and (PosY % 100) < 25):
                        if (self.TableauCaseChoixPossible[i].PosX == self.roundint(PosX, 25) or self.TableauCaseChoixPossible[i].PosX == self.roundint(PosX, 25) + 25):
                            if self.TableauCaseChoixPossible[i].PosX % 100 < PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 > PosY % 100:
                                self.movePion(self.pionSelect, "DiagGaucheBas")
                                break
                            elif self.TableauCaseChoixPossible[i].PosX % 100 < PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 < PosY % 100:
                                self.movePion(self.pionSelect, "DiagGaucheHaut")
                                break
                            elif self.TableauCaseChoixPossible[i].PosX % 100 > PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 > PosY % 100:
                                self.movePion(self.pionSelect, "DiagDroiteBas")
                                break
                            elif self.TableauCaseChoixPossible[i].PosX % 100 > PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 < PosY % 100:
                                self.movePion(self.pionSelect, "DiagDroiteHaut")
                                break
                if (PosX % 100) < 25:
                    if ((PosX % 100) > 25 and (PosY % 100) > 25) or ((PosX % 100) > 25 and (PosY % 100) < 25):
                        if (self.TableauCaseChoixPossible[i].PosX == self.roundint(PosX, 25) or self.TableauCaseChoixPossible[i].PosX == self.roundint(PosX, 25) + 25):
                            if self.TableauCaseChoixPossible[i].PosX % 100 < PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 > PosY % 100:
                                self.movePion(self.pionSelect, "DiagGaucheBas")
                                break
                            elif self.TableauCaseChoixPossible[i].PosX % 100 < PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 < PosY % 100:
                                self.movePion(self.pionSelect, "DiagGaucheHaut")
                                break
                            elif self.TableauCaseChoixPossible[i].PosX % 100 > PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 > PosY % 100:
                                self.movePion(self.pionSelect, "DiagDroiteBas")
                                break
                            elif self.TableauCaseChoixPossible[i].PosX % 100 > PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 < PosY % 100:
                                self.movePion(self.pionSelect, "DiagDroiteHaut")
                                break
                else:
                    if ((PosX % 100) > 25 and (PosY % 100) > 25) or ((PosX % 100) > 25 and (PosY % 100) < 25):
                        if (self.TableauCaseChoixPossible[i].PosX == self.roundint(PosX, 25) or self.TableauCaseChoixPossible[i].PosX == self.roundint(PosX, 25) + 25):
                            if self.TableauCaseChoixPossible[i].PosX % 100 < PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 > PosY % 100:
                                self.movePion(self.pionSelect, "DiagGaucheBas")
                                break
                            elif self.TableauCaseChoixPossible[i].PosX % 100 < PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 < PosY % 100:
                                self.movePion(self.pionSelect, "DiagGaucheHaut")
                                break
                            elif self.TableauCaseChoixPossible[i].PosX % 100 > PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 > PosY % 100:
                                self.movePion(self.pionSelect, "DiagDroiteBas")
                                break
                            elif self.TableauCaseChoixPossible[i].PosX % 100 > PosX % 100 and self.TableauCaseChoixPossible[i].PosY % 100 < PosY % 100:
                                self.movePion(self.pionSelect, "DiagDroiteHaut")
                                break


                
            self.isPionSelect = False
            self.pionSelect = 99
            return
            
        self.pionSelect = 0

        for i in range(len(self.TableauDames)):

            if ((PosX % 100) > 25 and (PosY % 100) > 25) or ((PosX % 100) > 25 and (PosY % 100) < 25):
                if (self.TableauDames[i].PosX == self.roundint(PosX, 25) or self.TableauDames[i].PosX == self.roundint(PosX, 25) + 25) and (self.TableauDames[i].PosY == self.roundint(PosY, 25) or self.TableauDames[i].PosY == self.roundint(PosY, 25) + 25) and self.TableauDames[i].Couleur == self.teamToPlay:
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    break
            elif (PosX % 100) < 25 and (PosY % 100) > 25:
                if self.TableauDames[i].PosX == self.roundint(PosX, 25) + 25 and self.TableauDames[i].PosY == self.roundint(PosY, 25) and self.TableauDames[i].Couleur == self.teamToPlay:
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    break
            elif (PosY % 100) < 25:
                if self.TableauDames[i].PosX == self.roundint(PosX, 25) + 25 and self.TableauDames[i].PosY == self.roundint(PosY, 25) + 25 and self.TableauDames[i].Couleur == self.teamToPlay:
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    break
            if (PosX % 100) < 25:
                if self.TableauDames[i].PosX == self.roundint(PosX, 25) + 25 and self.TableauDames[i].PosY == self.roundint(PosY, 25) + 25 and self.TableauDames[i].Couleur == self.teamToPlay:
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    break
            else:
                if self.TableauDames[i].PosX == self.roundint(PosX, 25) and self.TableauDames[i].PosY == self.roundint(PosY, 25) and self.TableauDames[i].Couleur == self.teamToPlay:
                    print("Pion found at PosX :", PosX, "Pos Y :", PosY, "i :", i)
                    break
                    
        if i == 99:
            self.pionSelect = 101
            self.isPionSelect = False
        
        if self.pionSelect < 101 and self.TableauDames[i].Status != "Null":            
            self.pionSelect = i
            print("Pion select :", i)
            self.isPionSelect = True
            
            self.canvas.create_rectangle(self.roundint(PosX, 50), self.roundint(PosY, 50), self.roundint(PosX, 50) + 50, self.roundint(PosY, 50) + 50 , outline = "yellow", width = 3, tags = "rectangleSelectPion")
            
            self.showPlaceToGo(self.pionSelect)
        
        
    def showPlaceToGo(self, pionSelect): #Montre les endroits possibles sur le damier
        
        pionSelect = self.pionSelect
        
        #listeInterdit = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
        listeInterdit = [0, 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 31, 33, 35, 37, 39, 40, 42, 44, 46, 48, 51, 53, 55, 57, 59, 60, 62, 64, 66, 68, 71, 73, 75, 77, 79, 80, 82, 84, 86, 88, 91, 93, 95, 97, 99]
        
        self.CercleChoixPossible = []

        if self.TableauDames[pionSelect].Equipe == "1":
            numberChange2 = 9           
            numberChange1 = 11

        elif self.TableauDames[pionSelect].Equipe == "2":
            numberChange1 = -9
            numberChange2 = -11
            
        if self.TableauDames[pionSelect + (numberChange1)].Status == "Null" and (pionSelect + numberChange1) not in listeInterdit:

            self.CercleChoixPossible.append(self.canvas.create_oval(self.TableauDames[pionSelect + (numberChange1)].PosX - 5, self.TableauDames[pionSelect + (numberChange1)].PosY - 5,           self.TableauDames[pionSelect + (numberChange1)].PosX + 5, self.TableauDames[pionSelect + (numberChange1)].PosY + 5, fill= "yellow"))
                
            self.TableauCaseChoixPossible.append(self.TableauDames[pionSelect + (numberChange1)])
                                
        if self.TableauDames[pionSelect + (numberChange2)].Status == "Null" and (pionSelect + numberChange2) not in listeInterdit:
                
            self.CercleChoixPossible.append(self.canvas.create_oval(self.TableauDames[pionSelect + (numberChange2)].PosX - 5, self.TableauDames[pionSelect + (numberChange2)].PosY - 5, self.TableauDames[pionSelect + (numberChange2)].PosX + 5, self.TableauDames[pionSelect + (numberChange2)].PosY + 5, fill= "yellow"))
               
            self.TableauCaseChoixPossible.append(self.TableauDames[pionSelect + (numberChange2)])


    def roundint(self, value, base=5):
        return int(value) - int(value) % int(base)
    
    def delete(self, MonTag):
        self.canvas.delete(self.canvas.find_withtag(MonTag))
        
# --- Fonctions Graphiques ---

    def cercle(self, x, y, r, coul, tagsC = "cercle"): #Fonction permettant de tracer un cercle
        "tracé d ' un cercle de centre (x,y) et de rayon r"
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=coul, tags="cercleChoixPos")
    
    def Rectangle(self, x, y, coul): #Fonction permettant de tracer un rectangle
        self.canvas.create_rectangle(x + 20, x+20, y + 20, y+20, outline=coul)



