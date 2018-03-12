# -*- coding: utf-8 -*-
# 程序入口
# 负责框架的搭建
# 负责框架功能的增添，需要编译的代码包含
# 负责依赖的包含

import configparser
import os
import sys
import logging
import JCheck
from PyQt5 import QtWidgets
from Hinclude import *

# from PyQt5.QtCore import QTranslator


# 引入日志系统
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[%(funcName)s:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%d,%H:%M:%S',
                filename='TestLog.log',
                filemode='w',
                    )
# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# AutoMaster项目执行环境工作路径可作为相对路径使用
maindir=os.getcwd()
here = maindir + '/Cmaster'
sys.path.append(here)
inifile=maindir+'/bin/CoreConfig.ini'

def check_ini(section,key,value):
    if (not os.path.exists(inifile)):
        inif = open(inifile, "w",encoding='UTF-8')
        inif.close()
    cf = configparser.ConfigParser()
    cf.read(inifile,encoding='UTF-8')
    if (not cf.has_option(section,key)):
        if (not cf.has_section(section)):
            cf.add_section(section)
        cf.set(section,key,value)
        if value!='':
            cf.write(open(inifile, "w",encoding='UTF-8'))
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

if __name__ == '__main__':
    #去除警告
    QtWidgets.QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    # 寄存系统指令
    _sys_argv=sys.argv
    app = QtWidgets.QApplication(_sys_argv)
    for i,cmd in enumerate(_sys_argv):
        write_ini('Sys','cmd%s'%i,str(cmd))
    # 语言国际化，CHJ试验失败，暂不知如何使用
    # trans = QTranslator()
    # trans.load("./bin/zh_CN") # 没有后缀.qm
    # app.installTranslator(trans)


    # app.setQuitOnLastWindowClosed(True)
    # python版本信息
    logging.info('***version %s***'%str(sys.version_info[0]))
    # 以下为该项目的执行模块配置,注意区分模块名称>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 导入登陆模块
    from Login1 import LoadWin as l1
    from Login2 import LoadWin as l2
    # 导入向导模块
    # from LangManTool import LoadWin as r2
    # 导入主体模块

    from Cmaster.Main1 import MainWindow as m1
    # 模块列表
    modlels=[
        #登陆模块
        [l1,l2],
        #向导模块
        [l1, l2],
        #主体模块
        [m1,]
    ]
    # 名称列表
    m_names=['Login','Guide','Main']
    # 标签列表
    m_lables=['loginwin','guidewin','mainwin']
    # 执行条件列表
    m_condition=[1,'loginok',1]
    # 模块配置文件初始化
    runmodle=[]
    try:
        for i,mns in enumerate(m_names):
            try:
                write_ini('Core','%s-Style'%mns,'Null or 0 to %d'%(len(modlels[i])-1))
                write_ini('Core','%s-Lable'%mns,m_lables[i])
            except Exception as e:
                logging.error('ini'+str(e))
            if read_ini('Core', '%s-Next'%mns)=='':
                write_ini('Core', '%s-Next'%mns,'') # 空键值也要保留在Core中
            configstr=read_ini('Running', mns, '0') #获取模块style配置，初始值为执行0主题
            if configstr!='':
                try:
                    # Running中键值非空则执行
                    temp2run=[]
                    temp2run.append(modlels[i][int(configstr)]) # 对应导入模块的modlels[][]
                    temp2run.append(1) # 是否等待该模块结束才执行下一模块
                    temp2run.append(m_condition[i]) # 执行条件，传递参数到condition函数的para中
                    temp2run.append(m_lables[i]) # 当前模块标签
                    temp2run.append(read_ini('Core', '%s-Next'%mns)) #跳转模块标签
                    # 执行列表[模块名称class,等待结束bool，执行条para,标签，跳转标签
                    runmodle.append(temp2run)
                except Exception as e:
                    logging.error('temp2run'+str(e))
    except Exception as e:
        logging.error(e)
    finally:
        logging.info('Loading Success')
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
    _need_appexec=False
    while 1:
        # logging.info('running into while index=%s'%index)
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
                    except AttributeError:
                        # 窗体不存在exec的需要app的exec来阻塞，例如Main1不阻塞界面显示就关闭来
                        _need_appexec=True
                    except Exception as e:
                        logging.error(e)
            except AttributeError:
                # 直接pyuic不存在show的界面使用setupUI
                QDialog=QtWidgets.QDialog()
                m.setupUi(QDialog)
                QDialog.show()
                if tasknow[1]:
                    # 使用exec_进行等待阻塞
                    cango = QDialog.exec_()
                    pass
            except Exception as e:
                logging.error(e)
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
    # 关闭项目
    if _need_appexec:
        sys.exit(app.exec())
    else:
        sys.exit()


