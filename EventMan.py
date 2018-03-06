# 定义可用实例子类
# 负责事件Case的实例


import StrCheck
# import Qtable
# import Mbox
from PyQt5.QtGui import QPixmap,QMovie
from PyQt5 import QtCore


import time

#记录开启的线程
runtlist=[]
class TimeThread(QtCore.QThread):
    signal = QtCore.pyqtSignal() # 信号
    def __init__(self, parent=None):
        super(TimeThread, self).__init__(parent)
        self.working = True
        self.looptime = 0

    def start_timer(self,*tpara):
        self.looptime = tpara[0]
        runtlist.append(self)
        self.start()
    def stop(self):
        self.working= False
    def run(self):
        while self.working:
            # print("Working", self.thread())
            self.signal.emit() # 发送信号
            # self.num += 1ptime)
            self.sleep(self.looptime)

class EThread(QtCore.QThread):
    signal = QtCore.pyqtSignal() # 信号
    def __init__(self, parent=None):
        super(EThread, self).__init__(parent)
        self.rev=[]
        self.casename="demo"

    def startet(self,case,*send):
        self.casename=case
        self.rev = send
        self.start()
        # runtlist.append(self)

    def run(self):
        # 执行一次，自动停止
        Banding = dict(demo=Demo,
                       # add=addrow, open=loaddics, save=savedic, deln=delrow,
                       ugroup=usergroupchange,
                       # init=initui,
                       )
        Banding[self.casename]().resp(*self.rev)

def Event(case="demo"):
    Banding = dict(demo=Demo,
                   # add=addrow, open=loaddics,save=savedic,deln=delrow,登陆=checkpassword,
                   初始化=initui,实时时间=updatashowtime,close=reclose,
                   )
    return Banding[case]()
def readlang(dictfile = './Language/Chinese.txt'):
    f = open(dictfile, 'r')
    a = f.read()
    trans = eval(a)
    # list=(trans.keys())
    f.close()
    return trans
def dlgclose(dlg):
    # 关闭轮询
    for i in runtlist:
        if i.isRunning():
            i.stop()
            while i.isRunning():
                time.sleep(0.1)
    # 退出对话框
    dlg.accept()
class reclose:
    #接管结束的函数
    def resp(self,*rev):
        dlgclose(rev[0])
# class checkpassword:
#     #响应用户密码登陆
#     def resp(self,*rev):
#         g,u,p =rev[1].currentIndex(),rev[2].text(),rev[3].text()
#         if StrCheck.check().gup(g,u,p):
#             dlgclose(rev[0])
#         else:
#             print(StrCheck.check().login, '3333')

class usergroupchange:
    #响应用户组切换
    def resp(self,*rev):
        picli=["./Res/admin.png","./Res/user.png","./Res/viewer.png"]
        rev[0].setPixmap(QPixmap(picli[rev[1].currentIndex()]))
class initui:
    #响应用户组切换
    def resp(self,*rev):
        #获得上次登陆的用户名称
        lastname=StrCheck.check().lastu()
        if lastname=='':
            # 设置焦点在用户名
            rev[3].setFocus()
        else:
            rev[3].setText(lastname)
            # 设置焦点在密码
            rev[4].setFocus()
        #获得对应的上次用户组
        rev[1].setCurrentIndex(StrCheck.check().lastg())
        picli=["./Res/admin.png","./Res/user.png","./Res/viewer.png","./Res/welcome.gif"]
        print(picli[rev[1].currentIndex()])
        rev[0].setPixmap(QPixmap(picli[rev[1].currentIndex()]))
        mv=QMovie(picli[3])
        rev[2].setMovie(mv)
        mv.start()
class Demo:
    #响应
    def resp(self,*rev):
        # time.sleep(2)
        print("=======demo==== para len %s ==="%len(rev))
class updatashowtime:
    #响应
    def resp(self,*rev):
        showtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # print(time.time())
        rev[0].setText(showtime)

# class loaddic:
#     #加载翻译的字典文件，并添加到table，resp参数[table]
#     def resp(self,*rev):
#         file=Mbox.openfiles('./Language/Chinese.txt')
#         if file[0]!="":
#             dicli=readlang(file[0])
#             Qtable.rlist(rev[0],list(dicli.values()),list(dicli.keys()),file[1])
# class loaddics:
#     #加载多个字典文件，并添加到table，resp参数[table]
#     def resp(self,*rev):
#         files=Mbox.openfiles('./Language/Chinese.txt')
#         for file in files:
#             if file[0]!="":
#                 dicli=readlang(file[0])
#                 Qtable.rlist(rev[0],list(dicli.values()),list(dicli.keys()),file[1])
# class addrow:
#     #新增行，添加到table，resp参数[table]
#     def resp(self,*rev):
#         word=Mbox.input("add")
#         if word!=None:
#             li=[]
#             li.append(word)
#             Qtable.rlist(rev[0],[""],li)
# class savedic:
#     #响应读取翻译的字典文件，并添加到table，resp参数[table]
#     def resp(self,*rev):
#         dicli=Qtable.getcdict(rev[0])
#         for fn in dicli.keys():
#             dictfile="./Language/%s.txt"%fn
#             f = open(dictfile, 'w')
#             f.write(str(dicli[fn]))
#             f.close()
#
# class delrow:
#     # 新增当前选择行，添加到table，resp参数[table]
#     def resp(self,*rev):
#         Qtable.delrow(rev[0])