def regrouper_points(tableau, k, max_iterations):
    '''
    Description:
    Diviser un ensemble de points dans un plan 2D en un nombre défini de
    groupes.


    Arguments:
    data (numpy.ndarray): Un tableau 2d numpy représentant l'ensemble de
    données à partitionner. Chaque ligne du tableau représente un
    histogramme décrivant un point.

    k (int): Le nombre de groupes à identifier dans l'ensemble de données.

    max_iterations (int): Le nombre maximal d'itérations que l'algorithme
    exécutera. La valeur par défaut est 50.


    Retourne :
    numpy.ndarray: Un tableau numpy 1D où chaque élément correspond à
    l'indice du centre le plus proche pour chaque point de l'ensemble de
    données. C'est un vecteur d'entiers de la même
    longueur que le nombre de points dans 'data', indiquant l'affectation de
    groupe pour chaque point.
    '''
    nb_groupe = k
    pt_centraux = k