# 负责对接插件系统
# 负责主体窗体构建
# 负责控件构建的公用部分，例如图标按键的add_acttion()

from PyQt5.QtCore import *
from PyQt5.QtGui import QKeySequence as QKSec
from Cmaster.Button import IconButton
from Cmaster.Textbox import Textbox

from Cmaster.Widget import *
from Cmaster.HCore import Config
from Cmaster.Icons import get_icon

from pluginbase import PluginBase
from functools import partial
import os
import logging

# os.path.join()：  将多个路径组合后返回
get_path = partial(os.path.join, os.getcwd()+'/Cmaster')
# 加入内建插件函数（应用app的plugins注册的函数内与内建的重名时会覆盖执行）
plugin_base = PluginBase(package='plugins',
                         searchpath=[get_path('./builtin_plugins')])
# 定义主体变量
main1para={}

class Builder(object):
    def __init__(self, name):
        # Each application has a name
        self.name = name
        # 插件字典做函数列表
        self.buildguis = {}
        self.events={}
        # 构造插件
        self.source = plugin_base.make_plugin_source(
            searchpath=[get_path('./%s/plugins' % name)],
            identifier=self.name)
        # 载入插件
        for plugin_name in self.source.list_plugins():
            plugin = self.source.load_plugin(plugin_name)
            plugin.build(self)  # 插件必须包含def build(app): 负责界面构建
        # 按名称寄存插件引用
        main1para[name]=self


    def register_guis(self, name, formatter):
        """A function a plugin can use to register a formatter."""
        self.buildguis[name] = formatter
    def register_events(self,eventlabel,eventfunc):
        self.events[eventlabel]=eventfunc
        return self

def run_builder(app):
    # 调试用，记录插件列表
    runlist=[]
    # 执行应用的插件函数内容
    logging.info('-=Runing%10s=-' % app.name)
    # 执行函数已排列
    for name, b in sorted(app.buildguis.items()):
        # 调试用，记录插件列表
        runlist.append(name)
        # 主执行函数
        b(main1para)
        # logging.info('%10s: %s' % (name, bfunc(source)))
    # 调试用，记录插件列表
    logging.info('==BuildList=='+str(runlist)) #打印已执行插件列表
def run_event(app,para):
    # 字典查询执行事件对应函数，并传递主体变量
    if app.events.__contains__(para):
        app.events.get(para)(main1para)
    else:
        logging.warning('NoRegister:%s'%para)

# 使用插件系统的主体
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.resize(1280, 800)
        self.setWindowTitle("Main Window %s"%Config.read_key('Main','Title','AutoMaster'))
        self.setDockNestingEnabled(True)
        self.setWindowIcon(get_icon("icon"))

        self._ribbon = Widget(self)
        self.addToolBar(self._ribbon)

        main1para['root'] = self
        # 由配置文件控制插件是所在目录及名称,home为初始app
        Config.read_key('Apps','home','1')
        for app in Config.ls_key('Apps'):
            run_builder(Builder(app))

    def add_action(self, caption, icon_name, status_tip, icon_visible, app_name,event_name, shortcut=None):
        "caption, icon_name, status_tip, icon_visible, app_name,event_name, shortcut=None"
        action = QAction(get_icon(icon_name), caption, self)
        action.setStatusTip(status_tip)
        action.triggered.connect(lambda :run_event(main1para[app_name],event_name))
        action.setIconVisibleInMenu(icon_visible)
        if shortcut is not None:
            action.setShortcuts(shortcut)
        self.addAction(action)
        return action


    # def closeEvent(self, close_event):
    #     pass




