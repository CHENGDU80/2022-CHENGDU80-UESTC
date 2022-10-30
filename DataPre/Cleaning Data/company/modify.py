import pandas as pd
import numpy as np
from datetime import datetime
original_data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/corporate_attributes/company_modify.csv')
#数据增强处理
times = original_data['ALTTIME'].copy()
for i in range(len(original_data)):
    if np.isnan(times[i]):
        times[i] = 0
processed_data = original_data.copy()
processed_data = processed_data.dropna(axis=0)
#计算一年的修改频率
entids = processed_data['entid']
entid_unique = entids.drop_duplicates().tolist()
process = pd.DataFrame()
for i in range(len(entid_unique)):
    entid = entid_unique[i]
    data = processed_data[processed_data['entid'] == entid].copy()
    dates = data['ALTDATE'].values
    data_year = []
    for j in range(len(dates)):
        date = dates[j]
        year = int(date[0:4])
        data_year.append(year)
    data['Year'] = data_year
    process = pd.concat([process,data])

modify_data = pd.DataFrame()
for i in range(len(entid_unique)):
    entid = entid_unique[i]
    data = process[process['entid']==entid].copy()
    years = data['Year'].drop_duplicates().tolist()
    frequency = []
    for j in range(len(years)):
        year = years[j]
        f = np.sum(data[data['Year']==year]['ALTTIME'])
        frequency.append(f)
    p_data = data.drop_duplicates(subset=['entid','Year']).copy()
    p_data['Frequency'] = frequency
    modify_data = pd.concat([modify_data,p_data])

modify_info = modify_data[['entid','Year','Frequency']]
stocking_data1 = pd.read_csv('stocking_asset1.csv')
stocking_modify1 = pd.merge(stocking_data1,modify_info,on='entid',how='left')
stocking_modify1.to_csv('stocking_modify1.csv',index=False)
stocking_data2 = pd.read_csv('stocking_asset2.csv')
stocking_modify2 = pd.merge(stocking_data2,modify_info,on='entid',how='left')
stocking_modify2.to_csv('stocking_modify2.csv',index=False)