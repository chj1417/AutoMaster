# 负责QtTableWidgets的相关操作
# 通过用途迭代及防呆，简化控件的使用
from PyQt5.QtWidgets import QTableWidgetItem

CHead=[]
RHead=[]
def rlist(table,list,rhead,head=""):
    #行方向列表函数rlist，tabel传入QTableWidget控件，内容list，行首rhead，列首head
    cnow=0
    try:
        CHead.index(head)
    except ValueError:
        if len(CHead)>0 and head=="":
            #列首为空，默认插入已有第一列
            pass
        else:
            table.insertColumn(table.columnCount())
            item = QTableWidgetItem()
            if head=="":
                item.setText("Default")
            else:
                item.setText(head)
            table.setHorizontalHeaderItem(table.columnCount()-1,item)
            #记录作为去重用途
            CHead.append(head)
            cnow=CHead.index(head)
    for i,r in enumerate(rhead):
        try:
            rnow=RHead.index(r)
            item = QTableWidgetItem()
            item.setText(list[i])
            table.setItem(rnow, CHead.index(head), item)
        except ValueError:
            table.insertRow(table.rowCount())
            item = QTableWidgetItem()
            item.setText(r)
            table.setVerticalHeaderItem(table.rowCount() - 1, item)
            # 记录作为去重用途
            RHead.append(r)
            # 插入list数据
            item = QTableWidgetItem()
            item.setText(list[i])
            table.setItem(table.rowCount()-1, cnow, item)
def getcdict(table):
    # 逐列C返回字典，键值为所有行R字典
    cd=dict.fromkeys(CHead)
    for i,c in enumerate(CHead):
        d=dict.fromkeys(RHead)
        for j,r in enumerate(RHead):
            t=table.item(j,i)
            if t==None:
                d[r]=""
            else:
                d[r]=t.text()
        cd[c]=d
    return (cd)
def delrow(tabel):
    # 单行删除后index不更新，index需从大到小逐行删除
    dli=[]
    for d in tabel.selectedIndexes():
        dli.append(d.row())
        dli.sort(reverse=True)
    for dr in dli:
        tabel.removeRow(dr)
        RHead.__delitem__(dr)