#!/usr/bin/python3
#coding:utf-8
#简单版的用户登陆窗

from PyQt5.QtWidgets import *
import JCheck
import logging

class LoadWin(QDialog):
    def __init__(self, parent=None):
        super(LoadWin, self).__init__(parent)
        usr = QLabel("用户：")
        pwd = QLabel("密码：")
        self.usrLineEdit = QLineEdit()
        self.pwdLineEdit = QLineEdit()
        self.pwdLineEdit.setEchoMode(QLineEdit.Password)

        gridLayout = QGridLayout()
        gridLayout.addWidget(usr, 0, 0, 1, 1)
        gridLayout.addWidget(pwd, 1, 0, 1, 1)
        gridLayout.addWidget(self.usrLineEdit, 0, 1, 1, 3);
        gridLayout.addWidget(self.pwdLineEdit, 1, 1, 1, 3);

        okBtn = QPushButton("确定")
        cancelBtn = QPushButton("取消")
        btnLayout = QHBoxLayout()

        btnLayout.setSpacing(60)
        btnLayout.addWidget(okBtn)
        btnLayout.addWidget(cancelBtn)

        dlgLayout = QVBoxLayout()
        dlgLayout.setContentsMargins(40, 40, 40, 40)
        dlgLayout.addLayout(gridLayout)
        dlgLayout.addStretch(40)
        dlgLayout.addLayout(btnLayout)

        self.setLayout(dlgLayout)
        okBtn.clicked.connect(self.accept)
        cancelBtn.clicked.connect(self.reject)
        self.setWindowTitle("登录")
        self.resize(300, 200)

    def accept(self):
        if JCheck.check().gup(0,self.usrLineEdit.text(), self.pwdLineEdit.text()):
            super(LoadWin, self).accept()
            logging.info('Longin Admin=%s'%self.usrLineEdit.text())
        else:
            QMessageBox.warning(self,
                    "警告",
                    "用户名或密码错误！",
                    QMessageBox.Yes)
            self.usrLineEdit.setFocus()

