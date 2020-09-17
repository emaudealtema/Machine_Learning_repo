# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 21:19:22 2020

@author: Emaude Altema
"""


import matplotlib.pyplot as plt
import cartopy.crs as ccrs
fig = plt.figure(figsize=(25, 15))
axe = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
# Liste des projection cartopy
#Azimuthalequidistant: une projection azimutale equidistsnte
# LambertCylindrical
#Mollweide
#RObinson
#interrupteGoodeHomolosine


axe.set_extent((251, 21,75, -35))

axe.stock_img()
axe.coastlines()
axe.tissot(facecolor='purple', alpha=0.8) 
