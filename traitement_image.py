from PIL import Image
import numpy as np


def appliquer_rgb_to_gry(chemin_a, chemin_b):

    image = Image.open(chemin_a)
    largeur, hauteur = image_couleur.size

    for i in range(hauteur):
        for j in range(largeur):
            r, g, b = image_couleur.getpixel((i, j))
            valeur_gris = int((r + g + b)/3)
            image.putpixel((i, j), (valeur_gris. valeur_gris, valeur_gris))

    image.save(chemin_b)


def appliquer_transfromation_1(image_grise):
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


