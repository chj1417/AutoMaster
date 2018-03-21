# 负责对接数据库sqlite3
# 每个文件为一个类实例
# 类记录，上次的Tablename和Header长度
# 数据库操作更简易化
import sqlite3
import logging

class DBfile():
    def __init__(self,db=':memory:'):
        self.connection = sqlite3.connect(db)
        self.lasttable=[] # name,headlen
        self.tables=[]
        self.tablelist()

    def tablelist(self):
        cmd="select name from sqlite_master where type = 'table' order by name"
        listpa=self.connection.execute(cmd).fetchall()
        if listpa==[]:
            self.tables=[]
            return []
        else:
            tablels=[]
            for name in listpa:
                tablels.append(name[0])
            #更新变量tables
            self.tables=tablels
        return tablels

    def headlist(self,name):
        headls=[]
        li=self.connection.execute("PRAGMA table_info(%s)"%name).fetchall()
        for h in li:
            headls.append(h[1])
        logging.info(li)
        return headls

    def new(self,name='test',head=None):
        if head==None:
            head=['tid','msg']
        # Create a table
        headlen=len(head)
        if (self.tables.count(name)==0):
            if headlen==1:
                cmd='CREATE TABLE '+name+' ('+str(head[0])+')'
            elif headlen>1:
                cmd='CREATE TABLE '+name+str(tuple(head))
            else:
                logging.error('Head Error 0 Columns')
                return False
            self.connection.execute(cmd)
            self.lasttable=[name,headlen]
            self.connection.commit()
            logging.info('Creat Table: %s'%name)
            return True
        elif headlen==len(self.headlist(name)):
            logging.warning('Already Exists Table: %s'%name)
            self.lasttable=[name,headlen]
            return True
        else:
            logging.error('Same Table Name is Different Header')
            return False
    def write(self,Data,table=None):
        if table==None:
            table=self.lasttable[0]
        inls=[]
        for one in Data:
            inls.append(tuple(one))
        cmd = 'INSERT INTO %s VALUES (?' % table
        for para in range(len(Data[0])-1):
            cmd=cmd+',?'
        cmd=cmd+')'
        self.connection.executemany(cmd,inls)
        self.connection.commit()

    def read(self,table=None,readHead=False):
        if table == None:
            table = self.lasttable[0]
        if readHead:
            resultls = [self.headlist(table)]
        else:
            resultls = []
        lsall = self.connection.execute('SELECT * FROM %s' % table).fetchall()
        for d in lsall:
            resultls.append(list(d))
        return resultls
