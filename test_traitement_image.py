from traitement_image import*
import numpy as np

def test_appliquer_transformation_1_a():
    tableau_fourni = np.array([[2,5,3,9,15],
                               [6,7,9,1,5],
                               [3,8,4,2,9],
                               [2,3,5,8,2],
                               [1,2,3,2,1]])
    resultat= np.array([[0,0,0,0,0],
                        [0,20,32,255,0],
                        [0,32,205,191,0],
                        [0,248,144,32,0],
                        [0,0,0,0,0]])
    assert np.all(appliquer_transformation_1(tableau_fourni) == resultat), 'Erreur'

def test_appliquer_transformation_1_b():
    tableau_fourni = np.array([[88,20,56,49,145,123],
                               [60,17,99,121,55,56],
                               [80,8,45,100,99,30],
                               [255,23,155,88,12,78],
                               [100,200,23,82,155,254]])
    resultat= np.array([[0,0,0,0,0,0],
                        [0,251,24,32,119,0],
                        [0,255,124,66,129,0],
                        [0,191,2,105,255,0],
                        [0,0,0,0,0,0]])
    assert np.all(appliquer_transformation_1(tableau_fourni) == resultat), 'Erreur'
def test_appliquer_transformation_2_a():
    tableau_fourni = np.array([[88,102,133,49,145,123],
    [14,100,200,121,55,56],
    [40,101,92,100,99,30],
    [255,23,155,88,12,78],
    [100,200,23,82,155,254]])
    resultat = np.array([[0,0,0,0,0,0],
    [0,3,6,3,6,0],
    [0,6,5,3,5,0],
    [0,7,5,3,6,0],
    [0,0,0,0,0,0]])
    assert np.all(appliquer_transformation_2(tableau_fourni, 1) == resultat), 'Erreur'

def test_appliquer_transformation_2_b():
    tableau_fourni = np.array([[88,102,133,49,145,123],
    [14,100,200,121,55,56],
    [40,101,92,100,99,30],
    [255,23,155,88,12,78],
    [100,200,23,82,155,254]])
    resultat = np.array([[0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,4,5,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]])
    assert np.all(appliquer_transformation_2(tableau_fourni, 2) == resultat), 'Erreur'