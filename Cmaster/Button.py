# 负责按钮管理
# 带图标的按钮IconButton定义大图标模式isbig和菜单栏模式

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *

from Cmaster import gui_scale
from Cmaster.StyleSheets import get_stylesheet

class IconButton(QToolButton):
    def __init__(self, owner, action, isbig):
        QPushButton.__init__(self, owner)
        sc = gui_scale()
        self._actionOwner = action
        self.update_button_status_from_action()
        self.clicked.connect(self._actionOwner.trigger)
        self._actionOwner.changed.connect(self.update_button_status_from_action)

        if isbig:
            self.setMaximumWidth(80 * sc)
            self.setMinimumWidth(50 * sc)
            self.setMinimumHeight(75 * sc)
            self.setMaximumHeight(80 * sc)
            self.setStyleSheet(get_stylesheet("BigButton"))
            self.setToolButtonStyle(3)
            self.setIconSize(QSize(32 * sc, 32 * sc))
        else:
            self.setToolButtonStyle(2)
            self.setMaximumWidth(120 * sc)
            self.setIconSize(QSize(16 * sc, 16 * sc))
            self.setStyleSheet(get_stylesheet("SmallButton"))

    def update_button_status_from_action(self):
        self.setText(self._actionOwner.text())
        self.setStatusTip(self._actionOwner.statusTip())
        self.setToolTip(self._actionOwner.toolTip())
        self.setIcon(self._actionOwner.icon())
        self.setEnabled(self._actionOwner.isEnabled())
        self.setCheckable(self._actionOwner.isCheckable())
        self.setChecked(self._actionOwner.isChecked())

class TButton(QPushButton):
    def __init__(self, owner, action, isbig=False):
        QPushButton.__init__(self, owner)
        # sc = gui_scale()
        self._actionOwner = action
        self.update_button_status_from_action()
        self.clicked.connect(self._actionOwner.trigger)
        self._actionOwner.changed.connect(self.update_button_status_from_action)

        if isbig:
        #     self.setMaximumWidth(80 * sc)
        #     self.setMinimumWidth(50 * sc)
        #     self.setMinimumHeight(75 * sc)
        #     self.setMaximumHeight(80 * sc)
            self.setStyleSheet(get_stylesheet("BigButton"))
        #     self.setToolButtonStyle(3)
        #     self.setIconSize(QSize(32 * sc, 32 * sc))
        else:
        #     self.setToolButtonStyle(2)
        #     self.setMaximumWidth(120 * sc)
        #     self.setIconSize(QSize(16 * sc, 16 * sc))
            self.setStyleSheet(get_stylesheet("SmallButton"))

    def update_button_status_from_action(self):
        self.setText(self._actionOwner.text())
        self.setStatusTip(self._actionOwner.statusTip())
        self.setToolTip(self._actionOwner.toolTip())
        # self.setIcon(self._actionOwner.icon())
        # self.setEnabled(self._actionOwner.isEnabled())
        # self.setCheckable(self._actionOwner.isCheckable())
        # self.setChecked(self._actionOwner.isChecked())
