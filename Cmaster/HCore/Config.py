# 负责配置参数
import configparser
import os
import logging

maindir=os.getcwd()
inifile=maindir+'/bin/CoreConfig.ini'

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

def read_key(section, key,value=''):
    # 键key不存在且有传递value非空的时候，进行写入文件操作
    cf=check_ini(section,key,value)
    value = cf.get(section, key)
    return value

def write_key(section, key, value):
    cf=check_ini(section,key,'')
    cf.set(section, key, value)
    # write to file
    cf.write(open(inifile, "w"))

def ls_key(section):
    cf=configparser.ConfigParser()
    cf.read(inifile)
    if (not cf.has_section(section)):
        cf.add_section(section)
        cf.write(open(inifile, "w"))
        logging.warning("[NewConfig %s ]" %section)
    return cf.options(section)