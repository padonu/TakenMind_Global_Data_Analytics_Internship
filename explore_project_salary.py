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

sal = ds1.salary
print sal
#print dp.describe()

ax = sal.value_counts(normalize=False, sort=False, ascending=True).plot.bar(rot=0, color='brown')
ax.set_ylabel('NUMBER OF EX-EMPLOYEES')
ax.set_xlabel('SALARY')
ax.set_title('SALARY OF EX-EMPLOYEES')

#plt.savefig('salary.png')

plt.show()