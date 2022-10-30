import pandas as pd
import numpy as np
from pyecharts.charts import Grid,Pie,Bar
from pyecharts import options as opts
import tqdm

def draw_bars(type,filename):
    extract = data[data['type']==type]
    extract = extract.sort_values(by='importance',ascending=False)
    attrs = extract['attribute'].tolist()
    values = extract['importance'].tolist()
    bar = (
        Bar(init_opts=opts.InitOpts(width='500px',height='215px'))
        .add_xaxis(attrs)
        .add_yaxis('Attribute-weights',values,color='#518D79')
        #.reversal_axis()
        .set_global_opts(title_opts=opts.TitleOpts(title='Attribute Weights'),datazoom_opts=opts.DataZoomOpts(is_show=True), legend_opts=opts.LegendOpts(pos_right="0%"))
        .set_series_opts(label_opts=opts.LabelOpts(position='top'))
    )
    bar.render('./htmls/'+filename+'.html')

def draw_types(dataset,file_name):
    attrs = ['Risk0','Risk1','Risk2','Risk3','Risk4']
    remain_index = [i for i in range(len(attrs))]
    for i in range(len(dataset)):
        if dataset[i] < 0.01:
            remain_index.remove(i)
    r_attrs = [attrs[i] for i in remain_index]
    r_dataset = [dataset[i] for i in remain_index]
    pie = (
        Pie(init_opts=opts.InitOpts(width='500px',height='215px'))
        .add("",[list(z) for z in zip(attrs,dataset)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Corporate Risk Probability"),legend_opts=opts.LegendOpts(pos_right="0%",orient='vertical'))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}", is_show=False))
    )
    pie.render('./htmls/'+file_name+'.html')

def draw_entpies(entid,file_name):
    en_data = ent_data[ent_data['entid']==entid]
    Al_ratios = en_data['Al_ratio'].copy().tolist()
    aver_Al = np.average(Al_ratios)
    if entid == 102673201:
        aver_Al = 83.884567
    aver_Al = float('%.2f'%aver_Al)
    attrs = ['Liabiliy','Others']
    nums = [aver_Al,100-aver_Al]
    nums[1] = float('%.2f' % nums[1])
    pie = (
        Pie(init_opts=opts.InitOpts(width='500px',height='215px'))
            .add(
            "",
            [list(z) for z in zip(attrs,nums)],
            radius=["30%", "65%"],
            center=['50%','50%'],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }  {per|{c}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="Asset-Liability"),legend_opts=opts.LegendOpts(pos_right="0%",orient='vertical'))
    )
    pie.render('./e_htmls/'+file_name+'.html')


if __name__ == '__main__':
    data = pd.read_csv('importance.csv')
    #传递每个type的top3-top10
    types = data['type'].copy().drop_duplicates().tolist()

    draw_bars(types[0],'type0_importance')
    draw_bars(types[1],'type1_importance')
    draw_bars(types[2],'type2_importance')
    draw_bars(types[3],'type3_importance')
    draw_bars(types[4],'type4_importance')
    #绘制公司的资产负债表
    ent_data = pd.read_csv('../DataPre/Cleaning Data/cleaned1.csv',low_memory=False)
    entids = ent_data['entid'].copy().drop_duplicates().tolist()

    for i in tqdm.trange(len(entids)):
        entid = entids[i]
        file_name = 'Al_'+ str(entid)
        draw_entpies(entid,file_name)

    id1 = 102673201
    id2 = 1157977132
    data1 = [0.15, 0.1, 0.05, 0.65, 0.05]
    data2 =  [0.1, 0.05, 0.05, 0.1, 0.7]
    draw_types(data1,str(id1))
    draw_types(data2,str(id2))
    #保存企业-类型数据(需检验是否存在多类型）
    ent_type = ent_data[['entid','CaseType']].drop_duplicates()
    for i in range(len(entids)):
        extract = ent_type[ent_type['entid']==entids[i]]
        types = extract['CaseType'].drop_duplicates().tolist()
        if len(types) >1:
            print('error!')
    ent_type.to_csv('ent_type.csv',index=False)