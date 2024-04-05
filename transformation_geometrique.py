import math
import numpy as np


def calculer_reflexion_point(tuple, axe):
    '''
    Description: Cette fonction applique une réflexion (miroir) à un point par rapport à un
    axe spécifié.

    Arguments point (tuple): Un tuple (x, y) représentant les coordonnées du point à
    réfléchir.
    axe (str): L'axe de réflexion. Doit être 'x' ou 'y'. Si l'axe est 'x', la
    réflexion se produit par rapport à l'axe vertical (mirroir horizontal),
    changeant la coordonnée y du point. Si l'axe est 'y', la réflexion se
    produit par rapport à l'axe horizontal (mirroir vertical), changeant la
    coordonnée x.

    Retourne : Un tuple (x', y') représentant les nouvelles coordonnées du point
    après la réflexion. Si l'axe de réflexion est 'x', y' sera l'opposé de y. Si
    l'axe est 'y', x' sera l'opposé de x.
    '''

    # Si l'axe X est choisi, on multiplie la valeur Y par -1
    if axe == 'x':
        reflexion_point_y = tuple[1] * -1
        reflexion_point_x = tuple[0]
    # Si l'axe Y est choisi on multiplie la valeur de X par -1
    elif axe =='y':
        reflexion_point_x = tuple[0] * -1
        reflexion_point_y = tuple[1]
    return reflexion_point_x, reflexion_point_y

def calculer_rotate_point(tuple_p, angle, tuple_c=(0,0)):
    '''
    Description:
    Cette fonction prend un point dans le plan cartésien et le fait pivoter
    autour d'un point central donné (le centre de rotation) d'un certain angle.

    Arguments:
    point (tuple): Un tuple (x, y) représentant les coordonnées du point à
    faire pivoter.

    angle (float): L'angle de rotation en degrés. Une valeur positive entraîne
    une rotation antihoraire, tandis qu'une valeur négative entraîne une
    rotation horaire.

    center (tuple): Un tuple représentant les coordonnées du centre de
    rotation. Par défaut, il s'agit de l'origine (0, 0).

    Retourne :
    tuple: Un tuple (x', y') représentant les nouvelles coordonnées du point
    après la rotation. Les résultats doivent être arrondis à deux chiffres
    après la virgule.

    '''

    angle_rad = math.radians(angle)
    xp = tuple_p[0] - tuple_c[0]
    yp = tuple_p[1] - tuple_c[1]
    coord_x = round(xp * math.cos(angle_rad) - yp * math.sin(angle_rad) , 2)
    coord_y = round(xp * math.sin(angle_rad) + yp * math.cos(angle_rad) , 2)

    return (coord_x, coord_y)


def calculer_inclinaison_point(tuple, angle, direction):
    '''
    Description:
    Cette fonction applique une transformation d'inclinaison (cisaillement)
    sur un point. L'inclinaison est déterminée par un angle en degrés et
    peut être appliquée selon l'axe des x ou l'axe des y.


    Arguments:
    point (tuple): Un tuple (x, y) représentant les coordonnées du point à
    incliner.

    angle (float): L'angle d'inclinaison en degrés. L'angle détermine
    l'intensité de la transformation de cisaillement.

    direction (str): La direction de l'inclinaison. Doit être 'x' pour une
    inclinaison horizontale ou 'y' pour une inclinaison verticale.

    Retourne :
    Un tuple (x', y') représentant les nouvelles coordonnées du point après
    l'inclinaison. Les résultats doivent être arrondis à deux chiffres après la
    virgule.

    '''
    # Transfère le tuple en matrice
    matrice_po = np.array([[tuple[0]],
                           [tuple[1]]])

    #Crée une variable m pour l'angle
    m = math.tan(math.radians(angle))
    matrice_pf = []
    # Création de deux matrices multiplicatives
    matrice_x = np.array([[1, m], [0, 1]])

    matrice_y = np.array([[1, 0], [m , 1]])

    # Multiplication de la matrice contenant le point d'origine avec la matrice multiplicative
    if direction == 'x':
        matrice_pf = np.round(np.dot(matrice_x, matrice_po), decimals=2)
    elif direction == 'y':
        matrice_pf = np.round(np.dot(matrice_y, matrice_po), decimals=2)
    # Transfère de la matrice en tuple
    tuple_pf = (matrice_pf[0, 0], matrice_pf[1, 0])

    return tuple_pf
