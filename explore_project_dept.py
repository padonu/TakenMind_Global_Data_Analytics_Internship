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

dp = ds1.dept
print dp
#print dp.describe()

ax = dp.value_counts(normalize=False, sort=True, ascending=True).plot.barh(rot=0, color='brown')
ax.set_xlabel('Number of ex-Employees')
ax.set_ylabel('Department')
ax.set_title('Departments of ex-Employees')

#plt.savefig('department.png')

plt.show()