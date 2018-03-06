# -*- coding: utf-8 -*-
import os
import sys
import logging
from PyQt5 import QtWidgets

from functools import partial
from pluginbase import PluginBase

#
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[%(funcName)s:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%d,%H:%M:%S',
                filename='TestLog.log',
                filemode='w',
                    )
#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

# logging.basicConfig(filename='TestLog.log', level=logging.DEBUG,datefmt='%d %H:%M:%S')
# logging.Formatter(fmt=None, datefmt=None)

# AutoMaster项目执行环境工作路径可作为相对路径使用
maindir=os.getcwd()
here = maindir + '/Cmaster'
sys.path.append(here)

get_path = partial(os.path.join, here)
# 注意："app_name/plugins"和'./builtin_plugins'文件夹内不允许非插件规格的py文件，其他后缀可以
# 插件规范，必须包含def setup(app): 函数定义

# Setup a plugin base for "example.modules" and make sure to load
# all the default built-in plugins from the builtin_plugins folder.
# 加入内建插件函数（应用app的plugins注册的函数内与内建的重名时会覆盖执行）
plugin_base = PluginBase(package='plugins',
                         searchpath=[get_path('./builtin_plugins')])
#
for pathnow in sys.path:
    logging.info(pathnow)

class Application(object):
    """Represents a simple example application."""

    def __init__(self, name):
        # Each application has a name
        self.name = name

        # And a dictionary where it stores "formatters".  These will be
        # functions provided by plugins which format strings.
        self.formatters = {}

        # and a source which loads the plugins from the "app_name/plugins"
        # folder.  We also pass the application name as identifier.  This
        # is optional but by doing this out plugins have consistent
        # internal module names which allows pickle to work.

        self.source = plugin_base.make_plugin_source(
            searchpath=[get_path('./%s/plugins' % name)],
            identifier=self.name)

        # Here we list all the plugins the source knows about, load them
        # and the use the "setup" function provided by the plugin to
        # initialize the plugin.
        for plugin_name in self.source.list_plugins():
            plugin = self.source.load_plugin(plugin_name)
            plugin.setup(self) #插件必须包含def setup(app): 函数定义

    def register_formatter(self, name, formatter):
        """A function a plugin can use to register a formatter."""
        self.formatters[name] = formatter


def run_demo(app, source):
    runlist=[]
    # 执行应用的插件函数内容
    """Shows all formatters in demo mode of an application."""
    logging.info('runing %s:' % app.name)
    # print(app.formatters.items())
    # 排列了，注意插件里面setup的名称，例如增加0001，0002即可控制执行顺序
    for name, fmt in sorted(app.formatters.items()):
        runlist.append(name)
        #主执行函数
        logging.info('  %10s: %s' % (name, fmt(source)))

    logging.info('=====>'+str(runlist)) #打印换行


def main():
    logging.info('[maindir]' + str(maindir))

    # 顺序执行的主函数主体
    # This is the demo string we want to format.
    source = ['This is a cool demo text to show this functionality.','ok']

    # Set up two applications.  One loads plugins from ./app1/plugins
    # and the second one from ./app2/plugins.  Both will also load
    # the default ./builtin_plugins.
    # 注意文件夹名称
    try:
        pass
        app1 = Application('app1')
        app2 = Application('app2')
    except Exception as e:
        logging.warning('app1 and app2 '+str(e))
    # Run the demo for both
    try:
        run_demo(app1, source)
    except Exception as e:
        logging.warning('demo1 '+str(e))
    try:
        run_demo(app2, source)
    except Exception as e:
        logging.warning('demo2 ' + str(e))
    # And just to show how the import system works, we also showcase
    # importing plugins regularly:

    # with app1.source:
    #     from plugins import secret
    #     print('Plugin module: %s' % secret)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    # python版本信息
    logging.warning('====version  '+str(sys.version_info[0])+'=====')
    # 以下为该项目的执行模块配置,注意区分模块名称>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 导入登陆模块
    from Login import LoadWin as r1
    # 导入
    # from LangManTool import LoadWin as r2


    # 中间函数，定义条件执行case>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def condition(para):
        if para == 'loginok':
            # print(StrCheck.check().login)
            # return StrCheck.check().login
            return 1
        else:
            # print(type(para),para)
            return para


    # 定义执行模块,[#执行列表[模块名称class,等待结束bool，执行条para,标签，跳转标签],,,]>>>>>>>>>>>>>
    runmodle = [
        [r1, 1, 1, 'loginwin', ''],
        # [r2, 1, 'loginok', '主界面', ''],  # 序列模式
        # [r2,1,'loginok','主界面','登陆界面'], #回转模式
        # [r1,1, 1,'其他界面',''], #序列模式demo加

    ]
    # 链式执行方式
    index = 0
    while 1:
        taskname = []
        for task in runmodle:
            taskname.append(task[3])
        tasknow = runmodle[index]
        cango = 0
        if condition(tasknow[2]):
            m = tasknow[0]()
            try:
                m.show()
                if tasknow[1]:
                    # 使用exec_进行等待阻塞
                    cango = m.exec_()
            except:
                QDialog=QtWidgets.QDialog()
                m.setupUi(QDialog)
                QDialog.show()
                if tasknow[1]:
                    # 使用exec_进行等待阻塞
                    cango = QDialog.exec_()

        # 接管窗口close函数的cango=1，使用esc或直接关闭窗体cango=0
        if cango:
            if tasknow[4] == '':
                index += 1
            else:
                try:
                    index = taskname.index(tasknow[4])
                except ValueError as e:
                    logging.error(str(e))
        else:
            break
    # 关闭项目
    main()


