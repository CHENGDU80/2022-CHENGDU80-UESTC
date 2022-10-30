import pandas as pd
import numpy as np
original_data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/corporate_attributes/tax_abnormal.csv')
abnormal = original_data[['entid','tax_state']]
year_data = pd.read_csv('year_qs.csv',low_memory=False)
year_abnormal = pd.merge(year_data,abnormal,on='entid',how='left')
year_abnormal.to_csv('year_abnormal.csv',index=False)
year_abnormal.to_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Constructed_test.csv',index=False)
label_year = pd.read_csv('label_year.csv',low_memory=False)
label_abnormal = pd.merge(label_year,abnormal,on='entid',how='left')
label_abnormal.to_csv('label_abnormal.csv',index=False)
label_abnormal.to_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Matched_test.csv',index=False)