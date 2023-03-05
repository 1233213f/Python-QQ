import win32gui
import win32con
import win32clipboard as w
import time


def send(name, msg):
    # 打开剪贴板
    w.OpenClipboard()
    # 清空剪贴板
    w.EmptyClipboard()
    # 设置剪贴板内容
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    # 获取剪贴板内容
    date = w.GetClipboardData()
    # 关闭剪贴板
    w.CloseClipboard()
    # 获取qq窗口句柄
    handle = win32gui.FindWindow(None, name)
    if handle == 0:
        print('未找到窗口！')
    # 显示窗口
    win32gui.ShowWindow(handle, win32con.SW_SHOW)
    # 把剪切板内容粘贴到qq窗口
    win32gui.SendMessage(handle, win32con.WM_PASTE, 0, 0)
    # 按下后松开回车键，发送消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    time.sleep(0)  # 延缓进程


def main():
    time.sleep(3)
    #m=input("请输入窗口名字(和谁聊天)：")
    name = '上•下'  # QQ聊天窗口的名字
    print('开始')
    for i in range(0, 100):
        time.sleep(1)
        send(name, '第' + str(i) + '哦！')
        t = str('哦!')
        j = 1
        while j<=i:
            t = t + t
            send(name,t)
            j+=1
    print('结束')


main()
