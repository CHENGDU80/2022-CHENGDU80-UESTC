#本代码是为了输出总体的情况
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Grid,Pie,Bar


# 绘制柱状图
def draw_bari(dataset,file_name):
    data = dataset.values
    i_0 = list(data[:,0])
    i_1 = list(data[:,1])
    i_2 = list(data[:,2])
    i_3 = list(data[:,3])
    i_4 = list(data[:,4])
    attrs = []
    ids = dataset['id'].tolist()
    for i in range(len(ids)):
        attrs.append(str(ids[i]))

    ind_bar = (
        Bar(init_opts=opts.InitOpts(width='640px',height='205px'))
        .add_xaxis(attrs)
        .add_yaxis('Risk0',i_0,stack='stack1')
        .add_yaxis('Risk1',i_1,stack='stack1')
        .add_yaxis('Risk2',i_2,stack='stack1')
        .add_yaxis('Risk3',i_3,stack='stack1')
        .add_yaxis('Risk4',i_4,stack='stack1')
        .set_global_opts(title_opts=opts.TitleOpts(title='Industry Risk Probabilities'),datazoom_opts=opts.DataZoomOpts(is_show=True),legend_opts=opts.LegendOpts(pos_right="0%"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    ind_bar.render('./htmls/'+file_name+'.html')


# 绘制柱状图
def draw_bare(dataset,file_name):
    data = dataset.values
    i_0 = list(data[:,0])
    i_1 = list(data[:,1])
    i_2 = list(data[:,2])
    i_3 = list(data[:,3])
    i_4 = list(data[:,4])
    attrs = []
    ids = dataset['id'].tolist()
    for i in range(len(ids)):
        attrs.append(str(ids[i]))

    ind_bar = (
        Bar(init_opts=opts.InitOpts(width='640px',height='205px'))
        .add_xaxis(attrs)
        .add_yaxis('Risk0',i_0,stack='stack1')
        .add_yaxis('Risk1',i_1,stack='stack1')
        .add_yaxis('Risk2',i_2,stack='stack1')
        .add_yaxis('Risk3',i_3,stack='stack1')
        .add_yaxis('Risk4',i_4,stack='stack1')
        .set_global_opts(title_opts=opts.TitleOpts(title='Enterprise Risk Probabilities'),datazoom_opts=opts.DataZoomOpts(is_show=True),legend_opts=opts.LegendOpts(pos_right="0%"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    ind_bar.render('./htmls/'+file_name+'.html')


if __name__ == '__main__':
    data = pd.read_csv('../DataPre/Cleaning Data/cleaned1.csv')

    # 按照entid进行去重
    unique_data = data.copy()
    unique_data = unique_data.drop_duplicates(subset=['entid'])
    type_attrs = unique_data['CaseType'].copy().drop_duplicates().sort_values().tolist()
    type_nums = []
    for i in range(len(type_attrs)):
        type_data = unique_data[unique_data['CaseType']==type_attrs[i]]
        type_nums.append(len(type_data))
    t_attrs = []
    for i in range(len(type_attrs)):
        t_attrs.append('Risk%d'%type_attrs[i])
    risk_attrs = t_attrs[:-1]
    risk_nums = type_nums[:-1]
    type_pie = (
        Pie(init_opts=opts.InitOpts(width='640px',height='205px'))
        .add('Overall', [list(z) for z in zip(t_attrs, type_nums)],center=["25%","50%"])
        .add('Risk',[list(z) for z in zip(t_attrs,risk_nums)],center=['75%','50%'])
        .set_global_opts(title_opts=opts.TitleOpts(title="Corporate Risk Management"),legend_opts=opts.LegendOpts(pos_right="0%"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}",is_show=False))
    )
    type_pie.render("./htmls/type_pie.html")

    # 统计各类别的风险特性
    industries = unique_data['INDUSTRYPHY'].copy().drop_duplicates().sort_values().tolist()
    ind_sta = []
    for i in range(len(industries)):
        ind_data = unique_data[unique_data['INDUSTRYPHY']==industries[i]]
        ind_nums = []
        for j in range(len(type_attrs)):
            ind_slice = ind_data[ind_data['CaseType']==type_attrs[j]]
            ind_nums.append(len(ind_slice))
        ind_ratios = []
        for j in range(len(ind_nums)):
            ind_ratios.append(ind_nums[j]/sum(ind_nums))
        ind_sta.append(ind_ratios)
    ind_sta = np.array(ind_sta)

    #实现不同风险查询标准的Top
    ind_dataset = pd.DataFrame(ind_sta,columns=['R0','R1','R2','R3','R4'])
    index = [i for i in range(len(ind_sta))]
    ind_dataset['id'] = index
    ind_dataset0 = ind_dataset.sort_values(by='R4',ascending=True)
    ind_dataset1 = ind_dataset.sort_values(by='R0',ascending=False)
    ind_dataset2 = ind_dataset.sort_values(by='R1',ascending=False)
    ind_dataset3 = ind_dataset.sort_values(by='R2',ascending=False)
    ind_dataset4 = ind_dataset.sort_values(by='R3',ascending=False)

    #统计企业类型对应的风险概率
    entity = unique_data['ENTTYPE'].copy().drop_duplicates().sort_values().tolist()
    ent_sta = []
    for i in range(len(entity)):
        ent_data = unique_data[unique_data['ENTTYPE']==entity[i]]
        ent_nums = []
        for j in range(len(type_attrs)):
            ent_slice = ent_data[ent_data['CaseType']==type_attrs[j]]
            ent_nums.append(len(ent_slice))
        ent_ratios = []
        for j in range(len(type_attrs)):
            ent_ratios.append(ent_nums[j]/sum(ent_nums))
        ent_sta.append(ent_ratios)
    ent_sta = np.array(ent_sta)
    ent_dataset = pd.DataFrame(ent_sta,columns=['R0','R1','R2','R3','R4'])
    index1 = [i for i in range(len(ent_sta))]
    ent_dataset['id'] = index1
    ent_dataset0 = ent_dataset.sort_values(by='R4',ascending=True)
    ent_dataset1 = ent_dataset.sort_values(by='R0',ascending=False)
    ent_dataset2 = ent_dataset.sort_values(by='R1',ascending=False)
    ent_dataset3 = ent_dataset.sort_values(by='R2',ascending=False)
    ent_dataset4 = ent_dataset.sort_values(by='R3',ascending=False)

    draw_bari(ind_dataset0,'industry_bar0')
    draw_bari(ind_dataset1,'industry_bar1')
    draw_bari(ind_dataset2,'industry_bar2')
    draw_bari(ind_dataset3,'industry_bar3')
    draw_bari(ind_dataset4,'industry_bar4')
    draw_bari(ind_dataset,'industry_bar')
    draw_bare(ent_dataset0,'enterprise_bar0')
    draw_bare(ent_dataset1,'enterprise_bar1')
    draw_bare(ent_dataset2,'enterprise_bar2')
    draw_bare(ent_dataset3,'enterprise_bar3')
    draw_bare(ent_dataset4,'enterprise_bar4')
    draw_bare(ent_dataset,'enterprise_bar')