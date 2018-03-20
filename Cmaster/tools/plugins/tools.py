# -*- coding: utf-8 -*-
# 插件内容
# 负责构建界面
# 负责定义构建的界面可能的事件函数
from PyQt5.QtCore import *

from Cmaster.Widget import *
from Cmaster.Button import IconButton,TButton
from Cmaster.HCore import Config
from PyQt5 import QtCore, QtGui, QtWidgets
from Cmaster.HCore import uitable,uibox
import logging

global langedit

# 读取语言文件，注意encoding为utf-8
def readlang(dictfile = './bin/Chinese.txt'):
    f = open(dictfile, 'r',encoding='utf-8')
    a = f.read()
    trans = eval(a)
    f.close()
    return trans
def e_load(para):
    global langedit
    files = uibox.openfiles('./bin/Chinese.txt')
    for file in files:
        dicli = readlang(file[0])
        uitable.rlist(langedit, list(dicli.values()), list(dicli.keys()), file[1])
def e_add(para):
    global langedit
    word=uibox.input("add")
    if word!=None:
        li=[]
        li.append(word)
        uitable.rlist(langedit,[""],li)
def e_del(para):
    global langedit
    uitable.delrow(langedit)
def e_save(para):
    global langedit
    dicli = uitable.getcdict(langedit)
    for fn in dicli.keys():
        dictfile = "./bin/%s.txt" % fn
        f = open(dictfile, 'w',encoding='utf-8')
        f.write(str(dicli[fn]))
        f.close()

def on_lang(para):
    rootwin = para['root']

    global langedit
    langedit = QtWidgets.QTableWidget()
    langedit.setAutoScrollMargin(16)
    langedit.setObjectName("tablelist")
    langedit.setColumnCount(0)
    langedit.setRowCount(0)

    _loadbtn_action = rootwin.add_action("load", "about", "Load Language File", False, 'tools','loadevent')
    _addbtn_action = rootwin.add_action("add", "about", "Add one row", False, 'tools', 'addevent')
    _delbtn_action = rootwin.add_action("del", "about", "Del one row", False, 'tools', 'delevent')
    spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    _savebtn_action = rootwin.add_action("save", "about", "Save to file", False, 'tools', 'saveevent')

    itemls=[_loadbtn_action,_addbtn_action,_delbtn_action,spacerItem,_savebtn_action]

    docklay={
        'H':[langedit,{"V":itemls}]
    }

    rootwin.auto_dock("Language",docklay)

def on_samp(para):
    rootwin = para['root']
    tree = QTreeWidget()
    headerItem = QTreeWidgetItem(["seq", "name", "func", "message", 'condition', 'goto'])
    item = QTreeWidgetItem()
    tree.setHeaderItem(headerItem)
    for i in range(4):
        parent = QTreeWidgetItem(tree)
        parent.setText(0, "Parent {}".format(i))
        parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
        for x in range(5):
            child = QTreeWidgetItem(parent)
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
            child.setText(0, "Child {}".format(x))
            child.setCheckState(0, Qt.Unchecked)
    _dial = QtWidgets.QDial()
    _dial.setMaximumSize(QtCore.QSize(16777215, 16777215))
    _dial.setObjectName("dial")
    docklay = {
        'H': [tree, _dial]
    }
    rootwin.auto_dock('editwin', docklay)

def tools(para):
    mainwin=para['root']
    app=para['tools']
    # -------- Qbuttom ----------
    # mainwin的函数add_action(caption, icon_name, status_tip, icon_visible, appname,eventname, shortcut=None):
    _about_action = mainwin.add_action("language", "database", "Program Language", True, 'tools','lang')
    _sample_action = mainwin.add_action("sample", "sample", "sample for ui", True, 'tools','sample')
    # -------- Tab --------------
    about_tab = mainwin._ribbon.add_ribbon_tab("Tools")  # Tab Name-----------
    info_panel = about_tab.add_ribbon_pane("Tools")  #Pane Name----------------
    other_panel =about_tab.add_ribbon_pane("Others")

    # Add Button----------
    info_panel.add_ribbon_widget(IconButton(mainwin, _about_action, True))
    other_panel.add_ribbon_widget(IconButton(mainwin, _sample_action, True))

    return 'about build finish'
def demo(para):
    print('demo',para)
#>>>>>>>>有待其他地方复用插件系统>>>>>>>
def setup(app):
    app.register_guis('8000tools', demo)

#插件负责界面构建函数和注册响应事件函数
def build(app):
    app.register_guis('8000 tools', tools)
    app.register_events('lang',on_lang)
    app.register_events('sample',on_samp)
    app.register_events('loadevent',e_load)
    app.register_events('addevent',e_add)
    app.register_events('delevent',e_del)
    app.register_events('saveevent',e_save)

