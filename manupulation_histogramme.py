from traitement_image import *
import matplotlib.pyplot as plt

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