import pandas as pd
import numpy as np
original_data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/corporate_attributes/company_ar_alterstockinfo.csv')
#按照entid和ANCHEYEAR进行计算
ori_trans = original_data['TRANSAMAFT'].copy()
for i in range(len(original_data)):
    if np.isnan(ori_trans[i]):
        ori_trans[i] = 0
processed_data = original_data.copy()
processed_data['TRANSAMAFT'] = ori_trans
key_content = processed_data[['entid','ANCHEYEAR']]
key_unique = key_content.drop_duplicates(subset=['entid','ANCHEYEAR'])
key_unique = key_unique.values
entids = key_unique[:,0]
years = key_unique[:,1]
items = pd.DataFrame()
for i in range(len(entids)):
    entid = entids[i]
    year = years[i]
    data = processed_data[(processed_data['entid']==entid) & (processed_data['ANCHEYEAR']==year)].copy()
    #提取所有的TRANSAMAFT
    scale = data['TRANSAMAFT']
    if np.sum(scale) == 0:
        ratio = [1]
    else:
        ratio = scale/np.sum(scale)
    data['Ratio'] = ratio
    item = data[data['Ratio'] == max(ratio)]
    items = pd.concat([items,item])
#提取特征
stocking_data = items[['entid','Ratio']]
asset_info = pd.read_csv('ar_asset.csv')
stocking_asset = pd.merge(asset_info,stocking_data,on='entid',how='left')
stocking_asset.to_csv('stocking_asset.csv',index=False)
label_asset = pd.read_csv('label_asset.csv')
label_stocking = pd.merge(label_asset,stocking_data,on='entid',how='left')
label_stocking.to_csv('label_stocking.csv',index=False)