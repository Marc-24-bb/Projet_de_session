from traitement_image import *
import math

def calculer_histogramme(tableau_2d, w):
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
    somme = 0
    for p, q in zip(histogramme_1, histogramme_2):
      résultat = (p-q)**2
      somme += résultat
      distance = round(math.sqrt(somme),2)
    return distance

def calculer_distance_2(histogramme_1, histogramme_2):
    somme = 0
    for p, q in zip(histogramme_1, histogramme_2):
        résultat = abs(p-q)
        somme += résultat
        distance = round(somme,2)
    return distance

def regrouper_points(tableau, k, max_iterations):
    nombre_groupe = k
    point_centraux = k
