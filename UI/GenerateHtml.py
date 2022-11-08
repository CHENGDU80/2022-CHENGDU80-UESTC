import pandas as pd
import numpy as np
import json
from pyecharts.charts import Bar, Bar3D, Pie, Line, Timeline, Tree, Radar, Graph
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
from Config import *


# 简单柱状图渲染
def drawSimpleBar(x, y, width, height, path, file_name, file_id):
    bar = Bar(init_opts=opts.InitOpts(width=width,height=height))
    bar.add_xaxis(x)
    bar.add_yaxis('Cluster Type', y, color='#518D79')
    bar.set_global_opts(title_opts=opts.TitleOpts(title="Title"),
                        datazoom_opts=opts.DataZoomOpts(is_show=True),
                        legend_opts=opts.LegendOpts(pos_right="0%"))
    bar.set_series_opts(label_opts=opts.LabelOpts(position='top'))
    bar.render(path+file_name+str(file_id)+'.html')


# 复杂柱状图渲染
def drawComplexBar(x, y, width, height, path, file_name, file_id):
    bar = Bar(init_opts=opts.InitOpts(width=width,height=height))
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
    bar.render(path+file_name+str(file_id)+'.html')


# 3D柱状图渲染
def draw3DBar(x, y, data, width, height, path, file_name, file_id):
    bar = Bar3D(init_opts=opts.InitOpts(width=width,height=height))
    bar.add(series_name="", data=data, xaxis3d_opts=opts.Axis3DOpts(type_="category",data=x),
            yaxis3d_opts=opts.Axis3DOpts(type_="category",data=y), zaxis3d_opts=opts.Axis3DOpts(type_="value"),)
    bar.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=400,
                                                          range_color=["#313695", "#4575b4", "#74add1", "#abd9e9",
                                                                       "#e0f3f8", "#ffffbf", "#fee090", "#fdae61",
                                                                       "#f46d43", "#d73027", "#a50026", ], ),
                        title_opts=opts.TitleOpts(title="Feature Importance"),
                        legend_opts=opts.LegendOpts(pos_right="0%"))
    # bar.set_series_opts(label_opts=opts.LabelOpts(position='top'))
    bar.render(path+file_name+str(file_id)+'.html')


# 复杂饼状图渲染
def drawComplexPie(x, y, width, height, path, file_name, file_id):
    pie = Pie(init_opts=opts.InitOpts(width=width,height=height))
    pie.add("",[list(Z) for Z in zip(x,y)])
    pie.set_global_opts(title_opts=opts.TitleOpts(title="Title"),
                        legend_opts=opts.LegendOpts(pos_right="0%",orient='vertical'))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}", is_show=False))
    pie.render(path+file_name+str(file_id)+'.html')


# 简单饼状图渲染
def drawSimplePie(x, y, width, height, path, file_name, file_id):
    pie = Pie(init_opts=opts.InitOpts(width=width,height=height))
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
    pie.render(path+file_name+str(file_id)+'.html')


# 复杂线状图渲染
def drawSimpleLine(x, y, width, height, path, file_name, file_id):
    line = Line(init_opts=opts.InitOpts(width=width,height=height))
    line.add_xaxis(x)
    line.add_yaxis('Yaix', y, color='#518D79')
    line.set_global_opts(title_opts=opts.TitleOpts(title="Title"),
                         datazoom_opts=opts.DataZoomOpts(is_show=True),
                         legend_opts=opts.LegendOpts(pos_right="0%"))
    line.set_series_opts(label_opts=opts.LabelOpts(position='top'))
    line.render(path+file_name+str(file_id)+'.html')


# 时间树状图渲染
def drawTimeTree(x, y, width, height, path, file_name, file_id):
    subtree_name = ['connections', 'repayment willingness', 'repayment ability', 'consumption', 'personal information']
    tl = Timeline(init_opts=opts.InitOpts(width=width, height=height))
    for i in range(0, 5):
        with open('./data/TargetTree'+str(i)+'.json', "r", encoding="utf-8") as f:
            j = json.load(f)
        tree=Tree(init_opts=opts.InitOpts(width=width, height=height))
        tree.add("", [j], collapse_interval=2)
        tree.set_global_opts(title_opts=opts.TitleOpts(title=y),
                             legend_opts=opts.LegendOpts(pos_right="0%"))
        tree.set_series_opts(label_opts=opts.LabelOpts(position='top'))
        tl.add(tree, subtree_name[i])
    tl.render(path+file_name+str(file_id)+'.html')


# 环形树状图渲染
def drawCircleTree(x, y, width, height, path, file_name, file_id):
    with open("./data/TargetTree0.json","r",encoding="utf-8") as f:
        j=json.load(f)
    tree = Tree(init_opts=opts.InitOpts(width=width,height=height))
    tree.add("", [j], collapse_interval=2, layout="radial")
    tree.set_global_opts(title_opts=opts.TitleOpts(title="Title"),
                         legend_opts=opts.LegendOpts(pos_right="0%"))
    tree.set_series_opts(label_opts=opts.LabelOpts(position='top'))
    tree.render(path+file_name+str(file_id)+'.html')


# 简单树状图渲染
def drawSimpleTree(x, y, width, height, path, file_name, file_id):
    with open(x,"r",encoding="utf-8") as f:
        j=json.load(f)
    tree = Tree(init_opts=opts.InitOpts(width=width,height=height))
    tree.add("", [j], collapse_interval=2)
    tree.set_global_opts(title_opts=opts.TitleOpts(title=y),
                         legend_opts=opts.LegendOpts(pos_right="0%"))
    tree.set_series_opts(label_opts=opts.LabelOpts(position='top'))
    tree.render(path+file_name+str(file_id)+'.html')


# 简单雷达图渲染
def drawSimpleRadar(x, y, width, height, path, file_name, file_id):
    x = [[88, 64, 37, 52, 94]]
    radar = Radar(init_opts=opts.InitOpts(width=width,height=height))
    radar.add_schema(schema=[
                opts.RadarIndicatorItem(name="A_1", max_=100),
                opts.RadarIndicatorItem(name="A_2", max_=100),
                opts.RadarIndicatorItem(name="A_3", max_=100),
                opts.RadarIndicatorItem(name="A_4", max_=100),
                opts.RadarIndicatorItem(name="A_5", max_=100)])
    radar.add("Credit Rating", x)
    radar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    radar.set_global_opts(legend_opts=opts.LegendOpts(pos_right="0%",selected_mode="single"),
                          title_opts=opts.TitleOpts(title="User Credit"),)
    radar.render(path+file_name+str(file_id)+'.html')


# 简单图谱渲染
def drawSimpleGraph(x, y, width, height, path, file_name, file_id):
    with open(x,"r",encoding="utf-8") as f:
        nodes = json.load(f)
    links = []
    count = 0
    m = [i for i in range(5, 25)]
    np.random.shuffle(m)
    for i in range(5):
        links.append({"source": nodes[i].get("name"),"target": nodes[25].get("name")})
        for j in range(4):
            links.append({"source": nodes[i].get("name"), "target": nodes[m[count]].get("name")})
            count = count + 1
    graph = Graph(init_opts=opts.InitOpts(width=width,height=height))
    graph.add("",nodes,links,repulsion=8000)
    graph.set_global_opts(title_opts=opts.TitleOpts(title="User Feature Graph"))
    graph.render(path+file_name+str(file_id)+'.html')


# 模型结构渲染
def drawStructure(x, y, width, height, path, file_name, file_id):
    submodel_name = ['Data cleaning', 'Key feature extract', 'Integrated learning', 'Anomaly detection']
    tl = Timeline(init_opts=opts.InitOpts(width=width, height=height))
    for i in range(len(submodel_name)):
        with open('./data/Structure'+str(i)+'.json', "r", encoding="utf-8") as f:
            nodes = json.load(f)
        links = []
        nodes_main = [{"name": "Input", "symbolSize": 70}, {"name": "Output", "symbolSize": 70}]
        for j in range(len(nodes)):
            if i == 1:
                with open('./data/StructureLink'+str(i)+'.json',"r",encoding="utf-8") as f:
                    links = json.load(f)
            else:
                links.append({"source": nodes[j].get("name"), "target": nodes_main[0].get("name")})
                links.append({"source": nodes[j].get("name"), "target": nodes_main[1].get("name")})
        nodes.append(nodes_main[1])
        nodes.append(nodes_main[0])
        graph=Graph(init_opts=opts.InitOpts(width=width,height=height))
        graph.add("",nodes,links,repulsion=8000)
        graph.set_global_opts(title_opts=opts.TitleOpts(title=submodel_name[i]))
        tl.add(graph, submodel_name[i])
    tl.render(path+file_name+str(file_id)+'.html')


# 生成主页元素
def generateMain():
    drawSimpleGraph("./data/Graph0.json", 0, MAIN_WIDTH, MAIN_HEIGHT, MAIN_PATH, 'Main_Graph_Simple_',0)
    drawTimeTree(0, "Target Tree", MAIN_WIDTH, MAIN_HEIGHT, MAIN_PATH, 'Main_Tree_Time_',0)
    draw3DBar(data['type'].drop_duplicates().tolist(), data['attribute'].drop_duplicates().tolist(),data.values.tolist(),
              MAIN_WIDTH, MAIN_HEIGHT, MAIN_PATH, 'Main_Bar_3D_', 0)
    drawSimpleRadar(0, 0, MAIN_WIDTH, MAIN_HEIGHT, MAIN_PATH, 'Main_Radar_Simple_', 0)
    drawStructure(0, 0, MAIN_WIDTH_, MAIN_HEIGHT_, MAIN_PATH, 'Main_Structure_', 0)


# 生成用户界面元素
def generateUser():
    drawSimpleRadar(0, 0, USER_WIDTH, USER_HEIGHT, USER_PATH, 'User_Radar_Simple_', 0)
    drawSimpleTree("./data/UserTargetTree0.json", "User Feature Rate", USER_WIDTH_, USER_HEIGHT_, USER_PATH, 'User_Tree_Simple_', 0)


# 生成模型界面元素
def generateModel():
    drawStructure(0, 0, MODEL_WIDTH, MODEL_HEIGHT, MODEL_PATH, 'Model_Structure_', 0)


# 生成分析界面元素
def generateAnalysis():
    drawSimpleGraph("./data/Graph0.json", 0, ANALYSIS_WIDTH, ANALYSIS_HEIGHT, ANALYSIS_PATH, 'Analysis_Graph_Simple_',0)
    drawTimeTree(0, "Target Tree", ANALYSIS_WIDTH, ANALYSIS_HEIGHT, ANALYSIS_PATH, 'Analysis_Tree_Time_',0)
    draw3DBar(data['type'].drop_duplicates().tolist(), data['attribute'].drop_duplicates().tolist(),data.values.tolist(),
              ANALYSIS_WIDTH, ANALYSIS_HEIGHT, ANALYSIS_PATH, 'Analysis_Bar_3D_', 0)
    drawSimpleRadar(0, 0, ANALYSIS_WIDTH, ANALYSIS_HEIGHT, ANALYSIS_PATH, 'Analysis_Radar_Simple_', 0)


if __name__ == '__main__':
    data = pd.read_csv('./data/importance_.csv')
    data.sort_index(axis=0, ascending=False, inplace=True)

    generateMain()
    generateUser()
    generateModel()
    generateAnalysis()

    # 簇的聚类情况
    cluster_data = np.load('./data/ids.npy')
    cluster_data_type = [np.sum(cluster_data == i) for i in range(31)]
    drawSimpleBar([i for i in range(31)], cluster_data_type, WIDTH, HEIGHT, PATH, 'Cluster_Bar_', 0)
    drawComplexBar([i for i in range(31)], cluster_data_type, WIDTH, HEIGHT, PATH,  'Cluster_Pie_', 0)

    # # 生成柱状图
    # drawSimpleBar(data['attribute'].tolist(), data['importance'].tolist(), 'Bar_Simple_', 0)
    # drawComplexBar(data['attribute'].iloc[0:2].tolist(), data['importance'].iloc[0:11].tolist(), 'Bar_Complex_', 0)
    # draw3DBar(data['type'].drop_duplicates().tolist(), data['attribute'].drop_duplicates().tolist(),
    #           data.values.tolist(), 'Bar_3D_', 0)
    #
    # # 生成饼状图
    # drawComplexPie(data['attribute'].tolist(), data['importance'].tolist(), 'Pie_Complex_', 0)
    # drawSimplePie(data['attribute'].iloc[0:2].tolist(), data['importance'].iloc[0:2].tolist(), 'Pie_Simple_', 0)
    #
    # # 生成折线图
    # drawSimpleLine(data['attribute'].tolist(), data['importance'].tolist(), 'Line_Simple_', 0)
    # drawTimeLine(data['attribute'].tolist(), data['importance'].tolist(), 'Line_Time_', 0)
    #
    # # 生成树状图
    # drawCircleTree(data['attribute'].tolist(), data['importance'].tolist(), 'Tree_Circle_', 0)
    # drawSimpleTree(data['attribute'].tolist(), data['importance'].tolist(), 'Tree_Simple_', 0)
    #
    # # 生成雷达图
    # drawSimpleRadar(data['attribute'].tolist(), data['importance'].tolist(), 'Radar_Simple_', 0)