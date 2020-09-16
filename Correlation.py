# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 02:00:13 2020

@author: Emaude Altema
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot
from scipy.stats.stats import pearsonr
from scipy import stats

dtst = pd.read_csv('iris.csv')

plot = sns.pairplot(dtst, kind='scatter')
plt.show()

plot.savefig("dispersion2.pdf", format='pdf')

x = dtst['longueur_petal']
y = dtst['largeur_petal']

cor = stats.pearsonr(x, y)
print(cor)

x1 = dtst['longueur_sepal']
y1 = dtst['largeur_sepal']

noncor = stats.pearsonr(x1, y1)
print(noncor)
