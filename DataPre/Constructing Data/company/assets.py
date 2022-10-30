import pandas as pd
import numpy as np
original_data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/corporate_attributes/company_ar_assetsinfo.csv')
asset_data = original_data[['entid','ASSGRO','MAIBUSINC','NETINC','TOTEQU','VENDINC']]
#拼接结果
base_ar = pd.read_csv('base_ar.csv')
ar_asset = pd.merge(base_ar,asset_data,on='entid',how='left')
ar_asset.to_csv('ar_asset.csv',index=False)
label_ar = pd.read_csv('label_ar.csv')
label_asset = pd.merge(label_ar,asset_data,on='entid',how='left')
label_asset.to_csv('label_asset.csv',index=False)