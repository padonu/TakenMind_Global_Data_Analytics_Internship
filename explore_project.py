import pandas as pd
import numpy as np
from numpy.random import randn
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sms
from scipy import stats



ds = pd.ExcelFile('Python_Analytics.xlsx')
ds1 = ds.parse('Employees who have left')
print ds1
print ds1.head()
print ds1.keys()

sl = ds1.satisfaction_level
print sl
print sl.describe()
bins = [0.09, 0.19, 0.29, 0.39, 0.49, 0.59, 0.69, 0.79, 0.89, 0.99]
cats = pd.cut(sl, bins)
print cats
print pd.value_counts(cats)


plt.style.use('fivethirtyeight')
ax = cats.value_counts(normalize=False, sort=True, ascending=True).plot.barh(color='brown')

ax.set_xlabel('Number of ex-Employees')
ax.set_ylabel('Satisfaction Levels')
ax.set_title('Satisfaction Level of ex-Employees')

#plt.savefig('satisfaction_level.png')
plt.show()


#print ds1.describe()



#ds1_sats_lvl = ds1.pivot('Emp ID', 'time_spend_company', 'satisfaction_level')




