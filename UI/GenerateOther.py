from pyecharts import options as opts
from pyecharts.charts import Liquid, MapGlobe
from pyecharts.globals import SymbolType
from pyecharts.faker import POPULATION
from Config import *


data = [x for _, x in POPULATION[1:]]
low, high = min(data), max(data)

# 生成地球
c = (
    MapGlobe()
    .add_schema()
    .add(
        maptype="world",
        series_name="World Population",
        data_pair=POPULATION[1:],
        is_map_symbol_show=False,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            min_=low,
            max_=high,
            range_text=["max", "min"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"],
        )
    )
    .render("map_globe_base.html")
)

# LOGO动态效果
def logo():
    liquid = Liquid(init_opts=opts.InitOpts(width='90px',height='90px'))
    liquid.add("lq", [0.3, 0.7], is_outline_show=False, shape=SymbolType.DIAMOND, color=[255,255,255])
    liquid.set_global_opts(title_opts=opts.TitleOpts(title=""))
    liquid.render("./htmls_main/logo.html")


if __name__ == '__main__':
    logo()
