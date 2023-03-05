import time

from tkinter import *

from PIL import Image, ImageTk

import win32gui

import win32con

import win32clipboard


def set_message(window_name, message):
    global failed  # 将failed申明为全局变量，因为后面会在函数外用到该变量

    win = win32gui.FindWindow(None, window_name)  # 找到指定联系人窗口的句柄

    if win != 0:  # 判断是否找到

        win32gui.SetForegroundWindow(win)  # 找到了就建立该窗口

        failed = False

    else:

        failed = True

    win32clipboard.OpenClipboard()  # 打开剪贴板

    win32clipboard.EmptyClipboard()  # 清空剪贴板

    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, message)  # 设置剪贴板

    win32clipboard.CloseClipboard()  # 关闭剪贴板

    win32gui.ShowWindow(win, win32con.WM_SHOWWINDOW)  # 显示窗口

    win32gui.SendMessage(win, win32con.WM_PASTE, 0, 0)  # 相当于粘贴

    win32gui.SendMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)  # 模拟按下Enter键

    win32gui.SendMessage(win, win32con.WM_KEYUP, win32con.VK_RETURN, 0)  # 模拟松开


def send():  # 发送消息的函数

    window_name = entry1.get()  # 获取输入框中的信息

    message = entry2.get()

    times = entry3.get()

    sleep_time = entry4.get()

    if sleep_time == '':  # 设置默认间隔时长

        sleep_time = 0

    if times and window_name and message != '':  # 判断是否输入了完整内容

        for i in range(int(times)):
            time.sleep(int(sleep_time))  # 根据间隔时长来停止程序

            set_message(window_name, message)  # 运行建立消息函数发送消息

        if failed:  # 判断是否找到了窗口句柄

            label7.place_forget()  # 隐藏其他该位置的组件

            label5.place_forget()

            label6.place(x=30, y=445, width=340, height=20)  # 显示当前需要显示的组件

        else:

            label7.place_forget()

            label6.place_forget()

            label5.place(x=140, y=445, width=120, height=50)

    else:

        label7.place(x=100, y=440, width=200, height=30)


root = Tk()  # 应用界面为root

image_name = Image.open('1.jpg')  # 打开准备好的背景图片

root.title('消息轰炸机')  # 给窗口命名

root.geometry('400x500+50+50')  # 设置窗口大小及位置

canvas_root = Canvas(root, width=400, height=500)  # 创建画布

im_root = ImageTk.PhotoImage(image_name)  # 预设打开的图片

canvas_root.create_image(200, 250, image=im_root)  # 嵌入预设的图片

canvas_root.pack()  # 将画布显示出来

label1 = Label(root, text='联系人', font=('宋体', 20), fg='blue', bg='pink')  # 设置组件

label2 = Label(root, text='消息内容', font=('宋体', 20), fg='blue', bg='pink')

label3 = Label(root, text='发送次数', font=('宋体', 20), fg='blue', bg='pink')

label4 = Label(root, text='间隔时长(默认为0秒)', font=('宋体', 20), fg='blue', bg='pink')

label5 = Label(root, text='发送成功', font=('宋体', 20), fg='green')

label6 = Label(root, text='发送失败,请打开与该联系人的聊天框', font=('宋体', 15), fg='red')

label7 = Label(root, text='未完整输入信息', font=('宋体', 20), fg='red', bg='black')

label1.place(x=150, y=25, width=100, height=50)

label2.place(x=140, y=115, width=120, height=50)

label3.place(x=140, y=205, width=120, height=50)

label4.place(x=70, y=295, width=260, height=50)

entry1 = Entry(root, font=('宋体', 20))  # 设置输入框

entry2 = Entry(root, font=('宋体', 20))

entry3 = Entry(root, font=('宋体', 20))

entry4 = Entry(root, font=('宋体', 20))

entry1.place(x=50, y=80, width=300, height=30)  # 显示组件

entry2.place(x=50, y=170, width=300, height=30)

entry3.place(x=50, y=260, width=300, height=30)

entry4.place(x=50, y=350, width=300, height=30)

button = Button(root, text='发送', font=('宋体', 20), fg='black', bg='green', command=send)  # 设置按钮

button.place(x=170, y=385, width=60, height=50)  # 显示按钮

root.mainloop()
