import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import sklearn as skl
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')



att = pd.ExcelFile('Python_Analytics.xlsx')
ds1 = att.parse('Existing employees')
df1 = att.parse('Employees who have left')
#print df1

promExist = ds1.promotion_last_5years.apply(lambda x: 'Yes' if x==1 else 'NO')
print promExist
promLeft = df1.promotion_last_5years.apply(lambda x: 'Yes' if x==1 else 'No')
print promLeft

workAccExist = ds1.Work_accident.apply(lambda x: 'Yes' if x==1 else 'No')
print workAccExist
workAccLeft = df1.Work_accident.apply(lambda x: 'Yes' if x==1 else 'No')
print workAccLeft


##### Employees that have left
#ax = sns.boxplot(x='dept', y='satisfaction_level', hue='promotion_last_5years', data=df1)
plt.yticks(np.arange(0, 1, step=0.05))
plt.legend(loc=1)
plt.title('Satisfaction Level against Department with respect to Promotion in the Last 5 years of ex - Employees')
#plt.show()

###### Existing employees
#ay = sns.boxplot(x='dept', y='satisfaction_level', hue='promotion_last_5years', data=ds1)
plt.yticks(np.arange(0, 1, step=0.05))
plt.legend(loc=1)
plt.title('Satisfaction Level against Department with respect to Promotion in the Last 5 years of Existing Employees')
#plt.show()

#ax = sns.boxplot(x='dept', y='satisfaction_level', hue='Work_accident', data=df1)
plt.yticks(np.arange(0, 1, step=0.05))
plt.legend(loc=1)
plt.title('Satisfaction Level against Department with respect to Work Accident of ex - Employees')
#plt.show()

###### Existing employees
#ay = sns.boxplot(x='dept', y='satisfaction_level', hue='Work_accident', data=ds1)
plt.yticks(np.arange(0, 1, step=0.05))
plt.legend(loc=1)
plt.title('Satisfaction Level against Department with respect to Work Accident of Existing Employees')
#plt.show()


ax = sns.boxplot(x='salary', y='satisfaction_level', data=df1)
plt.yticks(np.arange(0, 1, step=0.05))
plt.legend(loc=1)
plt.title('Distribution of Satisfaction Level of ex - Employees with respect to Salary')
plt.show()

###### Existing employees
ay = sns.boxplot(x='salary', y='satisfaction_level', data=ds1)
plt.yticks(np.arange(0, 1, step=0.05))
plt.legend(loc=1)
plt.title('Distribution of Satisfaction Level of Existing Employees with respect to Salary')
plt.show()




#ax = sns.boxplot(x='salary', y='last_evaluation', data=df1)
plt.yticks(np.arange(0, 1, step=0.05))
#plt.show()

###### Existing employees
#ay = sns.boxplot(x='salary', y='last_evaluation', data=ds1)
plt.yticks(np.arange(0, 1, step=0.05))
#plt.show()
