import pandas as pd
dataset = pd.read_csv('/Users/duanjingyuan/Documents/Fintech80 2021/data analysis/final_cleaned1.csv',low_memory=False)
debts = dataset['debt'].copy()
def Debt_process(dataset):
    debts = dataset['debt'].copy().tolist()
    for i in range(len(debts)):
        debt = debts[i]
        if isinstance(debt,str):
            if len(debt) < 4:
                debts[i] = float(debt)
            else:
                debts[i] = float(debt[3:])
    data = dataset.copy()
    data['debt'] = debts
    return data
data = Debt_process(dataset)
debts_n = data['debt']
data = data.to_csv('removed.csv',index=False)