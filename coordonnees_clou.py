from transformation_geometrique import *
def calculer_coordonnees_clou(a, b, c, d, e):
    # Les équations servent à trouver la distance X et Y de l'origine
    tuple_t0 = ((b * -1) / 2, c / 2)
    tuple_t1 = ((b * -1) / 2, (-1 * c) / 2)
    tuple_t2 = (((b * -1) / 2) - d, -1 * a / 2)
    tuple_t3 = (((b * -1) / 2) - d, a / 2)
    tuple_k0 = (b / 2 + e, 0)
    tuple_k1 = (b / 2, -1 * c / 2)
    tuple_k2 = (b / 2, c / 2)
    return list[('pt_0', tuple_t0), ('pt_1', tuple_t1), ('pt_2', tuple_t2), ('pt_3', tuple_t3), ('pk_2', tuple_k2), ('pk_0', tuple_k0), ('pk_1', tuple_k1)]

def appliquer_transformation_clou(points_clou, center_rotation, angle_rotation, angle_inclinaison, direction_inclinaison, axe_reflexion):
    liste_point = [calculer_coordonnees_clou(3,10,1,.75,2)]
    return liste_point[]
print(appliquer_transformation_clou(calculer_coordonnees_clou(3,10,1,.75,2), (0,0),30,20,'x','x'))

'''
    liste_reflexion =list(points_clou.copy())
    liste_rotation = list(points_clou.copy())
    liste_inclinaison = list(points_clou.copy())

    for i in range(0,7):
        liste_reflexion[i] = calculer_reflexion_point(points_clou[i][1], axe_reflexion)
        liste_rotation[i] = calculer_rotate_point(points_clou[i][1], center_rotation, angle_rotation)
        liste_inclinaison[i] = calculer_inclinaison_point(points_clou[i][1], angle_inclinaison, direction_inclinaison)
    return liste_reflexion, liste_rotation, liste_inclinaison
print(appliquer_transformation_clou(calculer_coordonnees_clou(3,10,1,.75,2), (0,0), 30, 20, 'x', 'x'))
'''
