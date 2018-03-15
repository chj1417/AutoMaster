# -*- coding: utf-8 -*-
# 插件内容
# 负责构建界面
# 负责定义构建的界面可能的事件函数

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
    print('add--')
def e_del(para):
    print('del---')
def e_save(para):
    print('save----')
def e_close(para):
    print('close-----')

def on_lang(para):

    rootwin = para['root']
    global langedit
    # _tablelist = QtWidgets.QTableWidget(_dockWidgetContents)
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
    _closebtn_action = rootwin.add_action("close", "about", "Close the window", False, 'tools', 'closeevent')

    itemls=[_loadbtn_action,_addbtn_action,_delbtn_action,spacerItem,_savebtn_action,_closebtn_action]

    docklay={
        'H':[langedit,{"V":itemls}]
    }

    rootwin.auto_dock("Language",docklay)

def on_license(para):
    # file = open('LICENSE', 'r')
    # lic = file.read()
    # QMessageBox().information(self, "License", lic)
    print('on license')

def tools(para):
    mainwin=para['root']
    app=para['tools']
    # -------- Qbuttom ----------
    # mainwin的函数add_action(caption, icon_name, status_tip, icon_visible, appname,eventname, shortcut=None):
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
    app.register_events('loadevent',e_load)
    app.register_events('addevent',e_add)
    app.register_events('delevent',e_del)
    app.register_events('saveevent',e_save)
    app.register_events('closeevent',e_close)

