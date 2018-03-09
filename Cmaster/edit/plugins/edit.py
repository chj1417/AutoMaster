# -*- coding: utf-8 -*-
# 插件内容
# 负责构建界面
# 负责定义构建的界面可能的事件函数

# 快捷键模块
from PyQt5.QtGui import QKeySequence as QKSec

# 导入界面常用模块，Qlable可从该模块导入
from Cmaster.Widget import *
# Testbox输入框控件模块
from Cmaster.Textbox import Textbox
# IconButtom图形按钮模块
from Cmaster.Button import IconButton


# 定义事件函数>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def on_open(para):
    print('--==open==--')
    # return para[0]
def on_save(para):
    print('--==save==--')
    # return para[0]
def on_copy(para):
    print('--==copy==--')
    # return para[0]
def on_paste(para):
    print('--==paste==--')
    # return para[0]
def on_zoom(para):
    print('--==zoom==--')
    # return para[0]
#----test box changed -----
def on_textbox1_changed(para):
    print('--==textbox1==--')
    # return para[0]

def on_textbox2_changed(para):
    print('--==textbox2==--')
    # return para[0]

def on_textbox3_changed(para):
    print('--==textbox3==--')
    # return para[0]

def demoedit(para):
    return 'edit demo'
def edit(para):
    mainwin=para['root']
    app=para['edit']
    # -------------      actions       -----------------
    _open_action = mainwin.add_action("Open", "open", "Open file", True, 'edit', 'open', QKSec.Open)
    _save_action = mainwin.add_action("Save", "save", "Save file", True, 'edit', 'save', QKSec.Save)
    _copy_action = mainwin.add_action("Copy", "copy", "Copy selection", True, 'edit', 'copy', QKSec.Copy)
    _paste_action = mainwin.add_action("Paste", "paste", "Paste from clipboard", True, 'edit', 'paste', QKSec.Paste)
    _zoom_action = mainwin.add_action("Zoom", "zoom", "Zoom in on document", True, 'edit', 'zoom')

    # ------ textboxes  其changed事件是直接传递了 ------------

    _text_box1 = Textbox("Text 1", on_textbox1_changed, 80)
    _text_box2 = Textbox("Text 2", on_textbox2_changed, 80)
    _text_box3 = Textbox("Text 3", on_textbox3_changed, 80)

    # -------------      Tab and Pane     -----------------
    home_tab = mainwin._ribbon.add_ribbon_tab("Edit")
    file_pane = home_tab.add_ribbon_pane("File")

    # -------------      IconButton     -------------------
    file_pane.add_ribbon_widget(IconButton(mainwin, _open_action, True))
    file_pane.add_ribbon_widget(IconButton(mainwin, _save_action, True))
    # -------------     Pane            -------------------
    edit_panel = home_tab.add_ribbon_pane("Edit")
    edit_panel.add_ribbon_widget(IconButton(mainwin, _copy_action, True))
    edit_panel.add_ribbon_widget(IconButton(mainwin, _paste_action, True))
    # -------------     GridWidget      -------------------
    grid = edit_panel.add_grid_widget(200)
    grid.addWidget(QLabel("Text box 1"), 1, 1)
    grid.addWidget(QLabel("Text box 2"), 2, 1)
    grid.addWidget(QLabel("Text box 3"), 3, 1)
    grid.addWidget(_text_box1, 1, 2)
    grid.addWidget(_text_box2, 2, 2)
    grid.addWidget(_text_box3, 3, 2)
    # -------------     Pane            -------------------
    view_panel = home_tab.add_ribbon_pane("View")
    view_panel.add_ribbon_widget(IconButton(mainwin, _zoom_action, True))
    home_tab.add_spacer()

    return 'edit build finish'

#>>>>>>>>有待其他地方复用插件系统>>>>>>>
def setup(app):
    app.register_guis('01uppercase', demoedit)

# 插件负责界面构建函数和注册响应事件函数(事件名称通过查询注册字典得到)
def build(app):
    app.register_guis('1000 edit', edit)
    app.register_events('open', on_open)
    app.register_events('save', on_save)
    app.register_events('copy', on_copy)
    app.register_events('paste', on_paste)
    app.register_events('zoom', on_zoom)
    #textbox1_changed
    # app.register_events('textbox1_changed', on_textbox1_changed)
    # app.register_events('textbox2_changed', on_textbox2_changed)
    # app.register_events('textbox3_changed', on_textbox3_changed)

