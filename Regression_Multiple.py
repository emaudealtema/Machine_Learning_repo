# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:02:50 2020

@author: Emaude Altema
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression



data = pd.read_csv('boston_house_prices.csv')

x = data.drop("MEDV", axis=1)
y = data.MEDV

plt.figure(figsize=(75, 5))

for i, col in enumerate(x.columns):
        plt.subplot(1, 13, i+1)
        x = data[col]
        y = y
        plt.plot(x, y, 'o')
        # creation de la ligne de regression
        plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1)) (np.unique(x)))
        plt.style.use(['dark_background','fast'])
        plt.title(col)
        plt.xlabel(col)
        plt.ylabel('prix')
        
        
# Fractionnement des donnees entre train et test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)


scaler = StandardScaler()
scaler.fit(x_train)
scaler.fi(x_test)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

#contruction de notre model de regerssion


regressor=LinearRegression()
regressor.fit(x_train,y_train) # initialize & fit the model
y_pred=regressor.predict(x_test) # now predic

#j'adapte le model de regression lineaire a l'ensemble de donnees d'apprentissagege
#regressor.fit(x_train, y_train)

#faire de nouvelle prediction
#y_pred = regressor.predict(x_test)

plt.style.use("bmh")
plt.scartter(y_pred, y_test)
plt.show


regressor.predict(scaler.fit_transform(np.array([[0.17331,0,9.69,0,0.585,5.707,54,2.3817,6,391,19.2,396.9,12.01]])))