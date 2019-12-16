import pandas as pd
import numpy as np
from numpy.random import randn
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sms
from scipy import stats


ds = pd.ExcelFile('Python_Analytics.xlsx')
ds1 = ds.parse('Employees who have left')
#print ds1
#print ds1.head()
#print ds1.keys()

nop = ds1.number_project
print nop
print nop.describe()

ax = nop.value_counts(normalize=False, sort=True, ascending=True).plot.barh(rot=0, color='brown')
ax.set_xlabel('NUMBER OF EMPLOYEES')
ax.set_ylabel('NUMBER OF PROJECTS')
ax.set_title('NUMBER OF PROJECTS EXECUTED BY EX-EMPLOYEES')


#plt.savefig('number_project.png')

plt.show()