# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QPixmap
import os
import logging
import time

class TimeThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str) # 信号
    def __init__(self, parent=None):
        super(TimeThread, self).__init__(parent)
        self.working = True
        self.looptime = 0

    def start_timer(self,tpara):
        self.looptime = tpara
        self.start()
    def stop(self):
        self.working= False
    def run(self):
        while self.working:
            showtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.signal.emit(showtime)  # 发送信号
            self.sleep(self.looptime)
class LoadWin(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(200, 100)
        Dialog.setStyleSheet("")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(12, 12, 12, 12)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.grouppic = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grouppic.sizePolicy().hasHeightForWidth())
        self.grouppic.setSizePolicy(sizePolicy)
        self.grouppic.setMinimumSize(QtCore.QSize(90, 90))
        self.grouppic.setMaximumSize(QtCore.QSize(90, 90))
        self.grouppic.setText("")
        self.picli=["./bin/admin.png","./bin/user.png","./bin/viewer.png","./bin/welcome.gif"]##################
        self.grouppic.setPixmap(QtGui.QPixmap(self.picli[0]))
        self.grouppic.setScaledContents(True)
        self.grouppic.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.grouppic.setObjectName("grouppic")
        self.horizontalLayout_5.addWidget(self.grouppic)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.TypeLabel = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TypeLabel.sizePolicy().hasHeightForWidth())
        self.TypeLabel.setSizePolicy(sizePolicy)
        self.TypeLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TypeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TypeLabel.setObjectName("TypeLabel")
        self.horizontalLayout_3.addWidget(self.TypeLabel)
        self.group = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group.sizePolicy().hasHeightForWidth())
        self.group.setSizePolicy(sizePolicy)
        self.group.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.group.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.group.setObjectName("group")
        self.group.addItem("")
        self.group.addItem("")
        self.group.addItem("")
        self.horizontalLayout_3.addWidget(self.group)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.UserLabel = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UserLabel.sizePolicy().hasHeightForWidth())
        self.UserLabel.setSizePolicy(sizePolicy)
        self.UserLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.UserLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.UserLabel.setObjectName("UserLabel")
        self.horizontalLayout.addWidget(self.UserLabel)
        self.user = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user.sizePolicy().hasHeightForWidth())
        self.user.setSizePolicy(sizePolicy)
        self.user.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.user.setText("")
        self.user.setObjectName("user")
        self.horizontalLayout.addWidget(self.user)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PassLabel = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PassLabel.sizePolicy().hasHeightForWidth())
        self.PassLabel.setSizePolicy(sizePolicy)
        self.PassLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.PassLabel.setScaledContents(False)
        self.PassLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PassLabel.setObjectName("PassLabel")
        self.horizontalLayout_2.addWidget(self.PassLabel)
        self.pwd = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwd.sizePolicy().hasHeightForWidth())
        self.pwd.setSizePolicy(sizePolicy)
        self.pwd.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pwd.setObjectName("pwd")
        self.horizontalLayout_2.addWidget(self.pwd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.timenow = QtWidgets.QLabel(Dialog)
        self.timenow.setObjectName("timenow")
        self.horizontalLayout_4.addWidget(self.timenow)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.loginbtn = QtWidgets.QPushButton(Dialog)
        self.loginbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.loginbtn.setObjectName("loginbtn")
        self.horizontalLayout_4.addWidget(self.loginbtn)
        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 0, 1, 1)
        self.welcome = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome.sizePolicy().hasHeightForWidth())
        if os.path.exists(self.picli[3]):
            self.welcome.setSizePolicy(sizePolicy)
            self.welcome.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.welcome.setAutoFillBackground(True)
            self.welcome.setText("")
            self.welcome.setScaledContents(True)
            self.welcome.setAlignment(QtCore.Qt.AlignCenter)
            self.welcome.setObjectName("welcome")
            self.gridLayout.addWidget(self.welcome, 0, 0, 1, 1)
            #########
            mv = QMovie(self.picli[3])
            self.welcome.setMovie(mv)
            mv.start()

        self.retranslateUi(Dialog)
        self.group.currentIndexChanged['int'].connect(self.changegroud)
        self.loginbtn.clicked.connect(self.clicklogin)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.user, self.pwd)
        Dialog.setTabOrder(self.pwd, self.group)
        self.timer_t = TimeThread()
        self.timer_t.signal.connect(self.timeeven)
        self.timer_t.start_timer(1)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "loginwidow"))
        self.TypeLabel.setText(_translate("Dialog", "usergroup"))
        self.group.setItemText(0, _translate("Dialog", "admin"))
        self.group.setItemText(1, _translate("Dialog", "operator"))
        self.group.setItemText(2, _translate("Dialog", "viewer"))
        self.UserLabel.setText(_translate("Dialog", "username"))
        self.PassLabel.setText(_translate("Dialog", "password"))
        self.label.setText(_translate("Dialog", "Version V 1.0.0"))
        self.loginbtn.setText(_translate("Dialog", "login"))
    def timeeven(self,timestr):
        self.timenow.setText(timestr)
    def clicklogin(self):
        groupli=['Admin','Operator','Viewer']
        logging.info('longin %s=%s'%(groupli[self.group.currentIndex()],self.user.text()))
    def changegroud(self):
        self.grouppic.setPixmap(QPixmap(self.picli[self.group.currentIndex()]))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = LoadWin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

