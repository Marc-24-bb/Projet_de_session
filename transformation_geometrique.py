import math
import numpy as np

def calculer_reflexion_point(tuple, axe):

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
    angle_rad = math.radians(angle)
    xp = tuple_p[0] - tuple_c[0]
    yp = tuple_p[1] - tuple_c[1]
    coord_x = round(xp * math.cos(angle_rad) - yp * math.sin(angle_rad) , 2)
    coord_y = round(xp * math.sin(angle_rad) + yp * math.cos(angle_rad) , 2)

    return (coord_x, coord_y)


def calculer_inclinaison_point(tuple, angle, direction):
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
