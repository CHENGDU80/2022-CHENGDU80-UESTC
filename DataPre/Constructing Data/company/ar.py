import pandas as pd
original_data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/corporate_attributes/company_ar.csv')
ar_YD = original_data[['entid','ANCHEYEAR','ANCHEDATE','BUSST']]
#加载base_info
base_info = pd.read_csv('base_info.csv')
label_base = pd.read_csv('label_base.csv')
ar_base = pd.merge(base_info,ar_YD,on='entid',how='left')
ar_base.to_csv('base_ar.csv',index=False)
label_ar = pd.merge(label_base,ar_YD,on='entid',how='left')
label_ar.to_csv('label_ar.csv',index=False)