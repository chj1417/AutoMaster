import sys

from PyQt5 import QtCore, QtGui,QtWidgets

from Cmaster.StyleSheets import get_stylesheet

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    model = QtWidgets.QDirModel()#系统给我们提供的

    tree = QtWidgets.QTreeView()
    cssf=open('../stylesheets/TreeView.css')
    style=cssf.read()
    tree.setAlternatingRowColors(True)
    tree.setStyleSheet(style)

    tree.setModel(model)

    tree.setWindowTitle(tree.tr("Dir View"))

    tree.resize(640, 480)

    tree.show()

    sys.exit(app.exec_())