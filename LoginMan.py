from PyQt5 import QtWidgets, uic
# import CoreConfig
import EventMan
# import Lang

# tempui = Lang.loui("Login.ui")
# 使用uic.loadUiType载入界面文件
# print(tempui)
UiWindow, QtBaseClass = uic.loadUiType("Login.ui")

# 创建类LoadWin类继承于Qt库并且调用了父类的初始化函数
class LoadWin(QtWidgets.QDialog, UiWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UiWindow.__init__(self)
        self.setupUi(self)
        # 定时自触发事件，相当于定时器或超时CASE[等待间隔，*关联控件]>>>>>>>>>>>>>>>>>>>>>>>>>
        self.timercase={
            "实时时间":[1,'timenow'],

        }
        # 定义直接执行函数的事件，例如界面初始化事件，已经使用子模块线程的事件Qmovice等>>>>>>>>>
        self.direcase = {
            '初始化': ['grouppic', 'group', "welcome",'user','pwd'],
            '登陆':['group','user','pwd'],

        }
        # 自动构建轮询线程
        for case,para in self.timercase.items():
            # print(case,"+++>",para)
            self.timer_t = EventMan.TimeThread()
            self.timer_t.signal.connect(lambda: self.Event(case, *para[1:]))
            self.timer_t.start_timer(para[0],self.timer_t)
            # self.timer_t.stop_timer()
        # 构建直接执行的函数"初始化"
        # for func,p in self.direcase.items():
        self.Event('初始化', *self.direcase.get('初始化',['grouppic', 'group', "welcome",'user','pwd']))

        # 定义界面按钮的单击动作链接的执行函数>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # AutoC

        # self.actionrecord.triggered.connect(lambda:self.Event('demo','user'))
        self.loginbtn.clicked.connect(lambda:self.Event('登陆','self','group','user','pwd'))
        self.group.currentIndexChanged.connect(lambda:self.Event('ugroup','grouppic','group'))

        # 以上为脚本自动插入文本位置（插入索引"AutoC"）

    # 定义统一的事件触发入口,如何处理事件统一在EvenMan处理
    def Event(self, case, *index):
        # 整理需要传输的参数(相当于LabView事件结构的寄存器)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        try:
            reg1 = 1
        except:
            reg1 = 0
        # 以上预处理的寄存器，请添加到下面到字典中，Event直接使用其标签即可
        regdata = {
            # 使用字典可以定义唯一Label,注意字典定义间有逗号>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            # AutoH
            "self":self,
            "timenow":self.timenow,
            "welcome":self.welcome,
            "group":self.group,
            "user":self.user,
            "pwd":self.pwd,
            "grouppic":self.grouppic,
        }
        # 以上为脚本自动插入文本位置（插入索引"AutoH"）
        senddata = []
        for i in index:
            try:
                senddata.append(regdata[i])
            except KeyError as e:
                print("Warning[", case, "NotFound Para]", e)
                senddata.append(i)
                # break
        try:
            # 已含线程or定时器or过载事件不能再使用子线程
            if self.direcase.__contains__(case) or self.timercase.__contains__(case):
                EventMan.Event(case).resp(*senddata)
            else:
                self.et = EventMan.EThread()
                self.et.startet(case,*senddata)
        except KeyError as e:
            print("ERROR[", "Undefined Case]", e)
        # self.Return(self.spinRate)

    # 定义响应函数,界面被动刷新，有待设计处理方式>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def Return(self, *obj):
        self.et = EventMan.EThread()
        # self.timer_t.signal.connect(lambda: self.Event('uptime', 'timenow'))
        self.et.startet(*obj)


# 作为主函数调试，独立调试时请把该py放置在项目根位置（和CoreConfig同位置）
if __name__ == "__main__":
    print('# 作为主函数调试，独立调试时请把该py放置在项目根位置（和CoreConfig同位置）')
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = LoadWin()
    ui.show()
    sys.exit(app.exec_())















