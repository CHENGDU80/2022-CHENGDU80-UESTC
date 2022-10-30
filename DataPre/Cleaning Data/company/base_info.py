#本代码是为了处理company_base_info.csv
import pandas as pd
import numpy as np
#加载原始数据
original_data1 = pd.read_csv('extract1.csv')
file_name1 = 'base_info1.csv'
original_data2 = pd.read_csv('extract2.csv')
file_name2 = 'base_info2.csv'
def base_process(original_data,filename):
    #设置初始值为10，若有荣誉，则每个公司的评分升高1（最高加10分），若发布非法广告降2（最低减10分），若有资金和补贴则按照补贴级别设定奖励，最高设为10，有年度报告则升高5
    #计算各公司的评分
    action_grades = 10*np.ones((len(original_data),1)) #初始值
    #提取特征
    honor = original_data['honor_num']
    illegaled = original_data['illegad_num']
    yea_sub = original_data['yea_sub']
    web_dum = original_data['web_dum']
    #补0操作
    honor_r = honor.copy()
    for i in range(len(honor)):
        if np.isnan(honor[i]):
            honor_r[i] = 0
    illegaled_r = illegaled.copy()
    for i in range(len(illegaled)):
        if np.isnan(illegaled[i]):
            illegaled_r[i] = 0
    yea_r = yea_sub.copy()
    for i in range(len(yea_sub)):
        if np.isnan(yea_sub[i]):
            yea_r[i] = 0
    #计算评分增量
    incremental = np.zeros((len(original_data),1))
    for i in range(len(incremental)):
        hi = min(2*honor_r[i],10)
        ii = max(-2*illegaled_r[i],-10)
        wi = 5*web_dum[i]

        #将补贴分为5档：2（10以下）、4（50以下）、6（100以下）、8（2000以下）、10（10000以上）
        if yea_r[i] == 0:
            yi = 0
        elif yea_r[i] <= 10:
            yi = 2
        elif yea_r[i] <= 50:
            yi = 4
        elif yea_r[i] <= 100:
            yi = 6
        elif yea_r[i] <= 2000:
            yi = 8
        else:
            yi = 10
        incremental[i,0] = hi+ii+yi+wi
    #计算各公司得分
    action_grades = action_grades+incremental
    #grade_data
    grade_data = original_data.copy()
    grade_data['Action_Grade'] = action_grades[:,0]
    #社交关系（2:4:4）
    parnum = original_data['PARNUM']
    limparnum = original_data['LIMPARNUM']
    parform = original_data['PARFORM']
    parnum_r = parnum.copy()
    limparnum_r = limparnum.copy()
    parform_r = parform.copy()
    for i in range(len(original_data)):
        if np.isnan(parnum[i]):
            parnum_r[i] = 0
        if np.isnan(limparnum[0]):
            limparnum_r[i] = 0
        pf = parform[i]
        if isinstance(pf,str):
            if pf == '!':
                parform_r[i] = 1
            else:
                parform_r[i] = int(parform[i])
        elif np.isnan(pf):
            parform_r[i] = 0
    #计算社交关系
    social = 0.2*parnum_r+0.4*limparnum_r+0.4*parform_r
    social_data = grade_data.copy()
    social_data['Social'] = social
    #企业违约：均正常（0）、业务异常（1）、税务异常（2）、都异常（4）
    cancel = original_data['cancel_dum']
    tax  = original_data['tax_dum']
    inconfidence = np.zeros((len(original_data),1))
    for i in range(len(original_data)):
        if cancel[i] and tax[i]:
            inconfidence[i,0] = 4
        elif (cancel[i] == 0) and tax[i]:
            inconfidence[i,0] = 2
        elif cancel[i] and (tax[i] == 0):
            inconfidence[i,0] = 1
    inconfidence_data = social_data.copy()
    inconfidence_data['Inconfidence'] = inconfidence[:,0]
    reccap = original_data['RECCAP']
    reccap_r = reccap.copy()
    for i in range(len(original_data)):
        if np.isnan(reccap[i]):
            reccap_r[i] = 0
    reccap_data = inconfidence_data.copy()
    reccap_data['RECCAP'] = reccap_r
    #绘制大表
    column_list = ['entid','Action_Grade','ENTTYPE','INDUSTRYPHY','RECCAP','Social','Inconfidence','CaseType']
    base_info = reccap_data[column_list]
    #存储数据
    base_info.to_csv(filename,index=False)
    return base_info
base_info1 = base_process(original_data1,file_name1)
base_info2 = base_process(original_data2,file_name2)