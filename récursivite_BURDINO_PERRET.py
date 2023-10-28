import turtle as t
from math import sqrt
from random import randint

def traceMandelbrot(iterationMax, ReMin=-2, ReMax=1, ImMin=-1, ImMax=1, ReLongueur=900, ImLongueur=600, nbPointsRe=125, nbPointsIm=125):
    """
        Fonction principale initiant des paramètres du module turtle et lançant le programme de dessin de la fonction  Mandelbrot()
        Entrées :
            * n -> int : nombre de termes maximum calculés
            * ReMin -> int : début de l'axe des abcisses(réels)
            * ReMax -> int : fin de l'axe des abcisses (réels)
            * ImMin -> int : début de l'axe des ordonnées (imaginaire)
            * ImMax -> int : fin de l'axe (imaginaire)
            * ReLongueur -> int : longueur de l'axe des Réels
            * ImLongueur -> int : longueur de l'axe des Imaginaires
            * nbPointsRe -> int : nombre de points constituant le plan pour chaque ordonnée
            * nbPointsIm -> int : nombre de points constituant le plan pour chaque abcisse
        Sortie : aucune, affichage de l'ensemble de Mandelbrot à l'aide du module turtle
    """
    t.colormode(255) # Indique au module que les plages de valeurs (r,g,b) vont de 0 à 255
    t.Screen().setup(ReLongueur, ImLongueur) # On configure la taille de la fenêtre selon la taille du plan en entrée
    t.hideturtle()
    t.penup()
    t.tracer(0,0)

    Mandelbrot(iterationMax, ReMin, ReMax, ImMin, ImMax, ReLongueur, ImLongueur, nbPointsRe, nbPointsIm)
    t.update()
    t.mainloop()


def Mandelbrot(iterationMax, ReMin, ReMax, ImMin, ImMax, ReLongueur, ImLongueur, nbPointsRe, nbPointsIm):
    """
        Fonction qui dessine l'ensemble de Mandelbrot (avec le module turtle). Récupère un indice (en appelant la fonction indiceDivergence) pour chaque point c du plan complexe, calcule des valeurs r,g,b en fonction de cet indice et place un point de couleur (r,g,b) sur le plan
        Entrées : (mêmes entrées que la fonction traceMandelbrot)
            * iterationMax -> int : nombre de termes maximum calculés
            * ReMin -> int : début de l'axe des abcisses(réels)
            * ReMax -> int : fin de l'axe des abcisses (réels)
            * ImMin -> int : début de l'axe des ordonnées (imaginaire)
            * ImMax -> int : fin de l'axe (imaginaire)
            * ReLongueur -> int : longueur de l'axe des Réels
            * ImLongueur -> int : longueur de l'axe des Imaginaires
            * nbPointsRe -> int : nombre de points constituant le plan pour chaque ordonnée
            * nbPointsIm -> int : nombre de points constituant le plan pour chaque abcisse
        Sortie :
            * Aucune, affichage de l'ensemble de Mandelbrot
    """

    # Calcul longueur axe des réels / imaginaires (unité du plan)
    ecartRe = ReMax - ReMin
    ecartIm = ImMax - ImMin

    # Calcul des intervalles entre deux points dans le plan (longueur axe / nb de points à placer sur cet axe = écart entre 2 points)
    intervalleRe = ecartRe/nbPointsRe
    intervalleIm = ecartIm/nbPointsIm

    # Parcours du plan complexe par deux boucles (nbPointsRe*nbPointsIm points parcourus)
    for b in range(nbPointsIm):
        for a in range(nbPointsRe):
            # Calcul de l'indice à partir duquel la suite diverge (indice = -1 si elle est bornée)
            indice = indiceDivergence(iterationMax, [0,0], [ReMin+intervalleRe*a,ImMin+b*intervalleIm], 0)

            # Si la suite est bornée, on veut placer un point noir
            if indice == -1:
                couleur = 'black'
            # Sinon la suite diverge => calcul des valeurs r,g,b en fonction de l'indice de divergence
            else:
                red, green, blue = 237, 148, 52
                couleur = (red*indice//iterationMax, green*indice//iterationMax, blue*indice//iterationMax//2)
            # Positionnement de la tortue
            t.setpos(ReLongueur/ecartRe*(a*intervalleRe) - ReLongueur/2, ImLongueur/ecartIm*(b*intervalleIm) - ImLongueur/2)
            # Placement du point (d'une certaine taille, couleur)
            t.dot(9.5, couleur)


def indiceDivergence(iterationMax, terme, c, indiceTerme):
    """
        Fonction récursive qui renvoie l'indice à partir duquel la suite terme^2 + c est supérieure à 2, sinon -1
        Entrées :
            * iterationMax -> int : nombre de termes maximum calculés
            * terme -> list : 2 entiers (partie réelle et imaginaire) correspondant au terme de la suite
            * c -> list : 2 entiers (partie réelle et imaginaire) correspondant à un point du plan complexe
            * rangMax -> int : iterationMax
        Sortie :
            * int : indice de la suite
    """
    # Cas d'arrêt 1 : la fonction s'arrête (renvoie -1) quand iterationMax termes ont été calculés (de 0 à iterationMax-1)
    if indiceTerme >= iterationMax:
        return -1
    # Cas d'arrêt 2 : la fonction s'arrête (renvoie l'indice actuel) quand la distance à 0 du terme sur un plan est > 2
    elif sqrt(terme[0]**2+terme[1]**2) > 2: # distance à l'origine (module) > 2
        return indiceTerme
    # Sinon, on rappelle la fonction en calculant le terme suivant
    else:
        return indiceDivergence(iterationMax, additionC(multiplicationC(terme, terme), c), c, indiceTerme+1)


def additionC(c1, c2):
    """
        Fonction faisant la somme de deux nombres complexes de forme a+ib. Les deux parties réelles sont additionnées entre elles (et de même pour les deux parties imaginaires)
        Entrées :
            * c1, c2 -> list : listes contenant 2 nombres réels correspondant à la partie réelle/imaginaire d'un nombre complexe
        Sortie :
            * list : liste de deux réels correspondant à la partie réelle et imaginaire du nombre complexe obtenu après somme de c1 et c2
    """
    return [c1[0]+c2[0], c1[1]+ c2[1]]


def multiplicationC(c1, c2):
    """
        Fonction faisant la multiplication de deux nombres complexes (a+ib)
        Entrées :
            * c1, c2 -> list : listes contenant 2 nombres réels correspondant à la partie réelle/imaginaire d'un nombre complexe
        Sortie :
            * list : liste de deux réels correspondant à la partie réelle et imaginaire du nombre complexe obtenu après multiplication de c1 et c2
    """
    return [c1[0]*c2[0]-c1[1]*c2[1], c1[0]*c2[1]+c1[1]*c2[0]]