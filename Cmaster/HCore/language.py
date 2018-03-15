# 语言规则：全小写的英文作为标签，翻译对应的中文和英文
# 负责内核语言在线切换
# 使用工厂设计模式，实现对象创建在子类
# 新增语言：新增dict(EN=ENLang, CN=CNLang,JP=JPLang),复制class ENLang修改类名称，外部字典名称，修改内置字典即可

from Cmaster.HCore import Config
import logging

# 读取当前配置语言
Config.write_key('Config','Languages','EN,CN')
lonow=Config.read_key("Config","Lang","CN")

# 定义语言切换函数
def lolang(lang=lonow):
    languages = dict(EN=ENLang, CN=CNLang)
    return languages[lang]()

class CNLang:
    #中文语言字典
    def __init__(self):
        # 定义外部字典，有外部字典优先外部字典
        dictfile = './bin/Chinese.txt'
        try:
            f = open(dictfile, 'r',encoding='utf-8')
            a = f.read()
            self.trans = eval(a)
            f.close()
        except IOError:
        #内置字典文件，重新生成字典文件
            self.trans = dict(Error=u"错误！",NotFound=u"找不到")
            f = open(dictfile, 'w',encoding='utf-8')
            f.write(str(self.trans))
            f.close()
        except Exception as e:
            raise (e)

    def get(self, msgid):
        try:
            return self.trans[msgid]
        except Exception as e:
            logging.warning('Language Dict NotFound %s'%msgid)
            return str(msgid)


class ENLang:
    #  英文处理字段空格和标点符号
    def __init__(self):
        # 定义外部字典，有外部字典优先外部字典
        dictfile = './bin/English.txt'
        try:
            f = open(dictfile, 'r',encoding='utf-8')
            a = f.read()
            self.trans = eval(a)
            f.close()
        except IOError:
        #内置字典文件，重新生成字典文件
            self.trans = dict(Error=u"Error！",NotFound=u"Not Found")
            f = open(dictfile, 'w',encoding='utf-8')
            f.write(str(self.trans))
            f.close()
        except Exception as e:
            raise (e)
    def get(self, msgid):
        try:
            return self.trans[msgid]

        except Exception as e:
            logging.warning('Language Dict NotFound %s'%msgid)
            return str(msgid)


