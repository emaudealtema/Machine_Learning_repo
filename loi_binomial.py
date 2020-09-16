# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#x= z* o+ u

mu = 0.6
sigma = 0.2

dtst = np.random.normal(mu, sigma, 10000)

count, bins, ignored =plt.hist(dtst, bins=20, density=1,color="lightblue")

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * 
         np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=3, color='r')
plt.show()
#n = 10 
#p = 0.5
#data_binome = np.random.binomial(n, p, 1000)
#answer=sum(np.random.binomial(9, 0.1, 20000) == 0)/20000

