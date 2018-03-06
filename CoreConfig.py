#负责系统执行路径，存储路径变量maindir
#负责内部使用的参数
#负责构建整个项目的路径结构（文件夹）
#负责配置文件的寄存量定义

import configparser
import sys
import os
#导入依赖py2app调试
import numpy
import lxml
# import etree

#判断执行环境得到当前执行文件的相对路径
frozen = 'not'
if getattr(sys, 'frozen', False):
    # we are running in a bundle
    frozen = 'ever so'
    maindir = os.path.dirname(sys.executable)

else:
    # we are running in a normal Python environment
    maindir = os.path.dirname(os.path.abspath(__file__))
    # 编辑环境下，增加IDE协助脚本到环境变量
sys.path.append(maindir + '/IDE')
print('根路径',maindir)
#增加Core文件夹到系统环境路径变量
sys.path.append(maindir + '/Core')
#增加UI文件夹到系统环境路径变量
sys.path.append(maindir + '/UI')
#配置语言文件夹
if (not os.path.exists(maindir+"/Language")):
    os.mkdir(maindir+"/Language",0o777)
lang=maindir+"/Language"
print('语言路径',lang)
# 外部配置文件inifile
inifile=maindir+'/Config/Core.ini'
configpath = maindir + "/Config"
if (not os.path.exists(configpath)):
    os.mkdir(maindir+"/Config",0o777)
if (not os.path.exists(inifile)):
    inif=open(inifile, "w")
    inif.close()
#检查环境中的ui界面
def checkui(name):
    #在以下位置搜索ui文件，并返回绝对路径，checkli中前面优先
    checkli=[maindir + '/UI/'+name,maindir +'/'+ name,maindir + '/IDE/'+name]
    for ret in checkli:
        if os.path.exists(ret):
            return ret
            # break


def read_ini(section, key):
    cf = configparser.ConfigParser()
    cf.read(inifile)
    value = cf.get(section, key)
    return value

def write_ini(section, key, value):

    cf = configparser.ConfigParser()
    cf.read(inifile)
    if (not cf.has_section(section)):
        cf.add_section(section)
        print("Warning[NewSection]"+section)
    cf.set(section, key, value)
    # write to file
    cf.write(open(inifile, "w"))

#定义项目当前语言(防呆初始值为CN),定义是否记录登陆用户（Ture）
try:
    read_ini('Config',"language")
    read_ini('Config','saveuser')
except:
    write_ini('Config',"language","CN")
    write_ini('Config','saveuser','True')

# 配置外部执行脚本的路径
try:
    scrname=read_ini("Config","scrname")
except:
    scrname="sample.py"
    write_ini('Config', "scrname", scrname)
scr= maindir + '/Scripts/'+scrname
# 自动新建脚本范例（程序防呆）
if (not os.path.exists(maindir+"/Scripts")):
    print("ERROR[Scripts not exists]")
    os.mkdir(maindir+"/Scripts",0o777)
if (not os.path.exists(scr)):
    scrf=open(scr, "w")
    scrf.write("#执行脚本编写在该py文件\n")
    scrf.write(u"print('sample of script')")
    scrf.close()