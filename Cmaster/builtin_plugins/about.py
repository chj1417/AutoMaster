# -*- coding: utf-8 -*-
# 插件内容
# 负责构建界面
# 负责定义构建的界面可能的事件函数

from Cmaster.Widget import *
from Cmaster.Button import IconButton
from Cmaster.HCore import Config

def on_about(para):
    # title=Config.read_ini('Main','Title','AutoMaster')
    title='autom'
    # text = "%s\n--==ChenHuaJun==--"%Config.read_ini('Main','About','AutoMaster\n Version 1.0.0')
    text='tttext'
    print(para,'=========para in func')
    # QMessageBox().about(self, "About %s"%title, text)

def on_license(para):
    # file = open('LICENSE', 'r')
    # lic = file.read()
    # QMessageBox().information(self, "License", lic)
    print('on license')

def about(para):
    # print(para,'=====++++++++')
    mainwin=para[0]
    # mainwin的函数add_action(caption, icon_name, status_tip, icon_visible, connection, shortcut=None):

    _about_action = mainwin.add_action("About", "about", "About QupyRibbon", True, [para[1],'about'])
    _license_action = mainwin.add_action("License", "license", "Licence for this software", True, [para[1],'license'])
    about_tab = mainwin._ribbon.add_ribbon_tab("About")  # Tab Name
    info_panel = about_tab.add_ribbon_pane("Info")  #Pane Name
    # Add Button
    info_panel.add_ribbon_widget(IconButton(mainwin, _about_action, True))
    info_panel.add_ribbon_widget(IconButton(mainwin, _license_action, True))

    return 'ok'

def setup(app):
    app.register_formatter('00lowercase', make_lowercase)

#插件负责界面构建函数和注册响应事件函数
def build(app):
    app.register_formatter('00 build tab', about)
    app.register_events('about',on_about)
    app.register_events('license',on_license)
