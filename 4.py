#先通过这个找到需要点击的位置

import pyautogui as gui

screenWidth, screenHeight = gui.size()#以双整数元组的形式返回屏幕的(宽度，高度)以像素为单位

currentMouseX, currentMouseY = gui.position()

# '''

# 以双整数元组的形式返回鼠标指针的当前xy坐标。Args: x (int, None, optional)

# ——如果没有，这个参数将覆盖返回值中的x。y (int, None, optional)

# ——如果不是None，这个参数将覆盖返回值中的y。返回:(x, y)鼠标当前xy坐标的元组。注意:position() functon不检查故障保险。

# '''

print(screenWidth, screenHeight )

print(currentMouseX, currentMouseY )

#在将位置改完之后在运行以下代码

import tkinter

from tkinter import messagebox

from tkinter import ttk

import pyautogui as gui

import time

def run():

time.sleep(2)

gui.hotkey('Alt', 'Tab')

gui.click(951, 685)#点击表情包的位置(要更改)

time.sleep(0.6)

gui.click(967, 330)#点击要发送的表情的位置(要更改)

gui.click(953, 695)#点击信息栏的位置(要更改)

time.sleep(0.2)

gui.hotkey('ctrl', 'c')

time.sleep(0.2)

gui.hotkey('ctrl', 'enter')

for i in range(4):

    gui.hotkey('ctrl', 'v')

    time.sleep(0.2)

    gui.hotkey('ctrl', 'enter')

def take():

    time.sleep(2)

    gui.hotkey('Alt', 'Tab')

    gui.click(951, 685)#点击表情包的位置(要更改)

    time.sleep(0.6)

    gui.click(967, 330)#点击要发送的表情的位置(要更改)

    gui.click(953, 695)#点击信息栏的位置(要更改)

    time.sleep(0.2)

    gui.hotkey('ctrl', 'c')

    time.sleep(0.2)

    gui.hotkey('ctrl', 'enter')

for i in range(4):

    gui.hotkey('ctrl', 'v')

    time.sleep(0.2)

    gui.hotkey('ctrl', 'enter')

def reu(s):

    print(s)

if s=='qq':

    run()#运行QQ轰炸

elif s=='wei':

    take()#运行微信轰炸

    rook=tkinter.Tk()

    rook   .title('微信轰炸')#界面名称

    rook.geometry('450x300')#界面大小

#

comvalue = tkinter.StringVar() # 窗体自带的文本，新建一个值

comboxlist = ttk.Combobox(rook, width=12,textvariable=comvalue)# 初始化

comboxlist["values"] = ('qq','wei')#下拉框中的值

comboxlist.current(0) # 选择第一个

comboxlist.bind("<>", reu) # 绑定事件,(下拉列表框被选中时，绑定go()函数)

#绑定事件,(下拉列表框被选中时，绑定func()函数)

comboxlist.pack()

tkinter.Label(rook,text='请输入：',font=("黑体",10, "bold"),bg='Yellow').pack()

# 绑定变量

e = tkinter.Variable()

entry2 = tkinter.Entry(rook, textvariable=e)#输入内容

entry2.pack()

# e就代表输入框这个对象

# 设置值

b1=tkinter.Button(rook,text='运行',font=("黑体",11, "bold"),command=lambda : reu(entry2.get())).pack()

#输入的内容entry2.get())

rook.mainloop()