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

le = ds1.last_evaluation
print le
print le.describe()

bins = [0.45, 0.55, 0.65, 0.75, 0.85, 0.95, 1.05]
cats = pd.cut(le, bins)
print cats
print pd.value_counts(cats)

ax = cats.value_counts(normalize=False, sort=True, ascending=True).plot.barh(rot=0, color='brown')
ax.set_xlabel('Number of Employees')
ax.set_ylabel('Last Evaluation')
ax.set_title('Last Evaluation of ex-Employees')

#plt.savefig('last evaluation.png')

plt.show()