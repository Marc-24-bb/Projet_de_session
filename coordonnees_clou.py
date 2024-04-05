from transformation_geometrique import *
def calculer_coordonnees_clou(a, b, c, d, e):
    '''
    Description:
    Cette fonction détermine les coordonnées d'un clou en suivant la
    paramétrisation illustrée dans la Figure 1.


    Arguments:
    A, B, C, D, E (float): Dimensions spécifiques du clou, utilisées pour
    calculer les coordonnées.

    Retourne :
    list: Une liste de tuples, où chaque tuple contient :
    ● Une chaîne de caractères indiquant le nom du point (par
    exemple, "pt_0").
    ● Un tuple de deux nombres (float, float) représentant les
    coordonnées du point dans un plan 2D.

    La liste des points retournée suit l'ordre : pt_0, pt_1, pt_2, pt_3, pk_2,
    pk_0, pk_1. Ces points représentent différentes parties du clou en
    suivant la paramétrisation de la Figure 1.
    '''

    # Les équations servent à trouver la distance X et Y de l'origine
    tuple_t0 = ((b * -1) / 2, c / 2)
    tuple_t1 = ((b * -1) / 2, (-1 * c) / 2)
    tuple_t2 = (((b * -1) / 2) - d, -1 * a / 2)
    tuple_t3 = (((b * -1) / 2) - d, a / 2)
    tuple_k0 = (b / 2 + e, 0)
    tuple_k1 = (b / 2, -1 * c / 2)
    tuple_k2 = (b / 2, c / 2)
    return [('pt_0', tuple_t0), ('pt_1', tuple_t1), ('pt_2', tuple_t2), ('pt_3', tuple_t3),
            ('pk_2', tuple_k2), ('pk_0', tuple_k0), ('pk_1', tuple_k1)]

def appliquer_transformation_clou(points_clou, center_rotation, angle_rotation, direction_inclinaison, angle_inclinaison, axe_reflexion):
    '''
    Description:
    Cette fonction prend un ensemble de points clés représentant un clou et
    applique trois types de transformations géométriques : réflexion,
    rotation et inclinaison. Chaque transformation est appliquée
    séquentiellement à tous les points clés.


    Arguments:
    Apoints_clou (list): Une liste de tuples, où chaque tuple contient :
    ● Une chaîne de caractères indiquant le nom du point (par
    exemple, "pt_0").
    ● Un tuple de deux nombres (float, float) représentant les
    coordonnées du point dans un plan 2D.

    center_rotation (tuple): Le centre de rotation pour la transformation de
    rotation.
    angle_rotation (float): L'angle de rotation en degrés.
    angle_inclinaison (float): L'angle d'inclinaison en degrés.
    direction_inclinaison (str): La direction de l'inclinaison ('x' ou 'y').
    axe_reflexion (str): L'axe de réflexion ('x' ou 'y').


    Retourne :
    tuple : Trois listes de tuples. Chaque liste correspond aux coordonnées
    des points clés après l'application d'une des transformations (réflexion,
    rotation, inclinaison). Cela permet une analyse et une visualisation
    détaillées de l'impact de chaque transformation sur la structure du clou.
    '''

    nouvelle_liste_reflexion = []
    nouvelle_liste_rotation = []
    nouvelle_liste_inclinaison= []

    for i in range(len(points_clou)):
        nouvelle_liste_reflexion.append((points_clou[i][0], calculer_reflexion_point(points_clou[i][1], axe_reflexion)))
        nouvelle_liste_rotation.append((points_clou[i][0], calculer_rotate_point((points_clou[i][1]), angle_rotation, center_rotation)))
        nouvelle_liste_inclinaison.append((points_clou[i][0], calculer_inclinaison_point(points_clou[i][1], angle_inclinaison, direction_inclinaison)))

    return nouvelle_liste_reflexion, nouvelle_liste_rotation, nouvelle_liste_inclinaison

