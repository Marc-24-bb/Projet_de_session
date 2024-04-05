from manupulation_histogramme import *
import numpy as np

def test_calculer_histogramme():
    tableau_fourni = np.array([[255,160,10,49],
                               [20,170,1,121],
                               [30,233,230,100],
                               [255,23,155,88]])
    resultat = np.array([[4,0,2,3],
                         [3,2,2,2],
                         [4,0,2,3],
                         [2,3,2,2]])
    assert np.all(calculer_histogramme(tableau_fourni, 3) == resultat), 'Erreur'


def test_calculer_distance_1():
    histogramme_1 = (1,2,3,4,5)
    histogramme_2 = (2,3,4,5,6)
    assert calculer_distance_1(histogramme_1, histogramme_2) == 2.24, 'Erreur'

def test_calculer_distance_2():
    histogramme_1 = (1,2,3,4,5)
    histogramme_2 = (2,3,4,5,6)
    assert calculer_distance_2(histogramme_1, histogramme_2) == 5, 'Erreur'