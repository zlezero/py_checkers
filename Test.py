from tkinter import *


## -- Evènements --

#def showDamier(): #Fonction qui trace un damier
#    x = -50
#    y = -50
#    line = 0
#    while line <= 10: #On boucle tant que toutes les lignes n'ont pas été tracées
#        y = 0
#        if line % 2 == 0: #Si le numéro de ligne est impaire on les places normalement
#            while y < 500: #On boucle tant que l'on a pas fait chacune des lignes
#                while x < 450: #On boucle tant que l'on a pas fini chaque carré d'une ligne
#                    can.create_rectangle(x+50, y, x+100, y + 50, fill='black')
#                    x += 100       
#                x = -50
#                y += 100
#        else: #Sinon on les décales
#            while y < 500: #On boucle tant que l'on a pas fait chacune des lignes
#                while x < 500: #On boucle tant que l'on a pas fini chaque carré d'une ligne
#                    can.create_rectangle(x+100, y+50, x+150, y + 100, fill='black')
#                    x += 100
#                x = -50
#                y += 100
#        line += 1
#    initPion()

#def initPion():
    
#    #Initialisation des variables
#    nombreLignes = 1
#    coteActuel = 0
#    couleur = "grey"
#    xB = -25
#    yB = -75
#    xW = 75
#    yW = 75   
    
#    #while coteActuel <= 1:
#        # while nombreLignes < 4:
#        #     yB = 25
#        #     yW = 475
#        #     yW = 575
#        #     if coteActuel == 0:
#        #         while yB < 500:
#        #             while xB < 500:
#        #                 if nombreLignes % 2 == 0:
#        #                     print("Black line :", nombreLignes)
#        #                     rond(xB - 50, yB, 25, 'grey')
#        #                     rond(xB - 50, yB + 100, 25, 'grey')
#        #                     rond(xB , yB + 150, 25, 'grey')
#        #                     rond(xB , yB + 50, 25, 'grey')
#        #                 else:
#        #                     print("Black line E :", nombreLignes)
#        #                     rond(xB - 25, yB + 100, 25, 'grey')
#        #                 xB += 100
#        #             yB += 100
#        #             nombreLignes += 1
#        #     else:
#        #         while nombreLignes <= 4:
#        #             yW = 475
#        #             while yW >= 0:
#        #                 while xW < 500:
#        #                     if nombreLignes % 2 == 0:
#        #                         print("White line :", nombreLignes)
#        #                         rond(xW, yW - 100, 25, 'white')
#        #                         rond(xW, yW, 25, 'white')
#        #                         rond(xW - 50, yW - 50, 25, 'white')
#        #                         rond(xW - 50, yW - 150, 25, 'white')
#        #                     else:
#        #                         print("White line E :", nombreLignes)
#        #                         rond(xW + 50, yW - 50, 25, 'white')
#        #                     xW += 100
#        #                 nombreLignes = nombreLignes + 1
#        #                 yW -= 100
#        #             
#        #         yW = 575
#        # nombreLignes += 1
#        # coteActuel += 1
#        # nombreLignes = 0

        
#    while nombreLignes <= 10: #On boucle tant que l'on a pas atteint la fin du damier
#        if nombreLignes <= 4 or nombreLignes > 6: #Cela permet d'avoir la coupure de deux lignes au milieu du damier
#            if nombreLignes == 7: #Si le nombre de ligne est égal à 7 cela veut dire que l'on a changé de coté
#                couleur = "white"
#                yB = 225
#            if nombreLignes % 2 == 0:
#                while xB < 470:
#                    rond(xB + 50, yB + 100, 25, couleur)
#                    xB += 100
#                xB = -25
#                yB += 100
#            else: #Sinon on les affiche décalés
#                if nombreLignes == 7: #Si le nombre de ligne est égal à 7 on modifie la hauteur
#                    yW = 375
#                while xW < 480: #Tant que l'on a pas fini une ligne on affiche des ronds 
#                    rond(xW, yW, 25, couleur)
#                    xW += 100
#                xW = 75
#                yW += 100
#        nombreLignes += 1


#def rond(x, y, r, coul): #Fonction permettant de tracer un rond plein
#    "tracé d ' un cercle de centre (x,y) et de rayon r"
#    can.create_oval(x-r, y-r, x+r, y+r, fill=coul)




## -- Programme Principal --

##Initialisation de la fenêtre et du canvas
#fen = Tk()
#can = Canvas(fen, width = 500, height = 500, bg = 'ivory' )
#can.pack(side =TOP, padx =0, pady =0)

##Initialisation des boutons
#bou1 = Button(fen, text='Afficher damier', command = showDamier)
#bou1.pack(side = LEFT, padx =3, pady =3)

##Boucle principale
#fen.mainloop()

import socket
import select

port = 12800

def serveur():
    global port
    hote = ''

    connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_principale.bind((hote, port))
    connexion_principale.listen(5)
    print("Le serveur écoute à présent sur le port {}".format(port))

    serveur_lance = True
    clients_connectes = []
    while serveur_lance:
        # On va vérifier que de nouveaux clients ne demandent pas à se connecter
        # Pour cela, on écoute la connexion_principale en lecture
        # On attend maximum 50ms
        connexions_demandees, wlist, xlist = select.select([connexion_principale],
            [], [], 0.05)
    
        for connexion in connexions_demandees:
            connexion_avec_client, infos_connexion = connexion.accept()
            # On ajoute le socket connecté à la liste des clients
            clients_connectes.append(connexion_avec_client)
    
        # Maintenant, on écoute la liste des clients connectés
        # Les clients renvoyés par select sont ceux devant être lus (recv)
        # On attend là encore 50ms maximum
        # On enferme l'appel à select.select dans un bloc try
        # En effet, si la liste de clients connectés est vide, une exception
        # Peut être levée
        clients_a_lire = []
        try:
            clients_a_lire, wlist, xlist = select.select(clients_connectes,
                    [], [], 0.05)
        except select.error:
            pass
        else:
            # On parcourt la liste des clients à lire
            for client in clients_a_lire:
                # Client est de type socket
                msg_recu = client.recv(1024)
                # Peut planter si le message contient des caractères spéciaux
                msg_recu = msg_recu.decode()
                print("Reçu {}".format(msg_recu))
                client.send(b"5/5")
                if msg_recu == "fin":
                    serveur_lance = False

    print("Fermeture des connexions")
    for client in clients_connectes:
        client.close()

    connexion_principale.close()

def client():    
    global port
    hote = "localhost"

    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((hote, port))
    print("Connexion établie avec le serveur sur le port {}".format(port))

    msg_a_envoyer = b""
    while msg_a_envoyer != b"fin":
        msg_a_envoyer = input("> ")
        # Peut planter si vous tapez des caractères spéciaux
        msg_a_envoyer = msg_a_envoyer.encode()
        # On envoie le message
        connexion_avec_serveur.send(msg_a_envoyer)
        msg_recu = connexion_avec_serveur.recv(1024)
        print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents

    print("Fermeture de la connexion")
    connexion_avec_serveur.close()



