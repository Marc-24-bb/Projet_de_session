from traitement_image import *
import math

def calculer_histogramme(tableau_2d, w):
    '''
    Description:
    Génère un histogramme pour chaque pixel de l'image en utilisant un
    carré de voisinage de taille spécifiée.


    Arguments:
    tableau_2D (numpy.ndarray): Un tableau 2D NumPy représentant une
    image.

    w (int): La taille du carré de voisinage autour de chaque pixel pour
    lequel l'histogramme est calculé.


    Retourne :
    numpy.ndarray: Un tableau 2D NumPy où chaque ligne représente un
    histogramme pour le carré correspondant de l'image.
    '''

    x = tableau_2d.shape[0]
    y = tableau_2d.shape[1]
    window = []
    max_val = np.max(tableau_2d)
    liste_hist = []
    for i in range(x - w + 1):
        for j in range(y - w + 1):
          window = tableau_2d[i:i+w, j:j+w]
          hist, _= np.histogram(window, bins=[0, max_val/4, max_val/2, (3*max_val)/4, max_val], range=(0, max_val))
          liste_hist.append(hist)
    return np.array(liste_hist)

def calculer_distance_1(histogramme_1, histogramme_2):
    '''
    Description:
    Calculer la distance entre deux histogrammes.


    Arguments:
    histogramme1 (numpy.ndarray): Premier histogramme sous forme de
    tableau 1D NumPy.

    histogramme2 (numpy.ndarray): Deuxième histogramme sous forme de
    tableau 1D NumPy

    Retourne :
    float: La distance entre les deux histogrammes.
    '''

    somme = 0
    for p, q in zip(histogramme_1, histogramme_2):
      résultat = (p-q)**2
      somme += résultat
      distance = round(math.sqrt(somme),2)
    return distance

def calculer_distance_2(histogramme_1, histogramme_2):
    '''
    Description:
    Calculer la distance entre deux histogrammes.


    Arguments:
    histogramme1 (numpy.ndarray): Premier histogramme sous forme de
    tableau 1D NumPy.

    histogramme2 (numpy.ndarray): Deuxième histogramme sous forme de
    tableau 1D NumPy

    Retourne :
    float: La distance entre les deux histogrammes.
    '''

    somme = 0
    for p, q in zip(histogramme_1, histogramme_2):
        résultat = abs(p-q)
        somme += résultat
        distance = round(somme,2)
    return distance

