# Créé par Yaya, le 26/10/2020 en Python 3.7

import turtle
turtle.tracer(0,0)            # accélération du tracé
turtle.screensize(50,50)  # taille fenêtre graphique
turtle.pu()
turtle.goto(0,0)
turtle.pd()

longueur = 10

angle = 120
niter = 2 #boucle
motifInitial ='F-G-G' # le motif initial creer un triangle


def dessiner(tapis,longueur, angle):
    """ réalise une représentation graphique d'un tapis de sierpinski donnée par des chaines de caractères """
    for caractere in tapis:
        if caractere == '+': turtle.left(angle)
        elif caractere == '-': turtle.right(angle)
        elif caractere in ['F', 'G']: turtle.forward(longueur)


#dessiner('F', 50, 60)

def triangle (chaine):
    nouvelleChaine = ''    # on crée une nouvelle chaine de caractères VIDE
    for lettre in chaine:  # on épelle la chaine de caractères donnée en paramètres
        if lettre == 'F':  # si dans l'ancienne chaine, il y a un 'F'
            nouvelleChaine = nouvelleChaine + 'F-G+F+G-F'  # alors, on écrit 'F-G+F+G-F' dans la nouvelle chaine
        if lettre == 'G':  # si dans l'ancienne chaine, il y a un 'G'
            nouvelleChaine = nouvelleChaine + 'GG'  # alors, on écrit 'GG' dans la nouvelle chaine
        else :
          nouvelleChaine = nouvelleChaine + 'F-G+F+G-F'  # sinon, on reporte la lettre telle quelle
    return nouvelleChaine


def tapisS(motifInitial, niter):
    """
        appelle niter fois regleKoch pour créer la courbe de Koch
    """
    tapis = motifInitial # on part du motif initial donné par l'utilisateur en paramètres
    for i in range(niter):
        nouveauMotif = triangle (tapis)  # on trouve le nouveau Motif à partir du motif de départ
        tapis = nouveauMotif # on dit que le nouveau Motif est maintenant le motif de départ
    return tapis



#triangle = ('F',3)
#dessiner(triangle,10, 120)

#def nouveauTriangle(motifInitial, niter):
 #   nouveauTriangle = tapis (motifInitial, niter)
  #  triangle = ''
   # for i in range(3):
    #    triangle += nouveauTriangle
     #   triangle += '--'

   # return nouveauTriangle



#longueur = 20
#angle = 120
#niter = 6
dessiner(tapisS('F-G-G', niter), longueur, angle) #le motif initial est F
#dessiner(tapisS('GG', niter), longueur, angle)


turtle.update()      # accélération du tracé
turtle.exitonclick() # permet la fermeture de la fenêtre graphique

