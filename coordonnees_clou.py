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
    return ('pt_0', tuple_t0), ('pt_1', tuple_t1), ('pt_2', tuple_t2), ('pt_3', tuple_t3), ('pk_2', tuple_k2), ('pk_0', tuple_k0), ('pk_1', tuple_k1)

def appliquer_transformation_clou(points_clou, center_rotation, angle_rotation, angle_inclinaison, direction_inclinaison, axe_reflexion):
    liste_point = [calculer_coordonnees_clou(3,10,1,.75,2)]

    liste_reflexion = liste_point.copy()
    liste_rotation = liste_point.copy()
    liste_inclinaison = liste_point.copy()
    for i in range(1,8):
        nouvelle_liste_reflexion = calculer_reflexion_point(liste_reflexion[i][1], axe_reflexion)

    return nouvelle_liste_reflexion

print(appliquer_transformation_clou(calculer_coordonnees_clou(3,10,1,.75,2), (0,0), 30, 20, 'x', 'x'))
