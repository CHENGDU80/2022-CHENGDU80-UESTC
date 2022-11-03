import sys
import os
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

path = os.getcwd()
print(path)
data = pd.read_csv('ent_type.csv')


class MainPage(QWidget):
    def __init__(self):
        super(MainPage, self).__init__()
        self.visibleFlag = False  # 初始不可见
        self.initUI()

    def initUI(self):
        # 将窗口大小设置为屏幕可用大小
        desktop = QApplication.desktop()
        sw = desktop.width()
        sh = desktop.height()
        self.resize(sw, sh)
        layout = QGridLayout()
        self.setLayout(layout)
        # 设置主体控件
        self.widget1 = QWidget()
        self.widget2 = QStackedWidget()
        layout.addWidget(self.widget1, 0, 0, 1, 2)
        layout.addWidget(self.widget2, 1, 0, 12, 1)
        # 设置widget1
        layout1 = QGridLayout()
        self.widget1.setLayout(layout1)
        # 创建子控件
        self.widget11 = QPushButton('Fintech-UESTCElite')
        self.widget12 = QWidget()
        layout1.addWidget(self.widget11, 0, 0, 1, 3)
        layout1.addWidget(self.widget12, 0, 3, 1, 6)
        # 设置logo和队名
        self.widget11.setIcon(QIcon('./images/logo.png'))
        self.widget11.setIconSize(QSize(80, 80))
        font1 = QFont()
        font1.setBold(True)
        font1.setPointSize(60)
        self.widget11.setFont(font1)
        self.widget11.setFlat(True)
        self.widget11.setStyleSheet('text-align:left')
        # 设置搜索框
        font12 = QFont()
        font12.setPointSize(25)
        layout12 = QGridLayout()
        self.widget12.setLayout(layout12)
        self.lineEdit12 = QLineEdit('Please input an entid:')
        self.lineEdit12.setFont(font12)
        self.btn12 = QPushButton()
        layout12.addWidget(self.lineEdit12, 0, 0, 1, 8)
        layout12.addWidget(self.btn12, 0, 8, 1, 1)
        self.btn12.setIcon(QIcon('./images/search.png'))
        self.btn12.setIconSize(QSize(30, 30))
        self.btn12.setFlat(True)
        # 设置页面展示
        self.widget21 = QWidget()
        self.widget22 = QWidget()
        # 将子页面添加入页面展示
        self.widget2.addWidget(self.widget21)
        self.widget2.addWidget(self.widget22)
        # 呈现子页面的效果
        self.widget21UI()
        self.widget22UI()
        self.widget2.setCurrentIndex(0)
        self.widget11.clicked.connect(self.back_mainpage)
        self.btn12.clicked.connect(self.search_context)

    # 定义子页面的内容
    def widget21UI(self):
        layout = QGridLayout()
        self.widget21.setLayout(layout)
        self.w21_widget1 = QWidget()
        self.w21_widget2 = QWebEngineView()
        layout.addWidget(self.w21_widget1, 0, 0, 1, 1)
        layout.addWidget(self.w21_widget2, 0, 1, 1, 2)
        # 对widget1进行设置
        layout1 = QGridLayout()
        self.w21_widget1.setLayout(layout1)
        self.w21_widget11 = QWidget()
        self.w21_widget12 = QWebEngineView()
        self.w21_widget13 = QWebEngineView()
        self.w21_widget14 = QWebEngineView()
        layout1.addWidget(self.w21_widget11, 0, 0, 1, 1)
        layout1.addWidget(self.w21_widget12, 1, 0, 4, 1)
        layout1.addWidget(self.w21_widget13, 5, 0, 4, 1)
        layout1.addWidget(self.w21_widget14, 9, 0, 4, 1)
        load_path = 'file://'+path+'/dist/index.html'
        self.w21_widget2.load(QUrl(load_path))
        # 加载其余控价内容
        self.w21_widget12.load(QUrl.fromLocalFile(path + '/htmls/type_pie.html'))
        self.w21_widget13.load(QUrl.fromLocalFile(path + '/htmls/industry_bar.html'))
        self.w21_widget14.load(QUrl.fromLocalFile(path + '/htmls/enterprise_bar.html'))
        # 设计widget11的界面
        layout11 = QHBoxLayout()
        self.w21_widget11.setLayout(layout11)
        self.w21_btn111 = QPushButton('Choose: ')
        self.w21_btn112 = QPushButton('Total')
        self.w21_btn113 = QPushButton('Risk0')
        self.w21_btn114 = QPushButton('Risk1')
        self.w21_btn115 = QPushButton('Risk2')
        self.w21_btn116 = QPushButton('Risk3')
        layout11.addWidget(self.w21_btn111)
        layout11.addWidget(self.w21_btn112)
        layout11.addWidget(self.w21_btn113)
        layout11.addWidget(self.w21_btn114)
        layout11.addWidget(self.w21_btn115)
        layout11.addWidget(self.w21_btn116)
        font11 = QFont()
        font11.setPointSize(20)
        self.w21_btn111.setFont(font11)
        self.w21_btn112.setFont(font11)
        self.w21_btn113.setFont(font11)
        self.w21_btn114.setFont(font11)
        self.w21_btn115.setFont(font11)
        self.w21_btn116.setFont(font11)
        # 连接跳转页面
        self.w21_btn111.clicked.connect(self.w21_choice_change111)
        self.w21_btn112.clicked.connect(self.w21_choice_change112)
        self.w21_btn113.clicked.connect(self.w21_choice_change113)
        self.w21_btn114.clicked.connect(self.w21_choice_change114)
        self.w21_btn115.clicked.connect(self.w21_choice_change115)
        self.w21_btn116.clicked.connect(self.w21_choice_change116)
        self.w21_btn111.setFlat(True)
        self.w21_btn112.setFlat(True)
        self.w21_btn113.setFlat(True)
        self.w21_btn114.setFlat(True)
        self.w21_btn115.setFlat(True)
        self.w21_btn116.setFlat(True)

    def w21_choice_change111(self):
        self.w21_widget13.load(QUrl.fromLocalFile(path + '/htmls/industry_bar.html'))
        self.w21_widget14.load(QUrl.fromLocalFile(path + '/htmls/enterprise_bar.html'))

    def w21_choice_change112(self):
        self.w21_widget13.load(QUrl.fromLocalFile(path + '/htmls/industry_bar0.html'))
        self.w21_widget14.load(QUrl.fromLocalFile(path + '/htmls/enterprise_bar0.html'))

    def w21_choice_change113(self):
        self.w21_widget13.load(QUrl.fromLocalFile(path + '/htmls/industry_bar1.html'))
        self.w21_widget14.load(QUrl.fromLocalFile(path + '/htmls/enterprise_bar1.html'))

    def w21_choice_change114(self):
        self.w21_widget13.load(QUrl.fromLocalFile(path + '/htmls/industry_bar2.html'))
        self.w21_widget14.load(QUrl.fromLocalFile(path + '/htmls/enterprise_bar2.html'))

    def w21_choice_change115(self):
        self.w21_widget13.load(QUrl.fromLocalFile(path + '/htmls/industry_bar3.html'))
        self.w21_widget14.load(QUrl.fromLocalFile(path + '/htmls/enterprise_bar3.html'))

    def w21_choice_change116(self):
        self.w21_widget13.load(QUrl.fromLocalFile(path + '/htmls/industry_bar4.html'))
        self.w21_widget14.load(QUrl.fromLocalFile(path + '/htmls/enterprise_bar4.html'))

    def widget22UI(self):
        layout = QGridLayout()
        self.widget22.setLayout(layout)
        self.w22_widget1 = QWidget()
        self.w22_widget2 = QWidget()
        layout.addWidget(self.w22_widget1, 0, 0, 1, 1)
        layout.addWidget(self.w22_widget2, 0, 1, 1, 2)
        layout1 = QVBoxLayout()
        self.w22_widget1.setLayout(layout1)
        self.w22_web11 = QWebEngineView()
        self.w22_web12 = QWebEngineView()
        self.w22_web13 = QWebEngineView()
        layout1.addWidget(self.w22_web11)
        layout1.addWidget(self.w22_web12)
        layout1.addWidget(self.w22_web13)
        layout2 = QHBoxLayout()
        self.w22_widget2.setLayout(layout2)
        self.w22_label = QLabel()
        layout2.addWidget(self.w22_label)

    def search_context(self):
        text = self.lineEdit12.text()
        if len(text) == 0 or text == 'Please input an entid:':
            QMessageBox.warning(self, 'Empty Search', 'Please input an entid!', QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes)
            # 重置内容
            self.lineEdit12.setText('Please input an entid:')
        else:
            self.widget2.setCurrentIndex(1)
            self.entid_changed(text)

    def entid_changed(self, text):
        entid = int(text)
        extract = data[data['entid'] == entid]
        if len(extract) == 0:
            QMessageBox.critical(self, 'Error Input', 'Please reinput an entid!', QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.Yes)
        else:
            type = extract['CaseType'].tolist()[0]
            type = int(type)
            importance = path + '/htmls/type%d_importance.html' % type
            probability = path + '/htmls/%d.html' % entid
            al = path + '/e_htmls/Al_%d.html' % entid
            # image = path + '/images/%d.png' % entid
            self.w22_web11.load(QUrl.fromLocalFile(importance))
            self.w22_web12.load(QUrl.fromLocalFile(probability))
            self.w22_web13.load(QUrl.fromLocalFile(al))
            self.w22_label.setStyleSheet('image:url(./images/102673201.png)')

    def back_mainpage(self):
        self.widget2.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainPage()
    main.show()
    sys.exit(app.exec_())