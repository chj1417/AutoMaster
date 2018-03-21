#负责树的数据处理
#负责csv文件与Tree数据对接（仅数据及数据结构）

import csv
from Cmaster.HCore.sqlite2data import DBfile as db

# headtext=['RunOrNot','Tree',"seq", "name", "func", "message",'condition','goto']

def wdata(TreeFile,TreeData,TreeHeader):
    with open(TreeFile, 'w', newline='') as f:
        writer = csv.writer(f)
        headtext = ['RunOrNot', 'Tree']
        headtext.extend(TreeHeader)
        # for row in datas:
        writer.writerow(headtext)

        # 还可以写入多行
        writer.writerows(TreeData)

def rdata(TreeFile):
    data=[]
    with open(TreeFile) as f:
        reader = csv.reader(f)
        # 读取一行，下面的reader中已经没有该行了
        head_row = next(reader)
        for row in reader:
            # 行号从2开始
            data.append(row)
    return data
def rheader(TreeFile):
    with open(TreeFile) as f:
        reader = csv.reader(f)
        # 读取一行，下面的reader中已经没有该行了
        head_row = next(reader)
    return head_row