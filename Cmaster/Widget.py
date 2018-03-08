#负责窗体部件widget管理

from PyQt5.QtWidgets import *
from Cmaster.Tab import Tab
from Cmaster import gui_scale
from Cmaster.StyleSheets import get_stylesheet

class Widget(QToolBar):
    def __init__(self, parent):
        QToolBar.__init__(self, parent)
        self.setStyleSheet(get_stylesheet("Widget"))
        self.setObjectName("ribbonWidget")
        self.setWindowTitle("Ribbon")
        self._ribbon_widget = QTabWidget(self)
        self._ribbon_widget.setMaximumHeight(140*gui_scale())
        self._ribbon_widget.setMinimumHeight(110*gui_scale())
        self.setMovable(False)
        self.addWidget(self._ribbon_widget)

    def add_ribbon_tab(self, name):
        ribbon_tab = Tab(self, name)
        ribbon_tab.setObjectName("tab_" + name)
        self._ribbon_widget.addTab(ribbon_tab, name)
        return ribbon_tab

    def set_active(self, name):
        self.setCurrentWidget(self.findChild("tab_" + name))