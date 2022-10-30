import pandas as pd
import numpy as np
original_data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/corporate_attributes/el_company_history_inv.csv')
conam_before = original_data['CONAM_before'].copy()
conam_after = original_data['CONAM_after'].copy()
ID = []
for i in range(len(original_data)):
    if np.isnan(conam_before[i]):
        conam_before[i] = 0
    if np.isnan(conam_after[i]):
        conam_after[i] = 0
    ID.append(i+1)
conam_new = conam_after-conam_before
conam_data = original_data.copy()
conam_data['CONAM_new'] = conam_new
conam_data['ID'] = ID
conprop_before = original_data['CONPROP_before'].copy()
conprop_after = original_data['CONPROP_after'].copy()
for i in range(len(original_data)):
    if np.isnan(conprop_before[i]):
        conprop_before[i] = 0
    if np.isnan(conprop_after[i]):
        conprop_after[i] = 0
conprop_new = conprop_after-conprop_before
conprop_data = conam_data.copy()
conprop_data['CONPROP_new'] = conprop_new
#补全ttype：最大值
valid_data = conprop_data[['ID','entid','CONAM_new','CONPROP_new','ttype']]
null_data = valid_data[valid_data.isnull().T.any()].copy()
valid_data = valid_data.dropna(axis=0)
ids = null_data['entid'].tolist()
types = []
for i in range(len(ids)):
    id = ids[i]
    data = valid_data[valid_data['entid']==id]
    u_data = data['ttype'].drop_duplicates().tolist()
    if len(u_data) == 0:
        type = 5
    else:
        nums = []
        for j in range(len(u_data)):
            num = len(data[data['ttype']==u_data[j]])
            nums.append(num)
        index = 0
        for j in range(len(u_data)):
            if nums[j] > nums[index]:
                index = j
        type = u_data[index]
    types.append(type)
Ids = null_data['ID'].tolist()
new_data = conprop_data.copy()
for i in range(len(Ids)):
    Id = Ids[i]
    if i == len(Ids):
        index = new_data.index[new_data['ID']==Id]
        new_data.loc[index,'ttype'] = 5
    else:
        index = new_data.index[new_data['ID'] == Id]
        new_data.loc[index,'ttype'] = types[i]
modify_data1 = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Cleaning Data/company/stocking_modify1.csv')
inv_data = new_data[['entid','CONAM_new','CONPROP_new','ttype']]
stocking_inv1 = pd.merge(modify_data1,inv_data,on='entid',how='left')
stocking_inv1.to_csv('stocking_inv1.csv',index=False)
modify_data2 = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Cleaning Data/company/stocking_modify2.csv')
stocking_inv2 = pd.merge(modify_data2,inv_data,on='entid',how='left')
stocking_inv2.to_csv('stocking_inv2.csv',index=False)