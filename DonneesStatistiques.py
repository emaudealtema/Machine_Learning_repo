# -*- coding: utf-8 -*-
import pandas as pd



dataset = pd.read_csv('tendance_centrale.csv')

print("\n Mesure de la moyenne")
print("La  valeur moyennes dans la distribution")

moy = dataset.mean()
print(moy)


print("\n Mesure de la mediane")

print("la valeur mediane dans la distribution est")
print(dataset.median())
print("*******************************************")



print('la valeur la plus representee')
print(dataset.mode())
print("*************************************")


print("\n Ecart Type de mesure  ")
print('la valeur de la standard deviation est de')
print(dataset.std())
print("***************************")


print("\n Ecart type de mesure    ")
print('deteminons si les donnees etaient symetrique ou asymetriques')
print(dataset.skew())

#nous avons trouve des indices compris entre -1 et 1 donc la distribution est symetrique 