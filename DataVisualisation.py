# -*- coding: utf-8 -*-
import numpy as np

import matplotlib.pyplot as plt
 
import pandas as pd
 
dtst = pd.read_csv('graph_1.csv')
axe_abscisse = dtst.iloc[:,0]
axe_ordonnee = dtst.iloc[:,-1]
 
 # mise en place de graphe simple
plt.plot(axe_abscisse, axe_ordonnee)
 
 # labeliser l'Axe et titre
 
plt.title("evolution du portefeuille")
plt.xlabel("Temps")
plt.ylabel("Montant du capital")
 
 #formater le ligne de couleur
plt.plot(axe_abscisse,axe_ordonnee, 'green')
          
          #sauvegarder en format pdf
plt.savefig('illustration_graph_1.pdf', format='pdf')
 


