import pandas as pd
import numpy as np
original_data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/corporate_attributes/tax_year.csv')
year_data = original_data[['entid','total_profit','assets_re']]
qs1 = pd.read_csv('inv_qs1.csv',low_memory=False)
year_qs1 = pd.merge(qs1,year_data,on='entid',how='left')
profit1 = year_qs1['total_profit'].copy()
for i in range(len(year_qs1)):
    if np.isnan(profit1[i]):
        profit1[i] = 0
qs_year1 = year_qs1.copy()
qs_year1['total_profit'] = profit1
qs_year1.to_csv('year_qs1.csv',index=False)
qs2 = pd.read_csv('inv_qs2.csv',low_memory=False)
year_qs2 = pd.merge(qs2,year_data,on='entid',how='left')
profit2 = year_qs2['total_profit'].copy()
for i in range(len(year_qs2)):
    if np.isnan(profit2[i]):
        profit2[i] = 0
qs_year2 = year_qs2.copy()
qs_year2['total_profit'] = profit2
qs_year2.to_csv('year_qs2.csv',index=False)