# 负责树样式
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
from Cmaster.StyleSheets import get_stylesheet
import logging

class TreeList(QTreeWidget):
    def __init__(self,Data,header):
        QTreeWidget.__init__(self)
        self.setStyleSheet(get_stylesheet("TreeView"))
        self.setAlternatingRowColors(True)
        headerItem = QTreeWidgetItem(header)
        self.setHeaderItem(headerItem)
        self.dat2tree(Data)

    def dat2tree(self,dat,pa=None):
        if pa is None:
            itempa={'root':self}
            self.runtimes=0
        else:
            self.runtimes+=1
            itempa=pa
        newpa={}
        newdat=[]
        for i in dat:
            if itempa.__contains__(i[1]):
                It = QTreeWidgetItem(itempa[i[1]])
                for j, pdata in enumerate(i[2:]):
                    It.setText(j, pdata)
                    It.setFlags(It.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
                newpa[i[2]] = It
                # CheckBox不选的属性是'0'或空''或'false'
                if (i[0]=='0' or i[0]=='' or i[0].lower()=='false'):
                    It.setCheckState(0, Qt.Unchecked)
                else:
                    It.setCheckState(0, Qt.Checked)
            else:
                newdat.append(i)
        if newdat!=[] and self.runtimes<10:
            if newpa=={}:
                for errdata in newdat:
                    logging.error('NoFound Tree Parent %s'%errdata[1])
                    errIt = QTreeWidgetItem(self)
                    for j, pdata in enumerate(errdata[1:]):
                        errIt.setText(j, pdata)
                    # errIt.setCheckState(0, Qt.Unchecked)
                print('----------No ParentTree Childs-----')
                print(newdat)
                print('----------MaxTree= %s Level---------'%self.runtimes)
            else:
                self.dat2tree(newdat,newpa)


