# -*- coding: utf-8 -*-
import os
import sys
import logging
from PyQt5 import QtWidgets

from functools import partial
from pluginbase import PluginBase

#
logging.basicConfig(filename='TestLog.log', level=logging.DEBUG)
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
    # 执行应用的插件函数内容
    """Shows all formatters in demo mode of an application."""
    logging.info('exec %s:' % app.name)
    # print(app.formatters.items())
    # 排列了，注意插件里面setup的名称，例如增加0001，0002即可控制执行顺序
    for name, fmt in sorted(app.formatters.items()):
        #主执行函数
        logging.info('  %10s: %s' % (name, fmt(source)))

    logging.info('') #打印换行


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
    logging.warning('====version  '+str(sys.version_info[0])+'=====')

    main()


