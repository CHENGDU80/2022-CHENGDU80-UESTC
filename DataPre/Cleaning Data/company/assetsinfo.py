import pandas as pd
import numpy as np
original_data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/corporate_attributes/company_ar_assetsinfo.csv')
asset_data = original_data[['entid','ASSGRO','MAIBUSINC','NETINC','TOTEQU','VENDINC']]
#拼接结果
base_ar1 = pd.read_csv('base_ar1.csv')
ar_asset1 = pd.merge(base_ar1,asset_data,on='entid',how='left')
ar_asset1.to_csv('ar_asset1.csv',index=False)
base_ar2 = pd.read_csv('base_ar2.csv')
ar_asset2 = pd.merge(base_ar2,asset_data,on='entid',how='left')
ar_asset2.to_csv('ar_asset2.csv',index=False)