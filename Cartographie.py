# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fig = plt.figure(figsize=(25, 15))


#axe = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
#axe = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
#axe = fig.add_subplot(1, 1, 1, projection=ccrs.LambertCylindrical())
axe = fig.add_subplot(1, 1, 1, projection=ccrs.Mollweide())
#axe = fig.add_subplot(1, 1, 1, projection=ccrs.AzimuthalEquidistant())
#axe = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
#axe = fig.add_subplot(1, 1, 1, projection=ccrs.InterruptedGoodeHomolosine())
# Liste de projection cartography
#AzimuthalEquidistant  : Une projection azimutal equidistante
#LambertCylindrical
#Mollweide
# RObinson
#InterruptedGoodeHomelosine

axe.set_extent((251, 21, 75, -35))

axe.stock_img()
axe.coastlines()
 
axe.tissot(facecolor='purple', alpha=0.8)