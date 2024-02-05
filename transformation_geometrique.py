import math


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
    coord_x = math.cos(angle_final_rad) * distance
    coord_y = math.sin(angle_final_rad) * distance
    djndvndvmvkv v fvkfv

    return coord_x, coord_y
resultat = calculer_rotate_point((2,4), (0,0), -45)
print(resultat)
