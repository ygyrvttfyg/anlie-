'''
1.读取数据
2.排序数据
3.写出数据
'''
from unittest import result


def read_file():
    s=[]
    with open("./学生成绩.txt") as f:
        for line in f:
            line = line[:-1]
            s.append(line.split(","))
        return s

def sort_grades(datas):
    return sorted(datas,key=lambda x: int(x[2]),reverse=True)

def write_file(datas):
    with open("./学生成绩排序版.txt","w") as f:
        for i in datas:
            f.write(",".join(i) + "\n")
# 读取数据
datas = read_file()
# 排序数据
datas = sort_grades(datas)
# 写出数据
write_file(datas)