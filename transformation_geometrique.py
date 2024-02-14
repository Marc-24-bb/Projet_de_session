import math
import numpy as np

def calculer_reflexion_point(tuple, axe):
    reflexion_point_x = None
    reflexion_point_y = None
    if axe == 'x':
        reflexion_point_y = tuple[1] * -1
        reflexion_point_x = tuple[0]
    elif axe =='y':
        reflexion_point_x = tuple[0] * -1
        reflexion_point_y = tuple[1]
    return reflexion_point_x, reflexion_point_y

def calculer_rotate_point(tuple_p, tuple_c, angle):
    distance = 0
    distance = ((tuple_p[0]-tuple_c[0])**2 + (tuple_p[1]-tuple_c[1])**2)**0.5
    angle_depart = 0
    angle_depart = math.degrees(math.atan((tuple_p[1]-tuple_c[1])/(tuple_p[0]-tuple_c[0])))
    angle_final = 0
    angle_final = angle + angle_depart

    if angle_final < 0:
        angle_final +=360

    angle_final_rad = math.radians(angle_final)
    coord_x = round((math.cos(angle_final_rad) * distance),2)
    coord_y = round((math.sin(angle_final_rad) * distance),2)

    return coord_x, coord_y

def calculer_inclinaison_point(tuple, angle, direction):
    matrice_po = np.array([[tuple[0]],
                           [tuple[1]]])
    m = math.tan(math.radians(angle))
    matrice_x = np.array([[1, m],
                          [0, 1]])
    matrice_y = np.array([[1, 0],
                          [m , 1]])
    if direction == 'x':
        matrice_pf = np.round(np.dot(matrice_x, matrice_po), decimals=2)
    elif direction == 'y':
        matrice_pf = np.round(np.dot(matrice_y, matrice_po), decimals=2)
    tuple_pf = (matrice_pf[0, 0], matrice_pf[1, 0])

    return tuple_pf