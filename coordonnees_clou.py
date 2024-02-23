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
    return [('pt_0', tuple_t0), ('pt_1', tuple_t1), ('pt_2', tuple_t2), ('pt_3', tuple_t3), ('pk_2', tuple_k2), ('pk_0', tuple_k0), ('pk_1', tuple_k1)]

def appliquer_transformation_clou(points_clou, center_rotation, angle_rotation, angle_inclinaison, direction_inclinaison, axe_reflexion):


    liste_reflexion = points_clou.copy()
    nouvelle_liste_reflexion = list()
    liste_rotation = points_clou.copy()
    nouvelle_liste_rotation = list()
    liste_inclinaison = points_clou.copy()
    nouvelle_liste_inclinaison= list()

    for i in range(0,7):
        nouvelle_liste_reflexion.append(points_clou[i][0])
        nouvelle_liste_reflexion.append(calculer_reflexion_point(liste_reflexion[i][1], axe_reflexion))
        nouvelle_liste_rotation.append(points_clou[i][0])
        nouvelle_liste_rotation.append(calculer_rotate_point(liste_reflexion[i][1], center_rotation, angle_rotation))
        nouvelle_liste_inclinaison.append(points_clou[i][0])
        nouvelle_liste_inclinaison.append(calculer_inclinaison_point(liste_reflexion[i][1], angle_inclinaison, direction_inclinaison))


    return nouvelle_liste_reflexion, nouvelle_liste_rotation, nouvelle_liste_inclinaison

