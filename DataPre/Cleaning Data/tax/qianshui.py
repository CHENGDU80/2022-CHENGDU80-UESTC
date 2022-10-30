import pandas as pd
import numpy as np
original_data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/corporate_attributes/tax_qianshui.csv')
taxtype = original_data['taxtype']
debt = original_data['debt'].copy()
for i in range(len(original_data)):
    if isinstance(debt[i],str):
        continue
    elif np.isnan(debt[i]):
        debt[i] = 0
qs_data = original_data.copy()
qs_data['debt'] = debt
qs_info = qs_data[['entid','debt','taxtype']]
stocking_inv1 = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Cleaning Data/el/stocking_inv1.csv')
inv_qs1 = pd.merge(stocking_inv1,qs_info,on='entid',how='left')
inv_qs1.to_csv('inv_qs1.csv',index=False)
stocking_inv2 = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Cleaning Data/el/stocking_inv2.csv')
inv_qs2 = pd.merge(stocking_inv2,qs_info,on='entid',how='left')
inv_qs2.to_csv('inv_qs2.csv',index=False)