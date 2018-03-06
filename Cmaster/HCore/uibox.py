# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMessageBox

def Info(mess):
    QMessageBox.information(None, ("Infomation"), mess, QMessageBox.StandardButton(QMessageBox.Ok))

def setup(app):
    pass