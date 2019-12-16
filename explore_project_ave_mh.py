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

avemh = ds1.average_montly_hours
print avemh
print avemh.describe()

bins = [126, 163, 200, 237, 274, 311]
cats = pd.cut(avemh, bins)
print cats
print pd.value_counts(cats)
sad = pd.value_counts(cats)

#sad.to_excel('ave_mh.xlsx')

ax = cats.value_counts(normalize=False, sort=True, ascending=True).plot.barh(rot=0, color='brown')
ax.set_xlabel('NUMBER OF EMPLOYEES')
ax.set_ylabel('AVERAGE MONTHLY HOURS')
ax.set_title('AVERAGE MONTHLY HOURS OF EMPLOYEES')

#plt.savefig('average monthly hours.png')

#plt.show()