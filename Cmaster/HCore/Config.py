# 负责配置参数
import configparser
import os
import logging
import codecs

maindir=os.getcwd()
inifile=maindir+'/bin/CoreConfig.ini'

def check_ini(section,key,value):
    if (not os.path.exists(inifile)):
        # inif = open(inifile, "w")
        # inif.close()
        # 使用好的打开方式
        codecs.open(inifile, 'w', 'utf-8')
    cf = configparser.ConfigParser()
    cf.read(inifile)
    if (not cf.has_option(section,key)):
        if (not cf.has_section(section)):
            cf.add_section(section)
        cf.set(section,key,value)
        if value!='':
            cf.write(codecs.open(inifile, 'w', 'utf-8'))
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
    cf.write(codecs.open(inifile, 'w', 'utf-8'))

def ls_key(section):
    cf=configparser.ConfigParser()
    cf.read(inifile)
    if (not cf.has_section(section)):
        cf.add_section(section)
        cf.write(codecs.open(inifile, 'w', 'utf-8'))
        logging.warning("[NewConfig %s ]" %section)
    return cf.options(section)