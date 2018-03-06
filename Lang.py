# 语言规则：全小写的英文作为标签，翻译对应的中文和英文
# 负责界面ui文件到处理，并自动在调用脚本中自动增加对应控件资源loui
# 负责界面语言切换
# 负责内核语言在线切换
# 使用工厂设计模式，实现对象创建在子类
# 新增语言：新增dict(EN=ENLang, CN=CNLang,JP=JPLang),复制class ENLang修改类名称，外部字典名称，修改内置字典即可

import CoreConfig
import lxml
import InsertString

# 读取当前配置语言
lonow=CoreConfig.read_ini("Config","language")

# 定义语言切换函数
def lolang(lang=lonow):
    languages = dict(EN=ENLang, CN=CNLang)
    return languages[lang]()
# 定义界面语言切换函数，修改xml的ui文件
def loui(fname,lang=lonow):
    uiname=CoreConfig.checkui(fname)
    #导入自定义的IDE"自动插入字符串"模块InsertString
    # from Master import InsertString
    lo=lolang(lang)
    xmlf=lxml.etree.parse(uiname) #######################################CHJ
    #翻译窗口标题windowTitle
    findcond = '//property[@name="windowTitle"]/string'
    gettitle = xmlf.xpath(findcond)
    for t in gettitle:
        t.text = lo.get(t.text)
    #定义需翻译的控件类class及对应标签tag
    findclass=['QPushButton','QLabel','QComboBox']
    findtag=['toolTip','text']
    # 自动IDE的信号connect和传递参数
    findcond = '//connection/sender'
    getsend = xmlf.xpath(findcond)
    findcond = '//connection/signal'
    getsign = xmlf.xpath(findcond)
    findcond = '//connection/receiver'
    getrece = xmlf.xpath(findcond)
    for i, sign in enumerate(getsign):
        inst = getsend[i].text + '.' + sign.text[:sign.text.find("(")]
        mkevent = '''self.%s.connect(lambda:self.Event('demo','%s'))''' % (inst, getrece[i].text)
        InsertString.str2file(mkevent, "# AutoC\n")
        mkreg = '''"%s":self.%s,''' % (getrece[i].text, getrece[i].text)
        InsertString.str2file(mkreg, "# AutoH\n")
    for ic in findclass:
        #自动IDE处理按钮的单击connect
        if ic =='QPushButton':
            findcond = '//widget[@class="%s"]/@name' %ic
            getclass = xmlf.xpath(findcond)
            for inst in getclass:
                mkevent='''self.%s.clicked.connect(lambda:self.Event('demo'))'''%inst
                InsertString.str2file(mkevent)
        #界面控件字符串翻译
        for jt in findtag:
            findcond='//widget[@class="%s"]//property[@name="%s"]/string'%(ic,jt)
            getclass=xmlf.xpath(findcond)
            print(len(getclass),"翻译 >%s >%s" % (ic, jt))
            for t in getclass:
                try:
                    t.text=lo.get(t.text)
                except Exception as e:
                    print("Warning[%s] >%s >%s"%(e,ic,jt))

    #更新缓存文件，新ui文件为后缀加lo
    tempui=uiname+'lo'
    xmlf.write(tempui)
    return tempui

class CNLang:
    #中文语言字典
    def __init__(self):
        # 定义外部字典，有外部字典优先外部字典
        dictfile = CoreConfig.lang + '/Chinese.txt'
        try:
            f = open(dictfile, 'r')
            a = f.read()
            self.trans = eval(a)
            f.close()
        except IOError:
        #内置字典文件，重新生成字典文件
            self.trans = dict(ScriptError=u"脚本错误！", Error=u"错误！",NotFound=u"找不到")
            f = open(dictfile, 'w')
            f.write(str(self.trans))
            f.close()
        except Exception as e:
            raise (e)

    def get(self, msgid):
        try:
            return self.trans[msgid]
        except Exception as e:
            print("Warning[字典不存在] %s" % msgid)
            return str(msgid)


class ENLang:
    #  英文处理字段空格和标点符号
    def __init__(self):
        # 定义外部字典，有外部字典优先外部字典
        dictfile = CoreConfig.lang + '/English.txt'
        try:
            f = open(dictfile, 'r')
            a = f.read()
            self.trans = eval(a)
            f.close()
        except IOError:
        #内置字典文件，重新生成字典文件
            self.trans = dict(ScriptError=u"Script Error！", Error=u"Error！",NotFound=u"Not Found")
            f = open(dictfile, 'w')
            f.write(str(self.trans))
            f.close()
        except Exception as e:
            raise (e)
    def get(self, msgid):
        try:
            return self.trans[msgid]

        except Exception as e:
            print("Warning[Not Dict] %s" % msgid)
            return str(msgid)


