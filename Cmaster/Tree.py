# 负责树样式
# 负责树的编辑

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QTreeWidgetItemIterator
from Cmaster.StyleSheets import get_stylesheet
import logging

class TreeList(QTreeWidget):
    def __init__(self,header):
        QTreeWidget.__init__(self)
        self.head=header
        self.setStyleSheet(get_stylesheet("TreeView"))
        self.setAlternatingRowColors(True)
        headerItem = QTreeWidgetItem(self.head)
        self.setHeaderItem(headerItem)
        # self.editbox=[] #可双击编辑

    def setlist(self,dat,pa=None):
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
                    # self.openPersistentEditor
                    It.setFlags(It.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable|Qt.ItemIsEditable)
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
                self.setlist(newdat,newpa)
    def getlist(self):
        it = QTreeWidgetItemIterator(self)
        ccount=it.value().columnCount()
        datas=[]
        while it.value():
            data = []
            # yield it.value()
            data.append(str(it.value().checkState(0)>=1))
            if (it.value().parent()==None):
                data.append('root')
            else:
                data.append(it.value().parent().text(0))
            for i in range(ccount):
                # print(it.value().data(1,0))
                data.append(it.value().text(i))
            it += 1
            datas.append(data)
        return datas
    def clonelist(self):
        cit=self.currentItem().clone()
        newit=cit.text(0)+'(copy)'
        cit.setText(0,newit)
        cpa = self.currentItem().parent()
        if cpa:
            cpa.addChild(cit)
        else:
            self.addTopLevelItem(cit)
    def dellist(self):
        dit=self.currentIndex().row()
        dpa = self.currentItem().parent()
        if dpa:
            dpa.takeChild(dit)
        else:
            self.takeTopLevelItem(dit)
    #   启动编辑框，It.setFlags(It.flags()|Qt.ItemIsEditable)可双击编辑
    # def editlist(self):
    #     for lastedit in self.editbox:
    #         self.closePersistentEditor(lastedit[0],lastedit[1])
    #     self.editbox=[]
    #     lastit=self.currentItem()
    #     lastcol=self.currentColumn()
    #     self.openPersistentEditor(lastit,lastcol)
    #     self.editbox.append([lastit,lastcol])
    def moveup(self):
        mit=self.currentItem()
        mitindex=self.currentIndex().row()
        mpa=mit.parent()
        if mitindex>0:
            self.dellist()
            if mpa:
                mpa.insertChild(mitindex-1,mit)
            else:
                self.insertTopLevelItem(mitindex-1,mit)
            self.setCurrentItem(mit)
    def movedown(self):
        mit = self.currentItem()
        mitindex = self.currentIndex().row()
        mpa = mit.parent()
        if mpa:
            if mitindex <(mpa.childCount()-1):
                self.dellist()
                mpa.insertChild(mitindex + 1, mit)
                self.setCurrentItem(mit)
        else:
            if mitindex<(self.topLevelItemCount()-1):
                self.dellist()
                self.insertTopLevelItem(mitindex + 1, mit)
                self.setCurrentItem(mit)
    def changestate(self):
        csit=self.currentItem()
        if csit.checkState(0)>=1:
            csit.setCheckState(0, Qt.Unchecked)
        else:
            csit.setCheckState(0, Qt.Checked)
    def changall(self):
        csit = QTreeWidgetItemIterator(self)
        disbool=True
        while csit.value():
            if csit.value().checkState(0) >= 1:
                csit.value().setCheckState(0, Qt.Checked)
            else:
                disbool=False
                csit.value().setCheckState(0, Qt.Checked)
            csit += 1
        if disbool:
            csit = QTreeWidgetItemIterator(self)
            while csit.value():
                csit.value().setCheckState(0, Qt.Unchecked)
                csit += 1





