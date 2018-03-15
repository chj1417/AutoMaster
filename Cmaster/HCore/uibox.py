# -*- coding: utf-8 -*-
# 简化所有的提示和消息窗口
# 负责各种信息提示窗口
# 内置语言
# 负责简单的输入窗口
import os
from PyQt5.QtWidgets import QMessageBox,QFileDialog,QDialog

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
def Info(mess):
    QMessageBox.information(None, ("Infomation"), mess, QMessageBox.StandardButton(QMessageBox.Ok))

def input(title,last=""):
# 输入窗，窗体比较简单，由本模块代码构建class Dlg(QDialog)
    add = Dlg(title,last)
    if add.exec_():
         return add.word
def openfile(samplefile):
# 传入文件Sample路径，跳转到同级位置open同类文件，Return[绝对文件路径，文件名称，文件后缀，文件位置路径]
    p, f = os.path.split(samplefile)
    f, ext = os.path.splitext(samplefile)
    #该出有异常提示objc[8783]百度为mac系统问题
    file = QFileDialog.getOpenFileName(None, "open file dialog", p, "OnlyFiles(*%s)"%ext)
    filepath, extname = os.path.splitext(file[0])
    path, name = os.path.split(filepath)
    return file[0],name,extname,path
def openfiles(samplefile):
# 传入文件Sample路径，跳转到同级位置open同类文件，Return[绝对文件路径s[]，文件名称，文件后缀，文件位置路径]
    p, f = os.path.split(samplefile)
    f, ext = os.path.splitext(samplefile)
    #该出有异常提示objc[8783]百度为mac系统问题
    files = QFileDialog.getOpenFileNames(None, "open file dialog", p, "OnlyFiles(*%s)"%ext)
    ret=[]
    for file in files[0]:
        filepath, extname = os.path.splitext(file)
        path, name = os.path.split(filepath)
        ret.append([file,name,extname,path])
    return ret