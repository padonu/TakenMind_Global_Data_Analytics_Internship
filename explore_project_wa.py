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

wa = ds1.Work_accident
print wa
print wa.describe()

ax = wa.value_counts(normalize=False, sort=False, ascending=True).plot.bar(rot=0, color='brown')
ax.set_ylabel('NUMBER OF EX-EMPLOYEES')
ax.set_xlabel('WORK ACCIDENT')
ax.set_title('WORK ACCIDENT OF EX-EMPLOYEES')


#plt.savefig('work accident.png')

plt.show()