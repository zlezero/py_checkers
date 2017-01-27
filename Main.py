tableaudames = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, #0 to 10
                1, 0, 1, 0, 1, 0, 1, 0, 1, 0, #10 to 20
                0, 1, 0, 1, 0, 1, 0, 1, 0, 1, #20 to 30
                1, 0, 1, 0, 1, 0, 1, 0, 1, 0, #30 to 40
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, #40 to 50
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, #50 to 60
                0, 2, 0, 2, 0, 2, 0, 2, 0, 2, #60 to 70
                2, 0, 2, 0, 2, 0, 2, 0, 2, 0, #70 to 80
                0, 2, 0, 2, 0, 2, 0, 2, 0, 2, #80 to 90
                2, 0, 2, 0, 2, 0, 2, 0, 2, 0] #90 to 100
                
                
teamToPlay = "Black"

def movePion(PionSelect, Direction):
    pionToMove = PionSelect
    pionDirection = Direction
    if pionDirection == "DiagDroite":
        if tableaudames[pionToMove + 11] == 0:
            tableaudames[pionToMove + 11] = 1
            tableaudames[pionToMove] = 0
            print("Déplacement : Diagonale Droite")
        else:
            print("Déplacement impossible")
    elif pionDirection == "DiagGauche":
        if tableaudames[pionToMove + 9] == 0:
            tableaudames[pionToMove + 11] = 1
            tableaudames[pionToMove] = 0
            print("Déplacement : Diagonale Gauche")
        else:
            print("Déplacement impossible")
    else:
        print("Direction unconnue !")
    showTerrain()

def showTerrain():
    tableauTemp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    removeId = 0
    while i < len(tableaudames):
        x = 0  
        while x < 10:
            if tableaudames[i] == 0:
                tableauTemp[i - removeId] = "N"
            elif tableaudames[i] == 1:
                tableauTemp[i - removeId] = "B"
            elif tableaudames[i] == 2:
                tableauTemp[i - removeId] = "W"
            i += 1
            x += 1
        removeId += 10
        print(tableauTemp)


def Reset():
    tableaudames = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, #0 to 10
                    1, 0, 1, 0, 1, 0, 1, 0, 1, 0, #10 to 20
                    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, #20 to 30
                    1, 0, 1, 0, 1, 0, 1, 0, 1, 0, #30 to 40
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, #40 to 50
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, #50 to 60
                    0, 2, 0, 2, 0, 2, 0, 2, 0, 2, #60 to 70
                    2, 0, 2, 0, 2, 0, 2, 0, 2, 0, #70 to 80
                    0, 2, 0, 2, 0, 2, 0, 2, 0, 2, #80 to 90
                    2, 0, 2, 0, 2, 0, 2, 0, 2, 0] #90 to 100
        

        
    