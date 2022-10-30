import pandas as pd
import numpy as np
original_data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/corporate_attributes/tax_abnormal.csv')
abnormal = original_data[['entid','tax_state']]
year_data1 = pd.read_csv('year_qs1.csv',low_memory=False)
year_abnormal1 = pd.merge(year_data1,abnormal,on='entid',how='left')
year_abnormal1.to_csv('year_abnormal1.csv',index=False)
year_abnormal1.to_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Cleaned_data1.csv',index=False)
year_data2 = pd.read_csv('year_qs2.csv',low_memory=False)
year_abnormal2 = pd.merge(year_data2,abnormal,on='entid',how='left')
year_abnormal2.to_csv('year_abnormal2.csv',index=False)
year_abnormal2.to_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Cleaned_data2.csv',index=False)
