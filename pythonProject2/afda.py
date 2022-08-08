import os
import json

workingPath = "/home/liu/PycharmProjects/pureSelect/pure_special"
# workingPath = "/home/liu/Downloads/qq-files/1726967050/file_recv/1300-3244"
os.chdir(workingPath)
dirList = os.listdir(workingPath)

# with open("special.txt","r") as file:
#     specialList = file.read().split("\n")

# for dirName in dirList:
#     if not os.path.isdir(dirName):
#         continue
#     fileList = os.listdir(dirName)
#     for item in fileList:
#         if os.path.isdir(dirName + "/" + item):
#             suibian = os.listdir(dirName+"/"+item)
#             for it in suibian:
#                 url = specialList[int(it[:-4])] + "\n"
#                 with open(dirName + "/" + item + "/" + it, "r", encoding="GBK") as file:
#                     content = file.read()
#                 content = url + content
#                 with open(dirName + "/" + item + "/" + it, "w", encoding="UTF-8") as file:
#                     file.write(content)
#         else:
#             url = specialList[int(item[:-4])] + "\n"
#             with open(dirName + "/" + item,"r",encoding="GBK") as file:
#                 content = file.read()
#             content = url + content
#             with open(dirName + "/" + item,"w",encoding="UTF-8") as file:
#                 file.write(content)
#
for dirName in dirList:
    if not os.path.isdir(dirName):
        continue
    urlList = []
    fileList = os.listdir(dirName)
    # fileList.sort(key=lambda x:int(x[:-4]))

    for item in fileList:
        num = 10000  # 编号
        if os.path.isdir(dirName + "/" + item):
            # item.sort(key=lambda x:int(x[:-4]))
            num = 10000  # 编号
            suibian = os.listdir(dirName+"/"+item)
            for it in suibian:
                os.rename(dirName + "/" + item + "/" + it , dirName + "/" + item + "/" + str(num) + ".txt")
                num += 1
        else:
            # fileList.sort(key=lambda x:int(x[:-4]))
            os.rename(dirName + "/" + item, dirName + "/" + str(num) + ".txt")
            num += 1
        #  #### os.rename(dirName + "/" + item, dirName + "/" + str(num) + ".txt")

# for dirName in dirList:
#     urlList = []
#     # if 'readme.md' in fileList:
#     #     fileList.remove('readme.md')
#     fileList = os.listdir(dirName)
#
#     # fileList.sort(key=lambda x:int(x[:-4]))
#     for item in fileList:
#         if os.path.isdir(dirName + "/" + item):
#             item.sort(key=lambda x:int(x[:-4]))
#
#             suibian = os.listdir(dirName + "/" + item)
#             for it in suibian:
#                 with open(dirName + "/" + item + "/" + it, "r") as file:
#                     content = file.readlines()
#                 url = content[0]
#                 with open(dirName + "/" + item + "/" +  "special.txt", "a") as file:
#                     file.write(url)
#                 content = "".join(content[1:])
#                 with open(dirName + "/" + item + "/" + it, "w") as file:
#                     file.write(content)
#         else:
#             fileList.sort(key=lambda x:int(x[:-4]))
#
#             with open(dirName + "/" + item, "r") as file:
#                 content = file.readlines()
#             url = content[0]
#             with open(dirName + "/" + "special.txt", "a") as file:
#                 file.write(url)
#             content = "".join(content[1:])
#             with open(dirName + "/" + item, "w") as file:
#                 file.write(content)



# 空格不算一行，注释不算，整个if for while等块算一行其中的内容每行另算
