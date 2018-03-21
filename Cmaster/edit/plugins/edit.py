# -*- coding: utf-8 -*-
# 插件内容
# 负责构建界面
# 负责定义构建的界面可能的事件函数

# 导入Qt核心模块

# 快捷键模块
from PyQt5.QtGui import QKeySequence as QKSec

# 导入界面常用模块，Qlable可从该模块导入
from Cmaster.Widget import *
# Testbox输入框控件模块
from Cmaster.Textbox import Textbox
# IconButtom图形按钮模块
from Cmaster.Button import IconButton
#
from Cmaster.Tree import TreeList
#

from Cmaster.HCore import csv2tree as treedata
from Cmaster.HCore.sqlite2data import DBfile
#
global tree
treedb = DBfile('./bin/temp.db')
# 定义编辑窗 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def edittree(para):
    rootwin=para['root']
    #
    global tree
    #
    # headtext = treedata.rheader('./bin/sam.csv')
    # ViewData=treedata.rdata('./bin/sam.csv')
    # tree = TreeList(headtext[2:])
    # tree.setlist(ViewData)
    #

    tree=TreeList(treedb.headlist('edit'))
    tree.setlist(treedb.read('edit'))

    docklay={
        'V':[tree]
    }
    rootwin.auto_dock('editwin',docklay)

    # 定义事件函数>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def on_revert(para):
    global tree
    # ViewData = treedata.rdata('./bin/sam.csv')
    ViewData=treedb.read('edit')
    tree.clear()
    tree.setlist(ViewData)
    # return para[0]
def on_commit(para):
    global tree
    #
    # treedata.wdata('./bin/sam.csv',tree.getlist(),tree.head)
    #
    # treedb = DBfile('./bin/temp.db')
    treedb.write(tree.getlist(),'edit')
    # return para[0]
def on_clone(para):
    global tree
    tree.clonelist()
    # return para[0]
def on_del(para):
    global tree
    tree.dellist()
    # return para[0]
def on_edit(para):
    global tree
    tree.editlist()
    # return para[0]
def on_up(para):
    global tree
    tree.moveup()
    # return para[0]
def on_down(para):
    global tree
    tree.movedown()
    # return para[0]
def on_ed(para):
    global tree
    tree.changestate()
    # return para[0]
def on_edall(para):
    global tree
    tree.changall()
    # return para[0]
def on_zoom(para):
    print('--==zoom==--')
    # return para[0]

def demoedit(para):
    return 'edit demo'
def edit(para):
    mainwin=para['root']
    app=para['edit']
    # -------------      actions       -----------------
    _commit_action = mainwin.add_action("commit", "save", "Commit All Data", True, 'edit', 'commit')
    _revert_action = mainwin.add_action("revert", "open", "Revert From Last Commit", True, 'edit', 'revert')
    _clone_action = mainwin.add_action("clone", "copy", "Clone Selection", True, 'edit', 'clone')
    _delect_action = mainwin.add_action("delect", "paste", "Delect Selection", True, 'edit', 'del')
    # _edit_action = mainwin.add_action("edit", "copy", "Edit selection", True, 'edit', 'edit')
    _up_action = mainwin.add_action("moveup", "moveup", "Move Selection Up", True, 'edit', 'up')
    _down_action = mainwin.add_action("movedown", "movedown", "Move Selection Down", True, 'edit', 'down')
    _ed_action = mainwin.add_action("enable", "ed", "Enable or Disable Selection", True, 'edit', 'ed')
    _edall_action = mainwin.add_action("enableall", "edall", "Enable or Disable All", True, 'edit', 'edall')

    _zoom_action = mainwin.add_action("Zoom", "zoom", "Zoom in on document", True, 'edit', 'zoom')


    # -------------      Tab and Pane     -----------------
    home_tab = mainwin._ribbon.add_ribbon_tab("Edit")

    file_pane = home_tab.add_ribbon_pane("Data")

    # -------------      IconButton     -------------------
    file_pane.add_ribbon_widget(IconButton(mainwin, _commit_action, True))
    file_pane.add_ribbon_widget(IconButton(mainwin, _revert_action, True))
    # -------------     Pane            -------------------
    edit_panel = home_tab.add_ribbon_pane("Sequence")
    edit_panel.add_ribbon_widget(IconButton(mainwin, _clone_action, True))
    edit_panel.add_ribbon_widget(IconButton(mainwin, _delect_action, True))
    # edit_panel.add_ribbon_widget(IconButton(mainwin, _edit_action, True))
    edit_panel.add_ribbon_widget(IconButton(mainwin, _up_action, True))
    edit_panel.add_ribbon_widget(IconButton(mainwin, _down_action, True))
    edit_panel.add_ribbon_widget(IconButton(mainwin, _ed_action, True))
    edit_panel.add_ribbon_widget(IconButton(mainwin, _edall_action, True))

    # -------------     Pane            -------------------
    view_panel = home_tab.add_ribbon_pane("View")
    view_panel.add_ribbon_widget(IconButton(mainwin, _zoom_action, True))
    home_tab.add_spacer()

    # -------------     Dock            -------------------
    edittree(para)

    return 'edit build finish'

#>>>>>>>>有待其他地方复用插件系统>>>>>>>
def setup(app):
    app.register_guis('01uppercase', demoedit)

# 插件负责界面构建函数和注册响应事件函数(事件名称通过查询注册字典得到)
def build(app):
    app.register_guis('1000 edit', edit)
    app.register_events('revert', on_revert)
    app.register_events('commit', on_commit)
    app.register_events('clone', on_clone)
    app.register_events('del', on_del)
    # app.register_events('edit', on_edit)
    app.register_events('up', on_up)
    app.register_events('down', on_down)
    app.register_events('ed', on_ed)
    app.register_events('edall', on_edall)
    #
    app.register_events('zoom', on_zoom)

