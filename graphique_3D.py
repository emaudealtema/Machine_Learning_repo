# -*- coding: utf-8 -*-

"""
import numpy as np
import pandas as pd

dataset = pd.DataFrame(np.random.rand(25,2), columns=['ventes','benefice'])

dataset.plot.scatter(x='ventes', y='benefice') """


""" 
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


chart = plt.figure()
chart3d = chart.add_subplot(111,projection='3d')

axe_x, axe_y, axe_z = axes3d.get_test_data(0.10)

chart3d.plot_wireframe(axe_x, axe_y, axe_z,color='r',rstride=15,cstride=10)
plt.show(['darck_background', 'fast'])"""


from pylab import *
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


fig = figure()
ax = Axes3D(fig)

X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)

X, Y = np.meshgrid(X, X)

R =np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')

plt.show