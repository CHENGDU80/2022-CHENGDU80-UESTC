import pandas as pd
import numpy as np
import tqdm
first1 = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Constructing Data/tax/year_abnormal.csv')
first2 = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/Constructing Data/tax/label_abnormal.csv')
columns = first1.columns.values.tolist()
def process_data(dataset):
    data = dataset.copy()
    data['ASSGRO'] = data['ASSGRO'].fillna(0)
    data['MAIBUSINC'] = data['MAIBUSINC'].fillna(0)
    data['NETINC'] = data['NETINC'].fillna(0)
    data['VENDINC'] = data['VENDINC'].fillna(0)
    data['TOTEQU'] = data['TOTEQU'].fillna(0)
    data['Frequency'] = data['Frequency'].fillna(0)
    data['taxtype'] = data['taxtype'].fillna(10)
    data['debt'] = data['debt'].fillna(0)
    data['tax_state'] = data['tax_state'].fillna(5)
    data['CONAM_new'] = data['CONAM_new'].fillna(0)
    data['CONPROP_new'] = data['CONPROP_new'].fillna(0)
    data['ttype'] = data['ttype'].fillna(5)
    return data
dataset1 = process_data(first1)
dataset2 = process_data(first2)
def supplement_data(dataset):
    data = dataset.copy()
    data = data.dropna(axis=0,subset=['ANCHEYEAR'])
    years = data['Year'].copy().tolist()
    anyears = data['ANCHEYEAR'].tolist()
    for i in range(len(data)):
        if np.isnan(years[i]):
            years[i] = anyears[i]
    s_data = data.copy()
    s_data['Year'] = years
    return s_data
s_data1 = supplement_data(dataset1)
s_data2 = supplement_data(dataset2)
def Ratio_compute(dataset):
    unique = dataset[['entid','ANCHEYEAR']].drop_duplicates().values
    ids = unique[:,0]
    years = unique[:,1]
    ratio_data = pd.DataFrame()
    for i in tqdm.trange(len(unique)):
        id = ids[i]
        year = years[i]
        data = dataset[(dataset['entid']==id) & (dataset['ANCHEYEAR']==year)].copy()
        num = len(data)
        ratios = data['Ratio'].tolist()
        max_ratio = max(ratios)
        if max_ratio > 100/num:
            item = data[data['Ratio']==max_ratio]
            ratio_data = pd.concat([ratio_data,item])
        else:
            initial = 0
            remain = num
            for j in range(len(ratios)):
                if np.isnan(ratios[j]) == False:
                    initial = initial+ratios[j]
                    remain = remain - 1
            for j in range(len(ratios)):
                if np.isnan(ratios[j]):
                    ratios[j] = (100-initial)/remain
            ratio_max = max(ratios)
            data['Ratio'] = ratios
            item = data[data['Ratio']==ratio_max]
            ratio_data = pd.concat([ratio_data,item])
    return ratio_data
r_data1 = Ratio_compute(s_data1)
r_data2 = Ratio_compute(s_data2)
def Debt_process(dataset):
    debts = dataset['debt'].copy().tolist()
    for i in range(len(debts)):
        debt = debts[i]
        if isinstance(debt, str):
            if len(debt) < 4:
                debts[i] = float(debt)
            else:
                debts[i] = float(debt[3:])
    data = dataset.copy()
    data['debt'] = debts
    return data
d_data1 = Debt_process(r_data1)
d_data2 = Debt_process(r_data2)
d_columns = d_data1.columns.values.tolist()
d_columns.remove('CaseType')
d_columns.append('CaseType')
final_constructed1 = d_data1[d_columns]
final_constructed2 = d_data2[d_columns]
final_constructed1.to_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/final_constructed1.csv',index=False)
final_constructed2.to_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/final_constructed2.csv',index=False)