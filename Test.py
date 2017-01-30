from tkinter import *

# -- Evènements --

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
    initPion()

def initPion():
    nombreLignes = 1
    coteActuel = 0
    couleur = "grey"
    xB = -25
    yB = -75
    xW = 75
    yW = 75
    #while coteActuel <= 1:
        # while nombreLignes < 4:
        #     yB = 25
        #     yW = 475
        #     yW = 575
        #     if coteActuel == 0:
        #         while yB < 500:
        #             while xB < 500:
        #                 if nombreLignes % 2 == 0:
        #                     print("Black line :", nombreLignes)
        #                     rond(xB - 50, yB, 25, 'grey')
        #                     rond(xB - 50, yB + 100, 25, 'grey')
        #                     rond(xB , yB + 150, 25, 'grey')
        #                     rond(xB , yB + 50, 25, 'grey')
        #                 else:
        #                     print("Black line E :", nombreLignes)
        #                     rond(xB - 25, yB + 100, 25, 'grey')
        #                 xB += 100
        #             yB += 100
        #             nombreLignes += 1
        #     else:
        #         while nombreLignes <= 4:
        #             yW = 475
        #             while yW >= 0:
        #                 while xW < 500:
        #                     if nombreLignes % 2 == 0:
        #                         print("White line :", nombreLignes)
        #                         rond(xW, yW - 100, 25, 'white')
        #                         rond(xW, yW, 25, 'white')
        #                         rond(xW - 50, yW - 50, 25, 'white')
        #                         rond(xW - 50, yW - 150, 25, 'white')
        #                     else:
        #                         print("White line E :", nombreLignes)
        #                         rond(xW + 50, yW - 50, 25, 'white')
        #                     xW += 100
        #                 nombreLignes = nombreLignes + 1
        #                 yW -= 100
        #             
        #         yW = 575
        # nombreLignes += 1
        # coteActuel += 1
        # nombreLignes = 0

        
    while nombreLignes <= 10:
        if nombreLignes <= 4 or nombreLignes > 6:
            if nombreLignes == 7:
                couleur = "white"
                yB = 225
            if nombreLignes % 2 == 0:
                while xB < 500:
                    rond(xB + 50, yB + 100, 25, couleur)
                    xB += 100
                xB = -25
                yB += 100
            else:
                if nombreLignes == 7:
                    yW = 375
                while xW < 500:
                    rond(xW, yW, 25, couleur)
                    xW += 100
                xW = 75
                yW += 100
        nombreLignes += 1


def rond(x, y, r, coul): #Fonction permettant de tracer un rond plein
    "tracé d ' un cercle de centre (x,y) et de rayon r"
    can.create_oval(x-r, y-r, x+r, y+r, fill=coul)




# -- Programme Principal --

#Initialisation de la fenêtre et du canvas
fen = Tk()
can = Canvas(fen, width = 500, height = 500, bg = 'ivory' )
can.pack(side =TOP, padx =0, pady =0)

#Initialisation des boutons
bou1 = Button(fen, text='Afficher damier', command = showDamier)
bou1.pack(side = LEFT, padx =3, pady =3)

#Boucle principale
fen.mainloop()