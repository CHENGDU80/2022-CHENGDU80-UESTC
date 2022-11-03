import pandas as pd
import numpy as np
from pyecharts.charts import Bar, Pie
from pyecharts import options as opts
from Config import *


# 柱状图渲染
def drawBar(x, y, file_name, file_id):
    bar = Bar(init_opts=opts.InitOpts(width=WIDTH,height=HEIGHT))
    bar.add_xaxis(x)
    bar.add_yaxis('Yaix', y, color='#518D79')
    bar.set_global_opts(title_opts=opts.TitleOpts(title="Title"),
                        datazoom_opts=opts.DataZoomOpts(is_show=True),
                        legend_opts=opts.LegendOpts(pos_right="0%"))
    bar.set_series_opts(label_opts=opts.LabelOpts(position='top'))
    bar.render(PATH+file_name+str(file_id)+'.html')


# 饼状图渲染
def drawPie(x, y, file_name, file_id):
    pie = Pie(init_opts=opts.InitOpts(width=WIDTH,height=HEIGHT))
    pie.add("",[list(Z) for Z in zip(attrs,dataset)])
    pie.set_global_opts(title_opts=opts.TitleOpts(title="Title"),
                        legend_opts=opts.LegendOpts(pos_right="0%",orient='vertical'))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}", is_show=False))
    pie.render(PATH+file_name+str(file_id)+'.html')


if __name__ == '__main__':
    data = pd.read_csv('importance.csv')
    # print(data.head())
    data.sort_index(axis = 0, ascending= False, inplace=True)
    drawBar(data['attribute'].tolist(), data['importance'].tolist(), 'Bar', 0)
    drawPie(data, data, 'Pie', 0)