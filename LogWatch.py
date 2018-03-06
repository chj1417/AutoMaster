# IDE小工具
# 负责监控log文件

import sys
import os
from PyQt5 import QtCore, QtWidgets

# 相对路径参考标准为对应os的工作路径getcwd
maindir=os.getcwd()
WatchFile = maindir + '/TestLog.log'
FileWatch = os.path.exists(WatchFile)
if (not os.path.exists(WatchFile)):
    inif = open(WatchFile, "w")
    inif.close()

class TimeThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str,int) # 信号
    def __init__(self, parent=None):
        super(TimeThread, self).__init__(parent)
        self.working = os.path.exists(WatchFile)
        self.looptime = 0

    def start_timer(self,tpara):
        self.file = open(WatchFile)
        self.looptime = tpara
        self.start()
    def stop(self):
        self.working= False
    def run(self):
        while self.working:
            self.where = self.file.tell()
            self.line = self.file.readline()
            if not self.line:
                self.sleep(self.looptime)
                self.file.seek(self.where)
                self.working = os.path.exists(WatchFile)
            else:
                self.signal.emit(self.line,20)  # 发送信号,显示行数20>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        sys.exit()

class WatchForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.timer_t = TimeThread()
        self.timer_t.signal.connect(self.addlog)
        self.timer_t.start_timer(1) #监控空闲间隔1s
        self.linelist=[]

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "日志监控"))
        self.textBrowser.setText(_translate("Form", "..."))
    def addlog(self,text,num):
        self.view=''
        self.linelist.append(text)
        if len(self.linelist)>num:
            self.linelist.pop()
        for i in self.linelist:
            self.view=i+self.view
            self.textBrowser.setText(self.view)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = WatchForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())