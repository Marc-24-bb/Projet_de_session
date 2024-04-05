from PIL import Image
import numpy as np
import math


def rgb_to_gry(chemin_image_couleur, chemin_sauvegarde_gris):
    '''
    Description:
    Cette fonction transforme une image en couleur en une nouvelle image
    en niveaux de gris.


    Arguments:
    chemin_image_couleur (str): Le chemin de l'image en couleur à
    transformer.
    chemin_sauvegarde_gris (str): Le chemin où sauvegarder l'image
    résultante en niveaux de gris.

    Retourne :
    None: La fonction ne retourne rien mais sauvegarde l'image en niveaux
    de gris au chemin spécifié.
    '''
    image = Image.open(chemin_image_couleur)
    largeur, hauteur = image.size

    for i in range(largeur):
        for j in range(hauteur):
            r, g, b = image.getpixel((i, j))
            valeur_gris = int((r + g + b)/3)
            image.putpixel((i, j), (valeur_gris, valeur_gris, valeur_gris))

    image.save(chemin_sauvegarde_gris)


def appliquer_transformation_1(image_grise):
    '''
    Description:
    Cette fonction prend une image en niveaux de gris sous forme d'un
    tableau NumPy 2D et applique une transformation pour simplifier et
    extraire des caractéristiques significatives de l'image.

    Arguments:
    image_gris (numpy.ndarray): Un tableau 2D NumPy représentant une
    image en niveaux de gris. Chaque élément du tableau correspond à
    l'intensité d'un pixel de l'image.

    Retourne :
    numpy.ndarray: Un tableau 2D NumPy résultant de la transformation
    appliquée
    '''

    hauteur, largeur = image_grise.shape
    nouvelle_matrice = np.zeros((hauteur, largeur), dtype=int)

    for i in range(1, hauteur - 1):
        for j in range(1, largeur - 1):
            liste_binaire = []
            valeur_central = image_grise[i, j]


            voisins = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j + 1),
                       (i + 1, j + 1), (i + 1, j), (i + 1, j - 1), (i, j - 1)]

            for x, y in voisins:

                if image_grise[x, y] >= valeur_central:
                    liste_binaire.append(1)
                else:
                    liste_binaire.append(0)
            # Conversion de la liste binaire en nombre décimal
            nombre_decimale = int("".join(map(str, liste_binaire)), 2)

            nouvelle_matrice[i, j] = nombre_decimale

    return nouvelle_matrice


def appliquer_transformation_2(image_gris, radius):
    '''
    Description:
     Transformer les données visuelles complexes d’une image en
    ensembles de caractéristiques plus simples et plus significatives.


    Arguments:
    image_gris (numpy.ndarray): Un tableau 2D NumPy représentant une
    image en niveaux de gris.
    rayon (int): Un entier spécifiant le rayon du voisinage à considérer pour
    chaque pixel lors de la transformation.

    Retourne :
    numpy.ndarray: Un tableau 2D NumPy résultant de la transformation
    appliquée. Cette transformation est basée sur le rayon spécifié et peut
    modifier les caractéristiques visuelles originales de l'image.
    '''

    largeur, hauteur = image_gris.shape
    matrice_resultante = np.zeros((largeur, hauteur))

    for i in range(radius, largeur-radius):
        for j in range(radius, hauteur-radius):
          terme_1 = math.log10(1 + abs((image_gris[i, j+radius]) - 2 * (image_gris[i,j]) + (image_gris[i,j-radius])))
          terme_2 = math.log10(1 + abs((image_gris[i+radius, j]) - 2 * (image_gris[i,j]) + (image_gris[i-radius,j])))
          terme_3 = math.log10(1 + abs((image_gris[i-radius, j+radius]) - 2 * (image_gris[i,j]) + (image_gris[i+radius,j-radius])))
          matrice_resultante[i][j] = int(terme_1 + terme_2 + terme_3)

    return matrice_resultante

