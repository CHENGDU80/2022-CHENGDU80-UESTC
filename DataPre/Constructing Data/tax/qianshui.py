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
stocking_inv = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Constructing Data/el/stocking_inv.csv')
inv_qs = pd.merge(stocking_inv,qs_info,on='entid',how='left')
inv_qs.to_csv('inv_qs.csv',index=False)
label_inv = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Constructing Data/el/label_inv.csv')
label_qs = pd.merge(label_inv,qs_info,on='entid',how='left')
label_qs.to_csv('label_qs.csv',index=False)