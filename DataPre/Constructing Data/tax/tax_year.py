import pandas as pd
import numpy as np
original_data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/corporate_attributes/tax_year.csv')
year_data = original_data[['entid','total_profit','assets_re']]
qs = pd.read_csv('inv_qs.csv',low_memory=False)
year_qs = pd.merge(qs,year_data,on='entid',how='left')
profit = year_qs['total_profit'].copy()
for i in range(len(year_qs)):
    if np.isnan(profit[i]):
        profit[i] = 0
qs_year = year_qs.copy()
qs_year['total_profit'] = profit
qs_year.to_csv('year_qs.csv',index=False)
label_qs = pd.read_csv('label_qs.csv',low_memory=False)
label_year = pd.merge(label_qs,year_data,on='entid',how='left')
label_profit = label_year['total_profit'].copy()
for i in range(len(label_profit)):
    if np.isnan(label_profit[i]):
        label_profit[i] = 0
year_label = label_year.copy()
year_label['total_profit'] = label_profit
year_label.to_csv('label_year.csv',index=False)