import random

import win32gui as a

import win32con as b

import win32clipboard as c

msg=[]

n=int(input('你想发多少条消息:'))

qq=int(input('你想要多少内容:'))

for j in range(qq):

    m=input('消息内容:')

    msg.append(m)

    name=input('对方昵称:')

    msg_len=len(msg)-1

for i in range(n+1):

    num=random.randint(0,msg_len)

    c.OpenClipboard()

    c.EmptyClipboard()

    c.SetClipboardData(b.CF_UNICODETEXT,msg[num])

    c.CloseClipboard()

    handle=a.FindWindow(None,name)

if handle != 0:

    a.SendMessage(handle,770,0,0)

    a.SendMessage(handle,b.WM_KEYDOWN,b.VK_RETURN,0

print("发送成功！",i)
