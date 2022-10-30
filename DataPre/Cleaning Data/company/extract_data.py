import pandas as pd
import numpy as np
label_data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/label_risk_company.csv')
labels = label_data['entid']
uni = labels.drop_duplicates().tolist()
abnormal = []
#检验是否一致
for i in range(len(uni)):
    id = uni[i]
    data = label_data.loc[label_data['entid']==id]
    types = data['CaseType'].drop_duplicates().tolist()
    if len(types) > 1:
        abnormal.append(id)
    else:
        continue
if len(abnormal) == 0:
    print('ok!')
#两类数据表：一类补4，一类全部忽略
origin_data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/corporate_attributes/company_base_info.csv')
entids = origin_data['entid'].drop_duplicates().tolist()
valid_types = label_data[['entid','CaseType']]
types_data = pd.merge(origin_data,valid_types,on='entid',how='left')
casetypes = types_data['CaseType'].copy()
for i in range(len(types_data)):
    if np.isnan(casetypes[i]):
        casetypes[i] = 4
extract1 = types_data.copy()
extract1['CaseType'] = casetypes
extract1.to_csv('extract1.csv',index=False)
extract2 = pd.merge(origin_data,valid_types,on='entid')
extract2.to_csv('extract2.csv',index=False)
