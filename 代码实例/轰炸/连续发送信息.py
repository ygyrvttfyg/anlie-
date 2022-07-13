'''
项目:代码实例
文件名:连续发送信息
制作人:"黄涛"
date:2022/4/4
'''
from pynput.keyboard import Key, Controller as key
from pynput.mouse import Button, Controller as mouse_el
import time

def send():
    keyboard = key()  # 获取键盘权限
    mouse = mouse_el()  # 获取鼠标权限

    mouse.press(Button.left)  # 鼠标左键点击
    mouse.release(Button.left)  # 鼠标左键松开
    time.sleep(5)  #程序运行等待五秒

    #读取test.txt文件中的内容
    f = open("test.txt", "r", encoding="utf-8")
    #循环遍历输出test.txt文件的内容
    for line in f:
        #判空处理
        if line in ['\n', '\r\n']:
            pass
        #空行直接跳过
        elif line.strip() == "":
            pass
        else:
            time.sleep(1) #程序运行等待0.5秒
            keyboard.type(line.rstrip())  # 输入框的内容
            keyboard.press(Key.enter)  # 回车键按下
            keyboard.release(Key.enter)  # 回车键松开
            print(line.rstrip())  # 消除每一行的末尾的换行符
    f.close()

#主函数
if __name__ == '__main__':
    send()

