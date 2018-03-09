# -*- coding: utf-8 -*-
# 插件内容
# 负责构建界面
# 负责定义构建的界面可能的事件函数

from Cmaster.Widget import *
from Cmaster.Button import IconButton
from Cmaster.HCore import Config

def on_about(para):
    rootwin=para['root']
    title=Config.read_key('Main','Title','AutoMaster')
    text = "%s\n--==ChenHuaJun==--"%Config.read_key('Main','About','AutoMaster\n Version 1.0.0')
    QMessageBox().about(rootwin, "About %s"%title, text)

def on_license(para):
    # file = open('LICENSE', 'r')
    # lic = file.read()
    # QMessageBox().information(self, "License", lic)
    print('on license')

def about(para):
    print(para,'=====++++++++')
    mainwin=para['root']
    app=para['about']
    # mainwin的函数add_action(caption, icon_name, status_tip, icon_visible, connection, shortcut=None):
    _about_action = mainwin.add_action("About", "about", "About QupyRibbon", True, 'about','about')
    _license_action = mainwin.add_action("License", "license", "Licence for this software", True, 'about','license')
    about_tab = mainwin._ribbon.add_ribbon_tab("About")  # Tab Name
    info_panel = about_tab.add_ribbon_pane("Info")  #Pane Name
    # Add Button
    info_panel.add_ribbon_widget(IconButton(mainwin, _about_action, True))
    info_panel.add_ribbon_widget(IconButton(mainwin, _license_action, True))

    return 'about build finish'
def demo(para):
    print('demo',para)
#>>>>>>>>有待其他地方复用插件系统>>>>>>>
def setup(app):
    app.register_guis('00lowercase', demo)

#插件负责界面构建函数和注册响应事件函数
def build(app):
    app.register_guis('9000 about', about)
    app.register_events('about',on_about)
    app.register_events('license',on_license)
