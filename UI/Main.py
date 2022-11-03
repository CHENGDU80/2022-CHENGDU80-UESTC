import sys
import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

from MainWindow import Ui_MainWindow
from Config import *

data = pd.read_csv('ent_type.csv')


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # 设定窗口
        super().__init__(parent)
        self.setupUi(self)
        self.start_x = None
        self.start_y = None
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框

        # 设定窗口移动尺寸变化变量
        self.evn = 0

        # 设置页面切换响应事件
        self.IntroList.itemClicked.connect(self.displayIntroPage)
        self.DetailsList.itemClicked.connect(self.displayDetailsPage)
        self.SearchBarButton.clicked.connect(self.displaySearchPage)

        # 页面设定
        self.mainPageStart()
        self.searchPageStart()
        self.barPageStart()
        self.piePageStart()
        self.graphPageStart()

    # 首页-函数设定
    def mainPageStart(self,):
        # 设置UI阴影效果
        self.effect_shadow_style(self.FirstFrame)
        self.effect_shadow_style2(self.SecondFrame)
        self.effect_shadow_style3(self.ThirdFrame)
        self.effect_shadow_style4(self.FourthFrame)

        # 设置首页选择列表的跳转函数
        self.MainPageChooseList.itemClicked.connect(self.mainPageList)

        # 设置按钮展示选择
        self.FirstFrameButton.clicked.connect(self.mainPageFirstButton)
        self.SecondFrameButton.clicked.connect(self.mainPageSecondButton)
        self.ThirdFrameButton.clicked.connect(self.mainPageThirdButton)
        self.FourthFrameButton.clicked.connect(self.mainPageFourthButton)

    # 首页-ListWeb元素选择跳转
    def mainPageList(self):
        text = self.MainPageChooseList.currentItem().text()
        if text == 'Last 120 second':
            self.MainWeb.load(QUrl.fromLocalFile(ABS_PATH+MAIN_PATH+'Bar_Complex_0.html'))
        elif text == 'Last 30 minute':
            self.MainWeb.load(QUrl.fromLocalFile(ABS_PATH+MAIN_PATH+'Bar_Simple_0.html'))
        elif text == 'Last 24 hours':
            self.MainWeb.load(QUrl.fromLocalFile(ABS_PATH+MAIN_PATH+'Pie_Complex_0.html'))
        elif text == 'Last 5 days':
            self.MainWeb.load(QUrl.fromLocalFile(ABS_PATH+MAIN_PATH+'Pie_Simple_0.html'))

    # 首页-Button元素选择跳转
    def mainPageFirstButton(self):
        self.MainWeb.load(QUrl.fromLocalFile(ABS_PATH+MAIN_PATH+'Line_Complex_0.html'))
    def mainPageSecondButton(self):
        self.MainWeb.load(QUrl.fromLocalFile(ABS_PATH+MAIN_PATH+'Line_Simple_0.html'))
    def mainPageThirdButton(self):
        self.MainWeb.load(QUrl.fromLocalFile(ABS_PATH+MAIN_PATH+'Tree_Circle_0.html'))
    def mainPageFourthButton(self):
        self.MainWeb.load(QUrl.fromLocalFile(ABS_PATH+MAIN_PATH+'Tree_Simple_0.html'))

    # searchPage页-函数设定
    def searchPageStart(self):
        self.SearchPageChooseList.itemClicked.connect(self.searchPageList)

    # searchPage页-ListWeb元素选择跳转
    def searchPageList(self):
        text=self.SearchPageChooseList.currentItem().text()
        if text == 'show the result':
            self.SearchWeb.load(QUrl.fromLocalFile(ABS_PATH+HTML_PATH+'Bar_Simple_0.html'))

    # barPage页-函数设定
    def barPageStart(self):
        # 设置piePage页选择列表的跳转函数
        self.BarPageChooseList.itemClicked.connect(self.barPageList)

    # barPage页-ListWeb元素选择跳转
    def barPageList(self):
        text = self.BarPageChooseList.currentItem().text()
        if text == 'Bar 1':
            self.BarWeb.load(QUrl.fromLocalFile(ABS_PATH+HTML_PATH+'Bar_Simple_0.html'))
        elif text == 'Bar 2':
            self.BarWeb.load(QUrl.fromLocalFile(ABS_PATH+HTML_PATH+'Bar_Simple_0.html'))
        elif text == 'Bar 3':
            self.BarWeb.load(QUrl.fromLocalFile(ABS_PATH+HTML_PATH+'Bar_Simple_0.html'))
        elif text == 'Bar 4':
            self.BarWeb.load(QUrl.fromLocalFile(ABS_PATH+HTML_PATH+'Bar_Simple_0.html'))

    # piePage页-函数设定
    def piePageStart(self):
        # 设置piePage页选择列表的跳转函数
        self.PiePageChooseList.itemClicked.connect(self.piePageList)

    # piePage页-ListWeb元素选择跳转
    def piePageList(self):
        text = self.PiePageChooseList.currentItem().text()
        if text == 'Pie 1':
            self.PieWeb.load(QUrl.fromLocalFile(ABS_PATH+HTML_PATH+'Pie_Simple_0.html'))
        elif text == 'Pie 2':
            self.PieWeb.load(QUrl.fromLocalFile(ABS_PATH+HTML_PATH+'Pie_Simple_0.html'))
        elif text == 'Pie 3':
            self.PieWeb.load(QUrl.fromLocalFile(ABS_PATH+HTML_PATH+'Pie_Simple_0.html'))
        elif text == 'Pie 4':
            self.PieWeb.load(QUrl.fromLocalFile(ABS_PATH+HTML_PATH+'Pie_Simple_0.html'))

    # graphPage页-函数设定
    def graphPageStart(self):
        # 设置piePage页选择列表的跳转函数
        self.GraphPageChooseList.itemClicked.connect(self.graphPageList)

    # graphPage页-ListWeb元素选择跳转
    def graphPageList(self):
        text = self.GraphPageChooseList.currentItem().text()
        if text == 'Graph 1':
            self.GraphWeb.load(QUrl.fromLocalFile(ABS_PATH+HTML_PATH+'Tree_Simple_0.html'))

    # 窗口尺寸调整-按压鼠标获取窗体坐标函数
    def mousePressEvent(self, event):
        if self.childAt(event.x(), event.y()) in [self.RightBottomWindowEdge]:
            self.evn = 1
            self.mouse_x = event.globalX()  # 获取鼠标当前的坐标
            self.mouse_y = event.globalY()
            self.origin_x = self.x()  # 获取窗体当前坐标
            self.origin_y = self.y()
        elif self.childAt(event.x(), event.y()) in [self.RightWindowEdge]:
            self.evn = 2
            self.mouse_x = event.globalX()  # 获取鼠标当前的坐标
            self.mouse_y = event.globalY()
            self.origin_x = self.x()  # 获取窗体当前坐标
            self.origin_y = self.y()
        elif self.childAt(event.x(), event.y()) in [self.BottomWindowEdge]:
            self.evn = 3
            self.mouse_x = event.globalX()  # 获取鼠标当前的坐标
            self.mouse_y = event.globalY()
            self.origin_x = self.x()  # 获取窗体当前坐标
            self.origin_y = self.y()
        else:
            self.evn = 0
            super(MyMainForm, self).mousePressEvent(event)
            self.start_x = event.x()
            self.start_y = event.y()

    # 窗口尺寸调整-松开鼠标重置窗口位置信息
    def mouseReleaseEvent(self, event):
        self.origin_x = None
        self.origin_y = None
        self.start_x = None
        self.start_y = None

    # 窗口尺寸调整-移动鼠标调整窗口位置信息
    def mouseMoveEvent(self, event):
        #
        if self.evn == 0:
            super(MyMainForm, self).mouseMoveEvent(event)
            dis_x = event.x() - self.start_x
            dis_y = event.y() - self.start_y
            self.move(self.x() + dis_x, self.y() + dis_y)
        elif self.evn == 1:  # 计算鼠标移动的x，y位移
            try:
                if event.x() < 814:
                    x = 814
                else:
                    x = event.x()
                if event.y() < 272:
                    y = 272
                else:
                    y = event.y()
                self.setGeometry(self.origin_x, self.origin_y, x, y)
                self.RightBottomWindowEdge.setGeometry(0, 0, x, y)
            except BaseException as f:
                pass
        elif self.evn == 2:  # 计算鼠标移动的x，y位移
            try:
                # 移动窗体
                if event.x() < 814:
                    x = 814
                else:
                    x = event.x()
                self.setGeometry(self.origin_x, self.origin_y, x, self.height())
                self.RightWindowEdge.setGeometry(0, 0, x, self.RightWindowEdge.height())
            except BaseException as f:
                pass
        elif self.evn == 3:  # 计算鼠标移动的x，y位移
            try:
                # 移动窗体
                if event.y() < 272:
                    y = 272
                else:
                    y = event.y()
                self.setGeometry(self.origin_x, self.origin_y, self.width(), y)
                self.BottomWindowEdge.setGeometry(0, 0, self.BottomWindowEdge.width(), y)
            except BaseException as f:
                pass

    # 设置色块阴影颜色效果
    def effect_shadow_style(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 8)  # 偏移
        effect_shadow.setBlurRadius(48)  # 阴影半径
        effect_shadow.setColor(QColor(162, 129, 247))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)
    def effect_shadow_style2(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 8)  # 偏移
        effect_shadow.setBlurRadius(48)  # 阴影半径
        effect_shadow.setColor(QColor(253, 139, 133))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)
    def effect_shadow_style3(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 8)  # 偏移
        effect_shadow.setBlurRadius(48)  # 阴影半径
        effect_shadow.setColor(QColor(243, 175, 189))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)
    def effect_shadow_style4(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 8)  # 偏移
        effect_shadow.setBlurRadius(48)  # 阴影半径
        effect_shadow.setColor(QColor(66, 226, 192))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)

    # 跳转页面函数设定
    def displayIntroPage(self):
        text = self.IntroList.currentItem().text()
        if text == 'Mainpage':
            self.DisplayPage.setCurrentIndex(0)  # 主页
            self.MainWeb.load(QUrl.fromLocalFile(ABS_PATH+HTML_PATH+'ComplexBar_0.html'))
    def displayDetailsPage(self):
        text = self.DetailsList.currentItem().text()
        if text == 'Bar':
            self.DisplayPage.setCurrentIndex(2)  # Bar页
            self.BarWeb.load(QUrl.fromLocalFile(ABS_PATH+HTML_PATH+'Bar_Simple_0.html'))
        if text == 'Pie':
            self.DisplayPage.setCurrentIndex(3)  # Pie页
            self.PieWeb.load(QUrl.fromLocalFile(ABS_PATH+HTML_PATH+'Pie_Simple_0.html'))
        elif text == 'Graph':
            self.DisplayPage.setCurrentIndex(4)  # Graph页
            self.GraphWeb.load(QUrl.fromLocalFile(ABS_PATH+HTML_PATH+'Tree_Circle_0.html'))

    # 搜索页面函数设定
    def displaySearchPage(self):
        text = self.SearchBarLine.text()
        self.DisplayPage.setCurrentIndex(1)  # Search页
        self.entidChanged(text)

    def entidChanged(self, text):
        entid = int(text)
        extract = data[data['entid'] == entid]
        type = extract['CaseType'].tolist()[0]
        type = int(type)
        # importance = ABS_PATH + HTML_PATH+'type%d_importance.html' % type
        # probability = ABS_PATH + HTML_PATH+'%d.html' % entid
        # al = ABS_PATH + '/e_htmls/Al_%d.html' % entid
        # image = ABS_PATH + '/images/%d.png' % entid
        # self.SearchWeb.load(QUrl.fromLocalFile(importance))
        # self.SearchWeb.load(QUrl.fromLocalFile(probability))
        # self.SearchWeb.load(QUrl.fromLocalFile(al))
        self.SearchWeb.load(QUrl.fromLocalFile(ABS_PATH + HTML_PATH + 'Tree_Circle_0.html'))
        # self.SearchWeb.setStyleSheet('image:url(./images/102673201.png)')

    # Web饼状图显示设定
    def initPie(self,):
        pie=Pie()
        pie.add(
            "",
            [list(z) for z in zip(Faker.choose(),Faker.values())],
            radius=["40%","75%"],
        )
        pie.set_global_opts(
            title_opts=opts.TitleOpts(title=''),
            legend_opts=opts.LegendOpts(orient="vertical",pos_top="15%",pos_left="2%"),
        )
        pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        pie.render(self.html)
        self.MainWeb.setUrl(QUrl('file://'+self.html))
        self.MainWeb.setZoomFactor(0.5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())