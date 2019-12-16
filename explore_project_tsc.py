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

tsc = ds1.time_spend_company
print tsc
print tsc.describe()
print tsc.unique()

ax = tsc.value_counts(normalize=False, sort=True, ascending=True).plot.barh(rot=0, color='brown')
ax.set_xlabel('NUMBER OF EX-EMPLOYEES')
ax.set_ylabel('TIME SPENT AT COMPANY')
ax.set_title('TIME SPENT AT COMPANY BY EX-EMPLOYEES')

#plt.savefig('time_spend_company.png')

plt.show()