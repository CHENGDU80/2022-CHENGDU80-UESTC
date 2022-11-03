import pandas as pd
import numpy as np
import json
from pyecharts.charts import Bar, Pie, Line, Timeline, Tree
from pyecharts import options as opts
from pyecharts.faker import Faker
from Config import *


# 简单柱状图渲染
def drawSimpleBar(x, y, file_name, file_id):
    bar = Bar(init_opts=opts.InitOpts(width=WIDTH,height=HEIGHT))
    bar.add_xaxis(x)
    bar.add_yaxis('Yaix', y, color='#518D79')
    bar.set_global_opts(title_opts=opts.TitleOpts(title="Title"),
                        datazoom_opts=opts.DataZoomOpts(is_show=True),
                        legend_opts=opts.LegendOpts(pos_right="0%"))
    bar.set_series_opts(label_opts=opts.LabelOpts(position='top'))
    bar.render(PATH+file_name+str(file_id)+'.html')


# 复杂柱状图渲染
def drawComplexBar(x, y, file_name, file_id):
    bar = Bar(init_opts=opts.InitOpts(width=WIDTH,height=HEIGHT))
    bar.add_xaxis(x)
    bar.add_yaxis('Yaix0', y[0:2], stack='stack')
    bar.add_yaxis('Yaix1', y[2:4], stack='stack')
    bar.add_yaxis('Yaix2', y[4:6], stack='stack')
    bar.add_yaxis('Yaix3', y[6:8], stack='stack')
    bar.add_yaxis('Yaix4', y[8:10], stack='stack')
    bar.set_global_opts(title_opts=opts.TitleOpts(title="Title"),
                        datazoom_opts=opts.DataZoomOpts(is_show=True),
                        legend_opts=opts.LegendOpts(pos_right="0%"))
    bar.set_series_opts(label_opts=opts.LabelOpts(position='top'))
    bar.render(PATH+file_name+str(file_id)+'.html')


# 复杂饼状图渲染
def drawComplexPie(x, y, file_name, file_id):
    pie = Pie(init_opts=opts.InitOpts(width=WIDTH,height=HEIGHT))
    pie.add("",[list(Z) for Z in zip(x,y)])
    pie.set_global_opts(title_opts=opts.TitleOpts(title="Title"),
                        legend_opts=opts.LegendOpts(pos_right="0%",orient='vertical'))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}", is_show=False))
    pie.render(PATH+file_name+str(file_id)+'.html')


# 简单饼状图渲染
def drawSimplePie(x, y, file_name, file_id):
    pie = Pie(init_opts=opts.InitOpts(width=WIDTH,height=HEIGHT))
    pie.add("",[list(Z) for Z in zip(x,y)], radius=["30%","65%"], center=['50%','50%'],
            label_opts=opts.LabelOpts(position="outside", formatter="{a|Title}{abg|}\n{hr|}\n {b|{b}: }  {per|{c}%}  ",
                                      background_color="#eee", border_color="#aaa", border_width=1, border_radius=4,
                                      rich={"a": {"color": "#999","lineHeight": 22,"align": "center"},
                                            "abg": {"backgroundColor": "#e3e3e3","width": "100%","align": "right",
                                                    "height": 22,"borderRadius": [4,4,0,0]},
                                            "hr": {"borderColor": "#aaa","width": "100%","borderWidth": 0.5,
                                                   "height": 0,},
                                            "b": {"fontSize": 16,"lineHeight": 33},
                                            "per": {"color": "#eee","backgroundColor": "#334455","padding": [2,4],
                                                    "borderRadius": 2}}))
    pie.set_global_opts(title_opts=opts.TitleOpts(title="Title"),
                        legend_opts=opts.LegendOpts(pos_right="0%",orient='vertical'))
    pie.render(PATH+file_name+str(file_id)+'.html')

# 复杂饼状图渲染
def drawSimpleLine(x, y, file_name, file_id):
    line = Line(init_opts=opts.InitOpts(width=WIDTH,height=HEIGHT))
    line.add_xaxis(x)
    line.add_yaxis('Yaix', y, color='#518D79')
    line.set_global_opts(title_opts=opts.TitleOpts(title="Title"),
                         datazoom_opts=opts.DataZoomOpts(is_show=True),
                         legend_opts=opts.LegendOpts(pos_right="0%"))
    line.set_series_opts(label_opts=opts.LabelOpts(position='top'))
    line.render(PATH+file_name+str(file_id)+'.html')


# 时间线饼图渲染
def drawTimeLine(x, y, file_name, file_id):
    tl = Timeline(init_opts=opts.InitOpts(width=WIDTH, height=HEIGHT))
    for i in range(2015, 2020):
        pie = Pie(init_opts=opts.InitOpts(width=WIDTH, height=HEIGHT))
        pie.add("商家A", [list(z) for z in zip(x, y)], rosetype="radius", radius=["30%", "55%"])
        pie.set_global_opts(title_opts=opts.TitleOpts(title="Title"),
                            datazoom_opts=opts.DataZoomOpts(is_show=True),
                            legend_opts=opts.LegendOpts(pos_right="0%"))
        tl.add(pie, "{}年".format(i))
    tl.render(PATH+file_name+str(file_id)+'.html')


# 树状图渲染
def drawTree(x, y, file_name, file_id):
    with open("flare.json", "r", encoding="utf-8") as f:
        j = json.load(f)
    tree = Tree(init_opts=opts.InitOpts(width=WIDTH,height=HEIGHT))
    tree.add("", [j], collapse_interval=2, layout="radial")
    tree.set_global_opts(title_opts=opts.TitleOpts(title="Title"),
                         datazoom_opts=opts.DataZoomOpts(is_show=True),
                         legend_opts=opts.LegendOpts(pos_right="0%"))
    tree.set_series_opts(label_opts=opts.LabelOpts(position='top'))
    tree.render(PATH+file_name+str(file_id)+'.html')


if __name__ == '__main__':
    data = pd.read_csv('importance.csv')
    data.sort_index(axis=0, ascending= False, inplace=True)
    drawSimpleBar(data['attribute'].tolist(), data['importance'].tolist(), 'SimpleBar', 0)
    drawComplexBar(data['attribute'].iloc[0:2].tolist(), data['importance'].iloc[0:11].tolist(), 'ComplexBar', 0)
    drawComplexPie(data['attribute'].tolist(), data['importance'].tolist(), 'ComplexPie', 0)
    drawSimplePie(data['attribute'].iloc[0:2].tolist(), data['importance'].iloc[0:2].tolist(), 'SimplePie', 0)
    drawSimpleLine(data['attribute'].tolist(), data['importance'].tolist(), 'SimpleLine', 0)
    drawTimeLine(data['attribute'].tolist(), data['importance'].tolist(), 'TimeLine', 0)