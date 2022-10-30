import pandas as pd
original_data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/corporate_attributes/company_ar.csv')
ar_YD = original_data[['entid','ANCHEYEAR','ANCHEDATE','BUSST']]
#加载base_info
base_info1 = pd.read_csv('base_info1.csv')
base_info2 = pd.read_csv('base_info2.csv')
ar_base1 = pd.merge(base_info1,ar_YD,on='entid',how='left')
ar_base1.to_csv('base_ar1.csv',index=False)
ar_base2 = pd.merge(base_info2,ar_YD,on='entid',how='left')
ar_base2.to_csv('base_ar2.csv',index=False)