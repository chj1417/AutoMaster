# 图标icons资源管理

from PyQt5.QtGui import *

icons_instance = None

def get_icon(name):
    global icons_instance
    if not icons_instance:
        icons_instance = Icons()
    return icons_instance.icon(name)


class Icons(object):
    def __init__(self):
        self._icons = {}
        self.make_icon("folder", "Cmaster/icons/folder.png")
        self.make_icon("open", "Cmaster/icons/folder.png")
        self.make_icon("save", "Cmaster/icons/save.png")
        self.make_icon("icon", "Cmaster/icons/icon.png")
        self.make_icon("exit", "Cmaster/icons/exit.png")
        self.make_icon("paste", "Cmaster/icons/paste.png")
        self.make_icon("zoom", "Cmaster/icons/zoom.png")
        self.make_icon("copy", "Cmaster/icons/copy.png")
        self.make_icon("about", "Cmaster/icons/about.png")
        self.make_icon("license", "Cmaster/icons/license.png")
        self.make_icon("default", "Cmaster/icons/folder.png")

    def make_icon(self, name, path):
        icon = QIcon()
        icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        self._icons[name] = icon

    def icon(self, name):
        icon = self._icons["default"]
        try:
            icon = self._icons[name]
        except KeyError:
            print("icon " + name + " not found")
        return icon
