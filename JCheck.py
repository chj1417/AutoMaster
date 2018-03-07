# 自定义的字符串处理模块
# 负责密码加密
# 唯一接口，单例模式
# 密码文件./bin/sys.avi

import os

class check(object):
    login = False
    # 重写new控制实例的创建过程，实现单例模式
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(check, cls).__new__(cls, *args, **kw)
        return cls._instance
    def __init__(self):
        self.pwdfile = './bin/sys.avi'
        if (not os.path.exists(self.pwdfile)):
            self.chjuser = {
                'chjlast': ['', 0],
                'admin': ['', 0]
            }
            self.save(self.chjuser)
        else:
            pwdf = open(self.pwdfile, 'r')
            a = pwdf.read()
            self.chjuser = eval(a)
            pwdf.close()
        # print(self.login)
    def issave(self):
        passfalse= True
        if passfalse=='' or passfalse.lower()=='false' or passfalse==0:
            return False
        else:
            return True
    def save(self,dict):
        pwdf = open(self.pwdfile, "w")
        pwdf.write(str(dict))
        pwdf.close()
    def gup(self,g,u,p):
        if self.chjuser.__contains__(u):
            con = self.chjuser.get(u)
            if con[0] == p and con[1] == g:
                self.login=True
                self.chjuser['chjlast'] = [u, g]
                self.save(self.chjuser)
                return True
            else:
                self.login=False
                return False
    def lastg(self):
        if self.issave():
            return self.chjuser['chjlast'][1]
        else:
            return 0
    def lastu(self):
        if self.issave():
            return self.chjuser['chjlast'][0]
        else:
            return ''
def adduser(self,g,u,p):
    pass
