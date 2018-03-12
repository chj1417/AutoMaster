# -*- coding: utf-8 -*-
# 插件内容
# 负责构建界面
# 负责定义构建的界面可能的事件函数

from Cmaster.Widget import *
from Cmaster.Button import IconButton
from Cmaster.HCore import Config
from PyQt5 import QtCore, QtGui, QtWidgets

def on_lang(para):

    rootwin = para['root']
    _dockWidget = QtWidgets.QDockWidget(rootwin)
    _dockWidget.setObjectName("dockWidget")
    _dockWidget.setWindowTitle("Language")
    _dockWidgetContents = QtWidgets.QWidget()
    _dockWidgetContents.setObjectName("dockWidgetContents")
    #
    _verticalLayout_2 = QtWidgets.QVBoxLayout(_dockWidgetContents)
    _verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
    _verticalLayout_2.setContentsMargins(12, 12, 12, 12)
    _verticalLayout_2.setObjectName("verticalLayout_2")
    _horizontalLayout = QtWidgets.QHBoxLayout()
    _horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
    _horizontalLayout.setObjectName("horizontalLayout")
    _tablelist = QtWidgets.QTableWidget(_dockWidgetContents)
    _tablelist.setAutoScrollMargin(16)
    _tablelist.setObjectName("tablelist")
    _tablelist.setColumnCount(0)
    _tablelist.setRowCount(0)
    _horizontalLayout.addWidget(_tablelist)
    _verticalLayout = QtWidgets.QVBoxLayout()
    _verticalLayout.setObjectName("verticalLayout")
    _openbtn = QtWidgets.QPushButton(_dockWidgetContents)
    _openbtn.setObjectName("openbtn")
    _verticalLayout.addWidget(_openbtn)
    _addbtn = QtWidgets.QPushButton(_dockWidgetContents)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(_addbtn.sizePolicy().hasHeightForWidth())
    _addbtn.setSizePolicy(sizePolicy)
    _addbtn.setObjectName("addbtn")
    _verticalLayout.addWidget(_addbtn)
    _delbtn = QtWidgets.QPushButton(_dockWidgetContents)
    _delbtn.setObjectName("delbtn")
    _verticalLayout.addWidget(_delbtn)
    spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    _verticalLayout.addItem(spacerItem)
    _savebtn = QtWidgets.QPushButton(_dockWidgetContents)
    _savebtn.setObjectName("savebtn")
    _verticalLayout.addWidget(_savebtn)
    _exitbtn = QtWidgets.QPushButton(_dockWidgetContents)
    _exitbtn.setObjectName("exitbtn")
    _verticalLayout.addWidget(_exitbtn)
    _horizontalLayout.addLayout(_verticalLayout)
    _verticalLayout_2.addLayout(_horizontalLayout)

    _openbtn.setToolTip("open")
    _openbtn.setText("open")
    _addbtn.setToolTip("add")
    _addbtn.setText("add")
    _delbtn.setToolTip("delrow")
    _delbtn.setText("delrow")
    _savebtn.setToolTip("save")
    _savebtn.setText("save")
    _exitbtn.setToolTip("exit")
    _exitbtn.setText("exit")

    _dockWidget.setWidget(_dockWidgetContents)
    rootwin.addDockWidget(2, _dockWidget)

def on_license(para):
    # file = open('LICENSE', 'r')
    # lic = file.read()
    # QMessageBox().information(self, "License", lic)
    print('on license')

def tools(para):
    mainwin=para['root']
    app=para['tools']
    # -------- Qbuttom ----------
    # mainwin的函数add_action(caption, icon_name, status_tip, icon_visible, paraname,eventname, shortcut=None):
    _about_action = mainwin.add_action("Language", "about", "Program Language", True, 'tools','lang')
    # -------- Tab --------------
    about_tab = mainwin._ribbon.add_ribbon_tab("Tools")  # Tab Name-----------
    info_panel = about_tab.add_ribbon_pane("Tools")  #Pane Name----------------
    # Add Button----------
    info_panel.add_ribbon_widget(IconButton(mainwin, _about_action, True))

    return 'about build finish'
def demo(para):
    print('demo',para)
#>>>>>>>>有待其他地方复用插件系统>>>>>>>
def setup(app):
    app.register_guis('00lowercase', demo)

#插件负责界面构建函数和注册响应事件函数
def build(app):
    app.register_guis('8000 tools', tools)
    app.register_events('lang',on_lang)
    # app.register_events('license',on_license)
