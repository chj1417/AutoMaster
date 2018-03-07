# -*- coding: utf-8 -*-
import configparser
import os
import sys
import logging
import JCheck
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
inifile=maindir+'/bin/CoreConfig.ini'

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
def check_ini(section,key,value):
    if (not os.path.exists(inifile)):
        inif = open(inifile, "w")
        inif.close()
    cf = configparser.ConfigParser()
    cf.read(inifile)
    if (not cf.has_option(section,key)):
        if (not cf.has_section(section)):
            cf.add_section(section)
        cf.set(section,key,value)
        if value!='':
            cf.write(open(inifile, "w"))
        logging.warning("[NewConfig %s ] %s ='%s'" %(section,key,value))
    return cf

def read_ini(section, key,value=''):
    # 键key不存在且有传递value非空的时候，进行写入文件操作
    cf=check_ini(section,key,value)
    value = cf.get(section, key)
    return value

def write_ini(section, key, value):
    cf=check_ini(section,key,'')
    cf.set(section, key, value)
    # write to file
    cf.write(open(inifile, "w"))

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
        logging.error('app1 and app2 '+str(e))
    # Run the demo for both
    try:
        run_demo(app1, source)
    except Exception as e:
        logging.error('demo1 '+str(e))
    try:
        run_demo(app2, source)
    except Exception as e:
        logging.error('demo2 ' + str(e))
    # And just to show how the import system works, we also showcase
    # importing plugins regularly:

    # with app1.source:
    #     from plugins import secret
    #     print('Plugin module: %s' % secret)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    # app.setQuitOnLastWindowClosed(True)
    # python版本信息
    logging.warning('====version  '+str(sys.version_info[0])+'=====')
    # 以下为该项目的执行模块配置,注意区分模块名称>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 导入登陆模块
    from Login1 import LoadWin as l1
    from Login2 import LoadWin as l2
    # 导入向导模块
    # from LangManTool import LoadWin as r2
    # 导入主体模块
    from GUI.MainWindow import MainWindow as m1
    # 模块列表
    modlels=[
        #登陆模块
        [l1,l2],
        #向导模块
        [l1, l2],
        #主体模块
        [m1,l2]
    ]
    # 名称列表
    m_names=['Login','Guide','Main']
    # 标签列表
    m_lables=['loginwin','guidewin','mainwin']
    # 执行条件列表
    m_condition=[1,'loginok',1]

    # 模块配置文件初始化
    runmodle=[]
    for i,mns in enumerate(m_names):
        write_ini('Core','%s-Style'%mns,'Null or 0 to %d'%(len(modlels[i])-1))
        write_ini('Core','%s-Lable'%mns,m_lables[i])
        if read_ini('Core', '%s-Next'%mns)=='':
            write_ini('Core', '%s-Next'%mns,'') # 空键值也要保留在Core中
        configstr=read_ini('Running', mns, '0') #获取模块style配置，初始值为执行0主题
        if configstr!='':
            # Running中键值非空则执行
            temp2run=[]
            temp2run.append(modlels[i][int(configstr)]) # 对应导入模块的modlels[][]
            temp2run.append(1) # 是否等待该模块结束才执行下一模块
            temp2run.append(m_condition[i]) # 执行条件，传递参数到condition函数的para中
            temp2run.append(m_lables[i]) # 当前模块标签
            temp2run.append(read_ini('Core', '%s-Next'%mns)) #跳转模块标签
            # 执行列表[模块名称class,等待结束bool，执行条para,标签，跳转标签
            runmodle.append(temp2run)

    # 中间函数，定义条件执行case>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def condition(para):
        if para == 'loginok':
            # 查询登陆状态
            return JCheck.check().login
        else:
            # print(type(para),para)
            return para

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
                    try:
                        cango = m.exec_()
                    except Exception as e:
                        logging.error(str(e))
            except Exception as e:
                logging.error(str(e))
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
                if index>=len(runmodle):
                    break
            else:
                try:
                    index = taskname.index(tasknow[4])
                except ValueError as e:
                    logging.error(str(e))
        else:
            break
    # 执行功能主体
    # main()
    # main_window = m1()
    # main_window.show()
    # main_window.exec_()
    # 关闭项目
    sys.exit(app.exec())


