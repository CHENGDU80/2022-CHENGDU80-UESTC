from pyecharts import options as opts
from pyecharts.charts import Liquid
from pyecharts.globals import SymbolType
from Config import *

# LOGO动态效果
def logo():
    liquid = Liquid(init_opts=opts.InitOpts(width='90px',height='90px'))
    liquid.add("lq", [0.3, 0.7], is_outline_show=False, shape=SymbolType.DIAMOND, color=[255,255,255])
    liquid.set_global_opts(title_opts=opts.TitleOpts(title=""))
    liquid.render("./main/logo.html")


if __name__ == '__main__':
    logo()
