# 简化所有的提示和消息窗口
# 负责各种信息提示窗口
# 内置语言
# 负责简单的输入窗口
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from numpy import unicode
import Lang
import sys
import os
import CoreConfig

#实例化语言，语言参数默认即为Core配置中的语言
lo=Lang.lolang()
def input(title,last=""):
# 输入窗，窗体比较简单，由本模块代码构建class Dlg(QDialog)
    add = Dlg(lo.get(title),last)
    if add.exec_():
         return add.word
def openfile(samplefile):
# 传入文件Sample路径，跳转到同级位置open同类文件，Return[绝对文件路径，文件名称，文件后缀，文件位置路径]
    p, f = os.path.split(samplefile)
    f, ext = os.path.splitext(samplefile)
    #该出有异常提示objc[8783]百度为mac系统问题
    file = QFileDialog.getOpenFileName(None, lo.get("openfiledialog"), p, "OnlyFiles(*%s)"%ext)
    filepath, extname = os.path.splitext(file[0])
    path, name = os.path.split(filepath)
    return file[0],name,extname,path
def openfiles(samplefile):
# 传入文件Sample路径，跳转到同级位置open同类文件，Return[绝对文件路径s[]，文件名称，文件后缀，文件位置路径]
    p, f = os.path.split(samplefile)
    f, ext = os.path.splitext(samplefile)
    #该出有异常提示objc[8783]百度为mac系统问题
    files = QFileDialog.getOpenFileNames(None, lo.get("openfiledialog"), p, "OnlyFiles(*%s)"%ext)
    ret=[]
    for file in files[0]:
        filepath, extname = os.path.splitext(file)
        path, name = os.path.split(filepath)
        ret.append([file,name,extname,path])
    return ret
class Dlg(QDialog):
    #带输入edit控件的输入窗口,可自动输入last,可作为单项修改编辑窗
    def __init__(self, title, last="", parent=None):
        super(Dlg, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle(title)
        self.inputedit = QLineEdit(last)
        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)
        validator = QRegExp(r'[^\s][\w\s]+')
        self.inputedit.setValidator(QRegExpValidator(validator, self))
        v_box = QVBoxLayout()
        v_box.addWidget(self.inputedit)
        v_box.addWidget(btns)
        self.setLayout(v_box)

        self.word = None
    def accept(self):
        if self.inputedit.text()=="":
            self.word = None
        else:
            self.word = unicode(self.inputedit.text())
        QDialog.accept(self)
    def reject(self):
        QDialog.reject(self)
def Err(message):
#错误信息窗口，模态
    mess=""
    for msgid in message.split():
        #分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
        # print(e.get(msgid), g.get(msgid))
        # print(msgid)
        mess+=lo.get(msgid)
    QMessageBox.critical(None,("Error"),mess, QMessageBox.StandardButton(QMessageBox.Ok))

def Warn(message):
#警告信息窗口，模态
    mess=""
    for msgid in message.split():
        #分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
        # print(e.get(msgid), g.get(msgid))
        # print(msgid)
        mess+=lo.get(msgid)
    QMessageBox.warning(None, ("Warning"), mess, QMessageBox.StandardButton(QMessageBox.Ok))
    # printerr(mess,1)

def Info(message):
#信息窗口，模态
    mess=""
    for msgid in message.split():
        #分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
        # print(e.get(msgid), g.get(msgid))
        # print(msgid)
        mess+=lo.get(msgid)
    QMessageBox.information(None, ("Infomation"), mess, QMessageBox.StandardButton(QMessageBox.Ok))
    # printerr(mess,1)

def printerr(meg="ERR:",start=0):
#获取调用源,可用于错误处理
    errfunc=[meg,sys._getframe(start).f_back.f_lineno]
    #[行号，函数名，文件名，上级函数名，上级文件名，，，]
    for i in range(start,20):
        errfunc.append(sys._getframe(i).f_back.f_code.co_name)
        errfile=sys._getframe(i).f_back.f_code.co_filename
        errfunc.append("->"+os.path.basename(errfile))
        if(os.path.dirname(errfile)==CoreConfig.maindir):
            break
        # print(sys._getframe().f_back.f_lineno)
    print(errfunc)
