# from PyQt5 import QtWidgets, QtCore

from PyQt5.QtCore import *
from PyQt5.QtGui import QKeySequence as QKSec
from Cmaster.Button import IconButton
from Cmaster.Icons import get_icon
from Cmaster.Textbox import Textbox
from Cmaster.Widget import *
from Cmaster.HCore import Config

from pluginbase import PluginBase
from functools import partial
import os
import logging

#
get_path = partial(os.path.join, os.getcwd()+'/Cmaster')
# 加入内建插件函数（应用app的plugins注册的函数内与内建的重名时会覆盖执行）
plugin_base = PluginBase(package='plugins',
                         searchpath=[get_path('./builtin_plugins')])

class Builder(object):
    def __init__(self, name):
        # Each application has a name
        self.name = name

        # And a dictionary where it stores "formatters".  These will be
        # functions provided by plugins which format strings.
        self.formatters = {}
        self.events={}
        self.source = plugin_base.make_plugin_source(
            searchpath=[get_path('./%s/plugins' % name)],
            identifier=self.name)

        for plugin_name in self.source.list_plugins():
            plugin = self.source.load_plugin(plugin_name)
            plugin.build(self)  # 插件必须包含def build(app): 负责界面构建

    def register_formatter(self, name, formatter):
        """A function a plugin can use to register a formatter."""
        self.formatters[name] = formatter
    def register_events(self,eventlabel,eventfunc):
        self.events[eventlabel]=eventfunc
        return self

def run_builder(app, source):
    runlist=[]
    # 执行应用的插件函数内容
    logging.info('runing %s:' % app.name)
    # 执行函数已排列
    for name, bfunc in sorted(app.formatters.items()):
        runlist.append(name)
        #主执行函数
        logging.info('  %10s: %s' % (name, bfunc(source)))

    logging.info('=====>'+str(runlist)) #打印换行
def run_event(app,para):
    # print('running event')
    if app.events.__contains__(para):
        print('has key----',para)
        e2run=app.events.get(para)
        e2run('o my event')
    else:
        print('nothing')




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.resize(1280, 800)
        self.setWindowTitle("Main Window %s"%Config.read_ini('Main','Title','AutoMaster'))
        self.setDockNestingEnabled(True)
        self.setWindowIcon(get_icon("icon"))

        self._main_dock2_widget = QDockWidget(self)
        self._main_dock2_widget.setObjectName("Dock2");
        self._main_dock2_widget.setWindowTitle("dock2")
        self.addDockWidget(Qt.RightDockWidgetArea, self._main_dock2_widget)
        #
        self._main_dock_widget = QDockWidget(self)
        self._main_dock_widget.setObjectName("MainDock");
        self._main_dock_widget.setWindowTitle("Main dock")
        self.addDockWidget(Qt.LeftDockWidgetArea, self._main_dock_widget)
        self.centralWidget()

        app1 = Builder('about')
        # run_event(app1,'nothing')


        # -------------      actions       -----------------

        self._open_action = self.add_action("Open", "open", "Open file", True, [app1,'about'], QKSec.Open)
        # self._save_action = self.add_action("Save", "save", "Save file", True, self.on_save, QKSec.Save)
        # self._copy_action = self.add_action("Copy", "copy", "Copy selection", True, self.on_copy, QKSec.Copy)
        # self._paste_action = self.add_action("Paste", "paste", "Paste from clipboard", True, self.on_paste, QKSec.Paste)
        # self._zoom_action = self.add_action("Zoom", "zoom", "Zoom in on document", True, self.on_zoom)


        # -------------      textboxes       -----------------

        self._text_box1 = Textbox("Text 1", self.on_text_box1_changed, 80)
        self._text_box2 = Textbox("Text 2", self.on_text_box1_changed, 80)
        self._text_box3 = Textbox("Text 3", self.on_text_box1_changed, 80)

        # Ribbon
        # print(self)
        self._ribbon = Widget(self)
        self.addToolBar(self._ribbon)
        self.init_ribbon()

        run_builder(app1, [self, app1])

    def add_action(self, caption, icon_name, status_tip, icon_visible, connection, shortcut=None):
        action = QAction(get_icon(icon_name), caption, self)
        action.setStatusTip(status_tip)
        action.triggered.connect(lambda :run_event(connection[0],connection[1]))
        action.setIconVisibleInMenu(icon_visible)
        if shortcut is not None:
            action.setShortcuts(shortcut)
        self.addAction(action)
        return action

    def init_ribbon(self):
        home_tab = self._ribbon.add_ribbon_tab("Home")
        file_pane = home_tab.add_ribbon_pane("File")
        file_pane.add_ribbon_widget(IconButton(self, self._open_action, True))
        # file_pane.add_ribbon_widget(IconButton(self, self._save_action, True))

        edit_panel = home_tab.add_ribbon_pane("Edit")
        # edit_panel.add_ribbon_widget(IconButton(self, self._copy_action, True))
        # edit_panel.add_ribbon_widget(IconButton(self, self._paste_action, True))
        grid = edit_panel.add_grid_widget(200)
        grid.addWidget(QLabel("Text box 1"), 1, 1)
        grid.addWidget(QLabel("Text box 2"), 2, 1)
        grid.addWidget(QLabel("Text box 3"), 3, 1)
        grid.addWidget(self._text_box1, 1, 2)
        grid.addWidget(self._text_box2, 2, 2)
        grid.addWidget(self._text_box3, 3, 2)

        view_panel = home_tab.add_ribbon_pane("View")
        # view_panel.add_ribbon_widget(IconButton(self, self._zoom_action, True))
        home_tab.add_spacer()

        # print(self,'----')

    # def closeEvent(self, close_event):
    #     pass

    def on_open_file(self):
        pass
        print('open')

    def on_save_to_excel(self):
        pass
        print('save2excel')

    def on_save(self):
        pass
        print('save')

    def on_text_box1_changed(self):
        pass

    def on_text_box2_changed(self):
        pass

    def on_text_box3_changed(self):
        pass

    def on_copy(self):
        pass
        print('copy')

    def on_paste(self):
        pass
        print('paste')

    def on_zoom(self):
        pass


