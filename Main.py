from tkinter import *


#0 = Vide
#1 = Pion Blanc
#2 = Pion Noir
#3 = Dame Blanche
#4 = Dame Noire

TableauDames = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, #0 to 9
                1, 0, 1, 0, 1, 0, 1, 0, 1, 0, #10 to 19
                0, 1, 0, 1, 0, 1, 0, 1, 0, 1, #20 to 29
                1, 0, 1, 0, 1, 0, 1, 0, 1, 0, #30 to 39
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, #40 to 49
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, #50 to 59
                0, 2, 0, 2, 0, 2, 0, 2, 0, 2, #60 to 69
                2, 0, 2, 0, 2, 0, 2, 0, 2, 0, #70 to 79
                0, 2, 0, 2, 0, 2, 0, 2, 0, 2, #80 to 89
                2, 0, 2, 0, 2, 0, 2, 0, 2, 0] #90 to 99

# TableauDames = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                 0, 2, 0, 2, 0, 0, 0, 0, 0, 0,
#                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                
                
teamToPlay = "Black"

def movePion(PionSelect, Direction):
    pionToMove = PionSelect
    pionDirection = Direction
    if TableauDames[pionToMove] != 0:
        if pionDirection == "DiagDroiteBas":
            if TableauDames[pionToMove + 11] == 0:
                if TableauDames[pionToMove] == 1:
                    TableauDames[pionToMove  + 11] = 1
                elif TableauDames[pionToMove] == 2:
                    TableauDames[pionToMove  + 11] = 2
                TableauDames[pionToMove] = 0
                print("Déplacement : Diagonale Droite Basse")
            elif TableauDames[pionToMove + 11] == 2 and TableauDames[pionToMove] == 1:
                print("Pion adverse !")
            elif TableauDames[pionToMove + 11] == 1 and TableauDames[pionToMove] == 2:
                print("Pion adverse !")
            else:
                print("Déplacement impossible")
        elif pionDirection == "DiagGaucheBas":
            if TableauDames[pionToMove + 9] == 0:
                if TableauDames[pionToMove] == 1:
                    TableauDames[pionToMove  + 9] = 1
                elif TableauDames[pionToMove] == 2:
                    TableauDames[pionToMove  + 9] = 2
                TableauDames[pionToMove] = 0
                print("Déplacement : Diagonale Gauche Basse")
            else:
                print("Déplacement impossible")
        
        elif pionDirection == "DiagGaucheHaut":
            if TableauDames[pionToMove - 12] == 0:
                if TableauDames[pionToMove] == 1:
                    TableauDames[pionToMove  - 12] = 1
                elif TableauDames[pionToMove] == 2:
                    TableauDames[pionToMove  - 12] = 2
                TableauDames[pionToMove] = 0
                print("Déplacement : Diagonale Gauche haut")
            elif TableauDames[pionToMove - 12] == 2 and TableauDames[pionToMove] == 1:
                print("Pion adverse !")
            elif TableauDames[pionToMove - 12] == 1 and TableauDames[pionToMove] == 2:
                print("Pion adverse !")
            else:
                print("Déplacement impossible")
        elif pionDirection == "DiagDroiteHaut":
            if TableauDames[pionToMove - 9] == 0:
                if TableauDames[pionToMove] == 1:
                    TableauDames[pionToMove  - 9] = 1
                elif TableauDames[pionToMove] == 2:
                    TableauDames[pionToMove  - 9] = 2
                TableauDames[pionToMove] = 0
                print("Déplacement : Diagonale Droite Haute")
            elif TableauDames[pionToMove - 9] == 2 and TableauDames[pionToMove] == 1:
                print("Pion adverse !")
            elif TableauDames[pionToMove - 9] == 1 and TableauDames[pionToMove] == 2:
                print("Pion adverse !")
            else:
                print("Déplacement impossible")
        else:
            print("Direction inconnue !")
    else:
        print("Pion inexistant !")
    showTerrain()

def movePion2(PionSelect, Direction):
    
    pionToMove = PionSelect
    pionDirection = Direction
    numberChange = 0
    
    #On vérifie si le pion existe
    if TableauDames[pionToMove] == 0:
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
    if TableauDames[pionToMove + (numberChange)] == 0: #Si l'endroit ou le pion doit aller est vide
        if TableauDames[pionToMove] == 1: #On bouge le pion en fonction de son équipe
            TableauDames[pionToMove + (numberChange)] = 1
        else:
            TableauDames[pionToMove + (numberChange)] = 2
        TableauDames[pionToMove] = 0
        print("DEBUG : New pos :", pionToMove + (numberChange))
    elif TableauDames[pionToMove + (numberChange)] == 2 and TableauDames[pionToMove] == 1: #On regarde si on peut prendre un pion
        if TableauDames[pionToMove + (numberChange * 2)] == 0: #Si une case est libre après le pion
            TableauDames[pionToMove + (numberChange * 2)] = 1 #On bouge le pion
            TableauDames[pionToMove + (numberChange)] = 0 #On élimine le pion adverse
            TableauDames[pionToMove] = 0 #On supprime le pion de son emplacement d'origine
            print("DEBUG : New pos :", pionToMove + (numberChange * 2))
            print("Pion pris !")
        else: #Si un emplacement est indisponible on ne peut pas prendre le pion
            print("Impossible de prendre le pion !")
    elif TableauDames[pionToMove + (numberChange)] == 1 and TableauDames[pionToMove] == 2:
        if TableauDames[pionToMove + (numberChange * 2)] == 0:
            TableauDames[pionToMove + (numberChange * 2)] = 2            
            TableauDames[pionToMove + (numberChange)] = 0
            TableauDames[pionToMove] = 0
            print("DEBUG : New pos :", pionToMove + (numberChange * 2))
            print("Pion pris !")
        else:
            print("Impossible de prendre le pion !")
    else:
        print("Déplacement impossible !")
    
    
    
    showTerrain()
        

def showTerrain():
    tableauTemp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    removeId = 0
    while i < len(TableauDames):
        x = 0  
        while x < 10:
            if TableauDames[i] == 0:
                tableauTemp[i - removeId] = "O"
            elif TableauDames[i] == 1:
                tableauTemp[i - removeId] = "B"
            elif TableauDames[i] == 2:
                tableauTemp[i - removeId] = "W"
            i += 1
            x += 1
        removeId += 10
        print(tableauTemp)

def showDamier(): #Fonction qui trace un damier
    x = -50
    y = -50
    line = 0
    while line <= 10: #On boucle tant que toutes les lignes n'ont pas été tracées
        y = 0
        if line % 2 == 0: #Si le numéro de ligne est impaire on les places normalement
            while y < 500: #On boucle tant que l'on a pas fait chacune des lignes
                while x < 450: #On boucle tant que l'on a pas fini chaque carré d'une ligne
                    can.create_rectangle(x+50, y, x+100, y + 50, fill='black')
                    x += 100       
                x = -50
                y += 100
        else: #Sinon on les décales
            while y < 500: #On boucle tant que l'on a pas fait chacune des lignes
                while x < 500: #On boucle tant que l'on a pas fini chaque carré d'une ligne
                    can.create_rectangle(x+100, y+50, x+150, y + 100, fill='black')
                    x += 100
                x = -50
                y += 100
        line += 1

def showTerrainFromPionPlace(): #Fonction qui place un pion aléatoirement sur le damier
    print("--------------------------------------------------")
    tableauTemp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    removeId = 0
    line = 1
    cercleY = 25
    cercleX = -25
    while i < len(TableauDames):
        x = 0  
        while x < 10:
            cercleX += 50
            if TableauDames[i] == 0:
                tableauTemp[i - removeId] = "O"
            elif TableauDames[i] == 1:
                tableauTemp[i - removeId] = "B"
                cercle(x + cercleX, i + cercleY, 20, 'black')
            elif TableauDames[i] == 2:
                tableauTemp[i - removeId] = "W"
                cercle(x + cercleX, i + cercleY, 20, 'white')
            i += 1
            x += 1
        cercleY += 50
        removeId += 10
        
        
        print(tableauTemp)
    

def cercle(x, y, r, coul): #Fonction permettant de tracer un cercle
    "tracé d ' un cercle de centre (x,y) et de rayon r"
    can.create_oval(x-r, y-r, x+r, y+r, fill=coul)
    
def Reset():
    TableauDames = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, #0 to 10
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
    while True:
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
                if TableauDames[idPion] != 1:
                    print("Vous ne pouvez pas jouer ceci !")
                else:
                    canPlay = False
            else:
                if TableauDames[idPion] != 2:
                    print("Vous ne pouvez pas jouer ceci !")
                else:
                    canPlay = False
        canPlay = True
        while canPlay:
            Direction = input("Entrez la direction DiagDroiteHaut/DiagGaucheHaut/DiagDroiteBas/DiagGaucheBas :")
            if Direction == "DiagDroiteHaut" or Direction == "DiagGaucheGaut" or Direction == "DiagDroiteBas" or Direction == "DiagGaucheBas":
                movePion2(idPion, Direction)
                canPlay = False
            else:
                print("Direction inconnue !")

def GetWinner():
    nbrWhite = 0
    nbrBlack = 0
    for i in range(len(TableauDames)):
        if TableauDames[i] == 1:
            nbrBlack += 1
        elif TableauDames[i] == 2:
            nbrWhite += 1
    if nbrWhite == 0:
        print("Black Win !")
        return "BWin"
    elif nbrBlack == 0:
        print("White Win !")
        return "WWin"
    else:
        return False
# -- Programme Principal --

#Initialisation de la fenêtre et du canvas
fen = Tk()
can = Canvas(fen, width = 500, height = 500, bg = 'ivory' )
can.pack(side =TOP, padx =0, pady =0)

#Initialisation des boutons
bou1 = Button(fen, text='Afficher damier', command = showDamier)
bou1.pack(side = LEFT, padx =3, pady =3)
bou2 = Button(fen, text='Placer un pion', command = showTerrainFromPionPlace)
bou2.pack(side = RIGHT, padx =3, pady =3)

#Boucle principale
fen.mainloop()
        

        
    