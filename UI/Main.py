import sys
import pandas as pd
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtGui import QColor, QPixmap, QMovie
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog

from MainWindow import Ui_MainWindow
from Config import *


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

        # 设定用户界面鼠标点击变量
        self.user_click = 0
        self.user_name =['UserID: c4e0d49d5bf94efa446e03ecf84ba5', 'UserID: ee0eed4ad96f4f5d6dc30d56bdf94',
                         'UserID: a9815449c0a385ee0d53305b8cca95c6', 'UserID: f9dd0d609cee4360e110d56cc35afd9',
                         'UserID: de5e19a5ea36e8f4b9f4cf5bdd953']

        # 设置页面切换响应事件
        self.IntroList.itemClicked.connect(self.displayIntroPage)
        self.DetailsList.itemClicked.connect(self.displayDetailsPage)
        self.SearchBarButton.clicked.connect(self.displayUserPage)

        # 页面设定
        self.mainPageStart()
        self.userPageStart()
        self.modelPageStart()
        self.analysisPageStart()
        self.barPageStart()
        self.piePageStart()
        self.graphPageStart()
        self.treePageStart()
        self.radarPageStart()

        # 窗口设定
        self.PageCloseButton.clicked.connect(QCoreApplication.instance().quit)
        self.PageMaximizeButton.clicked.connect(self.windowMaximized)
        self.PageMinimizeButton.clicked.connect(self.windowMinimized)

        # 设定LOGO
        self.LOGOWeb.load(QUrl.fromLocalFile(ABS_PATH+MAIN_PATH+'LOGO.html'))
        self.LOGOWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))
        self.LOGOWeb.settings().setAttribute(self.LOGOWeb.settings().ShowScrollBars, False)

    # 首页-函数设定
    def mainPageStart(self,):
        # 设置底端阴影效果
        self.effect_shadow_style1(self.FirstFrame)
        self.effect_shadow_style2(self.SecondFrame)
        self.effect_shadow_style3(self.ThirdFrame)
        self.effect_shadow_style4(self.FourthFrame)

        # 设置用户滚动阴影效果
        self.effect_shadow_style0(self.Scroll1)
        self.effect_shadow_style0(self.Scroll2)
        self.effect_shadow_style0(self.Scroll3)
        self.effect_shadow_style0(self.Scroll4)
        self.effect_shadow_style0(self.Scroll5)
        self.effect_shadow_style0(self.Scroll6)
        self.effect_shadow_style0(self.Scroll7)

        # 设置首页选择列表的跳转函数
        # self.MainPageChooseList.itemClicked.connect(self.mainPageList)

        # 设置按钮展示选择
        self.FirstFrameButton.clicked.connect(self.mainPageFirstButton)
        self.SecondFrameButton.clicked.connect(self.mainPageSecondButton)
        self.ThirdFrameButton.clicked.connect(self.mainPageThirdButton)
        self.FourthFrameButton.clicked.connect(self.mainPageFourthButton)

        # 首页大屏效果
        self.FirstFrameWeb.load(QUrl.fromLocalFile(ABS_PATH+MAIN_PATH+'Main_Graph_Simple_0.html'))
        self.SecondFrameWeb.load(QUrl.fromLocalFile(ABS_PATH+MAIN_PATH+'Main_Tree_Time_0.html'))
        self.ThirdFrameWeb.load(QUrl.fromLocalFile(ABS_PATH+MAIN_PATH+'Main_Bar_3D_0.html'))
        self.FourthFrameWeb.load(QUrl.fromLocalFile(ABS_PATH+MAIN_PATH+'Main_Radar_Simple_0.html'))
        self.RadarWeb.load(QUrl.fromLocalFile(ABS_PATH+MAIN_PATH+'Main_Structure_0.html'))
        self.FirstFrameWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))
        self.SecondFrameWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))
        self.ThirdFrameWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))
        self.FourthFrameWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))
        self.RadarWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))

    # 首页-Button元素选择跳转
    def mainPageFirstButton(self):
        self.DisplayPage.setCurrentIndex(2)  # Bar页
        self.barPageStart()
    def mainPageSecondButton(self):
        self.DisplayPage.setCurrentIndex(3)  # Pie页
        self.piePageStart()
    def mainPageThirdButton(self):
        self.DisplayPage.setCurrentIndex(4)  # Graph页
        self.graphPageStart()
    def mainPageFourthButton(self):
        self.DisplayPage.setCurrentIndex(4)  # Graph页
        self.graphPageStart()

    # userPage页-函数设定
    def userPageStart(self):
        # self.UserPageChooseList.itemClicked.connect(self.userPageList)
        self.UserRardaWeb.load(QUrl.fromLocalFile(ABS_PATH+USER_PATH+'User_Radar_Simple_0.html'))
        self.UserRardaWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))
        self.UserTreeWeb.load(QUrl.fromLocalFile(ABS_PATH+USER_PATH+'User_Tree_Simple_0.html'))
        self.UserTreeWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))
        self.UserTreeWeb_2.load(QUrl.fromLocalFile(ABS_PATH+USER_PATH+'User_Time_Simple_'+str(self.user_click%5)+'.html'))
        self.UserTreeWeb_2.page().setBackgroundColor(QColor(0, 0, 0, 0))

        # 切换用户界面按钮
        self.UserNext.clicked.connect(self.userSwitch)
        self.UserBefore.clicked.connect(self.userSwitch)
        self.UserAgree.clicked.connect(self.userSwitch)
        self.UserDisagree.clicked.connect(self.userSwitch)

    # userPage页-用户界面切换
    def userSwitch(self):
        # 用户属性切换
        self.UserRardaWeb.load(QUrl.fromLocalFile(ABS_PATH+USER_PATH+'User_Radar_Simple_'+str(self.user_click%5)+'.html'))
        self.UserRardaWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))
        self.UserTreeWeb.load(QUrl.fromLocalFile(ABS_PATH+USER_PATH+'User_Tree_Simple_'+str(self.user_click%5)+'.html'))
        self.UserTreeWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))
        self.UserTreeWeb_2.load(QUrl.fromLocalFile(ABS_PATH+USER_PATH+'User_Time_Simple_'+str(self.user_click%5)+'.html'))
        self.UserTreeWeb_2.page().setBackgroundColor(QColor(0, 0, 0, 0))

        # 用户头像与信息切换
        self.UserPic.setPixmap(QtGui.QPixmap('images/人物头像'+str(self.user_click%5)+'.png'))
        self.UserPic.setAlignment(QtCore.Qt.AlignCenter)
        self.UserName.setPalette(QtGui.QPalette())
        self.UserName.setText(QtCore.QCoreApplication.translate("MainWindow", self.user_name[self.user_click%5]))
        self.UserName.setStyleSheet("background-color: rgb(22, 76, 140);\n""border-radius:6px")

        # 用户特征属性切换
        self.A1Label.setText(QtCore.QCoreApplication.translate("MainWindow",str(np.random.randint(30,100))))
        self.A2Label.setText(QtCore.QCoreApplication.translate("MainWindow",str(np.random.randint(30,100))))
        self.A3Label.setText(QtCore.QCoreApplication.translate("MainWindow",str(np.random.randint(30,100))))
        self.A4Label.setText(QtCore.QCoreApplication.translate("MainWindow",str(np.random.randint(30,100))))
        self.A5Label.setText(QtCore.QCoreApplication.translate("MainWindow",str(np.random.randint(30,100))))
        self.PersonalCredit.setText(QtCore.QCoreApplication.translate("MainWindow",str(np.random.randint(30,80))))
        self.PersonalCredit1.setText(QtCore.QCoreApplication.translate("MainWindow",str(bool(np.random.randint(0,2)))))
        self.PersonalCredit1.setText(QtCore.QCoreApplication.translate("MainWindow",str(bool(np.random.randint(0,2)))))
        self.PersonalCredit1.setText(QtCore.QCoreApplication.translate("MainWindow",str(bool(np.random.randint(0,2)))))

        # 发送切换信号
        self.user_click = self.user_click + 1

    # userPage页-ListWeb元素选择跳转
    def userPageList(self):
        text = self.UserPageChooseList.currentItem().text()
        if text == 'show the analysis of current user':
            # 用户属性切换
            self.UserRardaWeb.load(
                QUrl.fromLocalFile(ABS_PATH+USER_PATH+'User_Radar_Simple_'+str(self.user_click % 5)+'.html'))
            self.UserRardaWeb.page().setBackgroundColor(QColor(0,0,0,0))
            self.UserTreeWeb.load(
                QUrl.fromLocalFile(ABS_PATH+USER_PATH+'User_Tree_Simple_'+str(self.user_click % 5)+'.html'))
            self.UserTreeWeb.page().setBackgroundColor(QColor(0,0,0,0))
            self.UserTreeWeb_2.load(
                QUrl.fromLocalFile(ABS_PATH+USER_PATH+'User_Time_Simple_'+str(self.user_click % 5)+'.html'))
            self.UserTreeWeb_2.page().setBackgroundColor(QColor(0,0,0,0))

            # 用户头像与信息切换
            self.UserPic.setPixmap(QtGui.QPixmap('images/人物头像'+str(self.user_click % 5)+'.png'))
            self.UserPic.setAlignment(QtCore.Qt.AlignCenter)
            self.UserName.setPalette(QtGui.QPalette())
            self.UserName.setText(QtCore.QCoreApplication.translate("MainWindow",self.user_name[self.user_click % 5]))
            self.UserName.setStyleSheet("background-color: rgb(22, 76, 140);\n""border-radius:6px")

            # 用户特征属性切换
            self.A1Label.setText(QtCore.QCoreApplication.translate("MainWindow",str(np.random.randint(30,100))))
            self.A2Label.setText(QtCore.QCoreApplication.translate("MainWindow",str(np.random.randint(30,100))))
            self.A3Label.setText(QtCore.QCoreApplication.translate("MainWindow",str(np.random.randint(30,100))))
            self.A4Label.setText(QtCore.QCoreApplication.translate("MainWindow",str(np.random.randint(30,100))))
            self.A5Label.setText(QtCore.QCoreApplication.translate("MainWindow",str(np.random.randint(30,100))))
            self.PersonalCredit.setText(QtCore.QCoreApplication.translate("MainWindow",str(np.random.randint(30,80))))
            self.PersonalCredit1.setText(QtCore.QCoreApplication.translate("MainWindow",str(bool(np.random.randint(0,2)))))
            self.PersonalCredit1.setText(QtCore.QCoreApplication.translate("MainWindow",str(bool(np.random.randint(0,2)))))
            self.PersonalCredit1.setText(QtCore.QCoreApplication.translate("MainWindow",str(bool(np.random.randint(0,2)))))


    # modelPage页-函数设定
    def modelPageStart(self):
        self.ModelPageChooseList.itemClicked.connect(self.userPageList)
        self.ModelStructureWeb.load(QUrl.fromLocalFile(ABS_PATH+MODEL_PATH+'Model_Structure_0.html'))
        self.ModelStructureWeb.page().setBackgroundColor(QColor(0,0,0,0))
        self.Gif = QMovie()
        self.Gif.setFileName("images/Loan.gif")
        self.ModelGif.setMovie(self.Gif)
        self.Gif.start()

    # modelPage页-ListWeb元素选择跳转
    def modelPageList(self):
        text = self.ModelPageChooseList.currentItem().text()
        if text == 'show the model process of current user':
            self.ModelStructureWeb.load(QUrl.fromLocalFile(ABS_PATH+MODEL_PATH+'Model_Structure_0.html'))
            self.ModelStructureWeb.page().setBackgroundColor(QColor(0,0,0,0))
            self.Gif=QMovie()
            self.Gif.setFileName("images/Loan.gif")
            self.ModelGif.setMovie(self.Gif)
            self.Gif.start()


    # analysisPage页-函数设定
    def analysisPageStart(self):
        # 设置底端阴影效果
        self.effect_shadow_style1(self.FirstFrame_2)
        self.effect_shadow_style2(self.SecondFrame_2)
        self.effect_shadow_style3(self.ThirdFrame_2)
        self.effect_shadow_style4(self.FourthFrame_2)

        # 显示web组件
        self.FirstFrameWeb_2.load(QUrl.fromLocalFile(ABS_PATH+ANALYSIS_PATH+'Analysis_Graph_Simple_0.html'))
        self.FirstFrameWeb_2.page().setBackgroundColor(QColor(0, 0, 0, 0))
        self.SecondFrameWeb_2.load(QUrl.fromLocalFile(ABS_PATH+ANALYSIS_PATH+'Analysis_Tree_Time_0.html'))
        self.SecondFrameWeb_2.page().setBackgroundColor(QColor(0, 0, 0, 0))
        self.ThirdFrameWeb_2.load(QUrl.fromLocalFile(ABS_PATH+ANALYSIS_PATH+'Analysis_Bar_3D_0.html'))
        self.ThirdFrameWeb_2.page().setBackgroundColor(QColor(0, 0, 0, 0))
        self.FourthFrameWeb_2.load(QUrl.fromLocalFile(ABS_PATH+ANALYSIS_PATH+'Analysis_Radar_Simple_0.html'))
        self.FourthFrameWeb_2.page().setBackgroundColor(QColor(0,0,0,0))

    # modelPage页-ListWeb元素选择跳转
    def analysisPageList(self):
        text = self.AnalysisPageChooseLayout.currentItem().text()
        if text == 'show the analysis of all users':
            self.FirstFrameWeb_2.load(QUrl.fromLocalFile(ABS_PATH+ANALYSIS_PATH+'Analysis_Graph_Simple_0.html'))
            self.FirstFrameWeb_2.page().setBackgroundColor(QColor(0,0,0,0))
            self.SecondFrameWeb_2.load(QUrl.fromLocalFile(ABS_PATH+ANALYSIS_PATH+'Analysis_Tree_Time_0.html'))
            self.SecondFrameWeb_2.page().setBackgroundColor(QColor(0,0,0,0))
            self.ThirdFrameWeb_2.load(QUrl.fromLocalFile(ABS_PATH+ANALYSIS_PATH+'Analysis_Bar_3D_0.html'))
            self.ThirdFrameWeb_2.page().setBackgroundColor(QColor(0,0,0,0))
            self.FourthFrameWeb_2.load(QUrl.fromLocalFile(ABS_PATH+ANALYSIS_PATH+'Analysis_Radar_Simple_0.html'))
            self.FourthFrameWeb_2.page().setBackgroundColor(QColor(0,0,0,0))


    # barPage页-函数设定
    def barPageStart(self):
        # 设置piePage页选择列表的跳转函数
        self.BarPageChooseList.itemClicked.connect(self.barPageList)
        self.BarWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Bar_Simple_0.html'))
        self.BarWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))

    # barPage页-ListWeb元素选择跳转
    def barPageList(self):
        text = self.BarPageChooseList.currentItem().text()
        if text == 'Bar 1':
            self.BarWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Bar_Simple_0.html'))
        elif text == 'Bar 2':
            self.BarWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Bar_Complex_0.html'))
        elif text == 'Bar 3':
            self.BarWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Bar_Simple_0.html'))
        elif text == 'Bar 4':
            self.BarWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Bar_Complex_0.html'))
        self.BarWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))

    # piePage页-函数设定
    def piePageStart(self):
        # 设置piePage页选择列表的跳转函数
        self.PiePageChooseList.itemClicked.connect(self.piePageList)
        self.PieWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Pie_Complex_0.html'))
        self.PieWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))

    # piePage页-ListWeb元素选择跳转
    def piePageList(self):
        text = self.PiePageChooseList.currentItem().text()
        if text == 'Pie 1':
            self.PieWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Pie_Complex_0.html'))
        elif text == 'Pie 2':
            self.PieWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Pie_Complex_0.html'))
        elif text == 'Pie 3':
            self.PieWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Pie_Complex_0.html'))
        elif text == 'Pie 4':
            self.PieWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Pie_Complex_0.html'))
        self.PieWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))

    # graphPage页-函数设定
    def graphPageStart(self):
        # 设置piePage页选择列表的跳转函数
        self.GraphPageChooseList.itemClicked.connect(self.graphPageList)
        self.GraphWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Graph_Simple_0.html'))
        self.GraphWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))

    # graphPage页-ListWeb元素选择跳转
    def graphPageList(self):
        text = self.GraphPageChooseList.currentItem().text()
        if text == 'Graph 1':
            self.GraphWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Graph_Simple_0.html'))
        if text == 'Graph 2':
            self.GraphWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Graph_Simple_0.html'))
        if text == 'Graph 3':
            self.GraphWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Graph_Simple_0.html'))
        if text == 'Graph 4':
            self.GraphWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Graph_Simple_0.html'))
        self.GraphWeb.page().setBackgroundColor(QColor(0,0,0,0))

    # TreePage页-函数设定
    def treePageStart(self):
        # 设置piePage页选择列表的跳转函数
        self.TreePageChooseList.itemClicked.connect(self.treePageList)
        self.TreeWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Tree_Circle_0.html'))
        self.TreeWeb.page().setBackgroundColor(QColor(0, 0, 0, 0))

    # TreePage页-ListWeb元素选择跳转
    def treePageList(self):
        text = self.TreePageChooseList.currentItem().text()
        if text == 'Tree 1':
            self.TreeWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Tree_Simple_0.html'))
        if text == 'Tree 2':
            self.TreeWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Tree_Circle_0.html'))
        if text == 'Tree 3':
            self.TreeWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Tree_Circle_0.html'))
        if text == 'Tree 4':
            self.TreeWeb.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Tree_Circle_0.html'))
        self.TreeWeb.page().setBackgroundColor(QColor(0,0,0,0))

    # RadarPage页-函数设定
    def radarPageStart(self):
        # 设置piePage页选择列表的跳转函数
        self.RadarPageChooseList.itemClicked.connect(self.radarPageList)
        self.RadarWeb_2.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Radar_Complex_0.html'))
        self.RadarWeb_2.page().setBackgroundColor(QColor(0, 0, 0, 0))

    # RadarPage页-ListWeb元素选择跳转
    def radarPageList(self):
        text = self.RadarPageChooseList.currentItem().text()
        if text == 'Radar 1':
            self.RadarWeb_2.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Radar_Simple_0.html'))
        if text == 'Radar 2':
            self.RadarWeb_2.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Radar_Complex_0.html'))
        if text == 'Radar 3':
            self.RadarWeb_2.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Radar_Simple_0.html'))
        if text == 'Radar 4':
            self.RadarWeb_2.load(QUrl.fromLocalFile(ABS_PATH+PATH+'Radar_Complex_0.html'))
        self.RadarWeb.page().setBackgroundColor(QColor(0,0,0,0))

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
    def effect_shadow_style0(self,widget):
        effect_shadow=QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 5)  # 偏移
        effect_shadow.setBlurRadius(12)  # 阴影半径
        effect_shadow.setColor(QtCore.Qt.gray)  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)
    def effect_shadow_style1(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 8)  # 偏移
        effect_shadow.setBlurRadius(10)  # 阴影半径
        effect_shadow.setColor(QColor(162, 129, 247))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)
    def effect_shadow_style2(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 8)  # 偏移
        effect_shadow.setBlurRadius(10)  # 阴影半径
        effect_shadow.setColor(QColor(253, 139, 133))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)
    def effect_shadow_style3(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 8)  # 偏移
        effect_shadow.setBlurRadius(10)  # 阴影半径
        effect_shadow.setColor(QColor(243, 175, 189))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)
    def effect_shadow_style4(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 8)  # 偏移
        effect_shadow.setBlurRadius(10)  # 阴影半径
        effect_shadow.setColor(QColor(66, 226, 192))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)

    # 跳转页面函数设定
    def displayIntroPage(self):
        text = self.IntroList.currentItem().text()
        if text == 'Mainpage':
            self.DisplayPage.setCurrentIndex(0)  # 主页
            self.mainPageStart()
        if text == 'User':
            self.DisplayPage.setCurrentIndex(1)  # 用户页面
            self.userPageStart()
        if text == 'Model':
            self.DisplayPage.setCurrentIndex(2)  # 模型页面
            self.modelPageStart()
        if text == 'Analysis':
            self.DisplayPage.setCurrentIndex(3)  # 分析页面
            self.analysisPageStart()
    def displayDetailsPage(self):
        text = self.DetailsList.currentItem().text()
        if text == 'Bar':
            self.DisplayPage.setCurrentIndex(4)  # Bar页
            self.barPageStart()
        if text == 'Pie':
            self.DisplayPage.setCurrentIndex(5)  # Pie页
            self.piePageStart()
        elif text == 'Graph':
            self.DisplayPage.setCurrentIndex(6)  # Graph页
            self.graphPageStart()
        elif text == 'Tree':
            self.DisplayPage.setCurrentIndex(7)  # Tree页
            self.graphPageStart()
        elif text == 'Radar':
            self.DisplayPage.setCurrentIndex(8)  # Radar页
            self.graphPageStart()

    # 搜索页面函数设定
    def displayUserPage(self):
        text = self.SearchBarLine.text()
        self.DisplayPage.setCurrentIndex(1)  # User页
        self.entidChanged(text)

    def entidChanged(self, text):
        self.DisplayPage.setCurrentIndex(1)  # 用户页面
        self.userPageStart()
        # entid = int(text)
        # extract = data[data['entid'] == entid]
        # ype = extract['CaseType'].tolist()[0]
        # type = int(type)
        # importance = ABS_PATH + HTML_PATH+'type%d_importance.html' % type
        # probability = ABS_PATH + HTML_PATH+'%d.html' % entid
        # al = ABS_PATH + '/e_htmls/Al_%d.html' % entid
        # image = ABS_PATH + '/images/%d.png' % entid
        # self.UserWeb.load(QUrl.fromLocalFile(importance))
        # self.UserWeb.load(QUrl.fromLocalFile(probability))
        # self.UserWeb.load(QUrl.fromLocalFile(al))
        # self.UserRardaWeb.load(QUrl.fromLocalFile(ABS_PATH + PATH + 'Bar_3D_0.html'))
        # self.UserWeb.setStyleSheet('image:url(./images/102673201.png)')

    # 窗口最大化函数设定
    def windowMaximized(self):
        # 获取桌面尺寸
        desktop = QApplication.desktop()
        rect = desktop.availableGeometry()
        self.setGeometry(rect)  # 这样就可以了，就是会导致窗口的标题栏在最上边不可见

    # 窗口最小化函数设定
    def windowMinimized(self):
        desktop = QApplication.desktop()
        desktopRect = desktop.availableGeometry()
        desktopRect.width()
        rect = QtCore.QRect(int((desktopRect.width()-WINDOW_WIDTH)/2), int((desktopRect.height()-WINDOW_HEIGHT)/2),
                            WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setGeometry(rect)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())