import numpy as np
import pandas as pd
data = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Online Data/training data/corporate_attributes/company_ar_socialfee.csv')
u_so1 = data['unPaidSocialInsSo1']
u_so2 = data['unPaidSocialInsSo2']
u_so3 = data['unPaidSocialInsSo3']
u_so4 = data['unPaidSocialInsSo4']
u_so5 = data['unPaidSocialInsSo5']
unPaid = (u_so1+u_so2+u_so3+u_so4+u_so5)/5
unPaid = unPaid.fillna(0)
social_data = data.copy()
social_data['Unpaid'] = unPaid
social = social_data[['entid','Unpaid']]
cleaned1 = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Cleaning Data/tax/year_abnormal1.csv',low_memory=False)
cleaned2 = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Cleaning Data/tax/year_abnormal2.csv',low_memory=False)
added1 = pd.merge(cleaned1,social,on='entid',how='left')
added2 = pd.merge(cleaned2,social,on='entid',how='left')
added1.to_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Cleaning Data/cleaned1.csv',index=False)
added2.to_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Cleaning Data/cleaned2.csv',index=False)