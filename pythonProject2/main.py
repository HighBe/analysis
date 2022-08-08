import xlrd
import os
import function
import openpyxl as op
import json


if __name__ == "__main__":
    #要先使用第一条语句生成存放链接的文件，再批量生成网页
    # function.collectLink("/home/liu/PycharmProjects/pureSelect/special/改变变量顺序","/home/liu/PycharmProjects/pureSelect/special.txt")
    #批量生成网页
    # function.generateHtml("/home/liu/PycharmProjects/pureSelect/special/改变变量顺序","/home/liu/PycharmProjects/pureSelect/special.txt")

    #统计emit占总行数的比例
    # path = "/home/liu/PycharmProjects/pythonProject2/case"
    # os.chdir(path)
    # all_file = os.listdir(path)
    # wb = op.Workbook()#创建工作簿对象
    # ws = wb['Sheet']#创建字表
    # ws.append(['项目名','总行数','emit数','emit数/总行数','总行数/emit数'])#添加表头
    # i = 0
    # for obj in all_file:#遍历目录下的每一个项目
    #     if os.path.isdir(obj):
    #         count = [0] #直接使用整数类型是传递参数，要传引用就要用数组
    #         emitcount = [0]
    #         current_path = os.path.join(path,obj)
    #         function.traversal(current_path,count,emitcount)#统计当前项目中总行数和emit数
    #         d = obj,count[0],emitcount[0],(emitcount[0]/count[0] if(count[0] != 0) else -1),(count[0]/emitcount[0] if(emitcount[0] != 0) else-1)
    #         ws.append(d)#每次写入xlsx表格一行
    # wb.save("/home/liu/PycharmProjects/pythonProject2/{}.xlsx".format('amount'))#将生成的xldx表格存放到制定的目录下


    #统计收藏数
    # path = "/home/liu/PycharmProjects/SolidityWorm/Repositories"
    # function.countstar(path)

    #统计emit改动次数
    path = "D:/Tool/Tool/PyCharm Community Edition 2022.2/Code/case/case"
    function.changepercent(path)

    # content = open(path + "/0age Spawner/1b342afda0c1ec47e6a2d65828a6ca50f0a442fe.json","r")
    # strings = content.read()
    # jsonStr = json.loads(strings)
    # t = 'patch' in jsonStr.keys()
    # tmpStr = jsonStr['files'][0]['patch'].replace(' ', '')
    # lines = tmpStr.split('\n')  # 将文件修改的patch信息用列表lines来存储
    # print(len(jsonStr['files']))


