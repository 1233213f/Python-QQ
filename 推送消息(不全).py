import win32gui
import win32api
from win32.lib import win32con
import win32clipboard as w
import time
from threading import Lock
import traceback
import ctypes
from ctypes import wintypes
import pythoncom
mutex = Lock()


def send(send_mess, group_name):
    try:
        mutex.acquire()
        # TXGuiFoundation
        win = win32gui.FindWindow(None, group_name)	# 群组名称 or 人名
        w.OpenClipboard()
        w.EmptyClipboard()
        if type(send_mess) == str:
        	# 文本消息
            w.SetClipboardData(win32con.CF_UNICODETEXT, send_mess)	# 需要发送的消息
            w.CloseClipboard()
            # time wait pywintypes.error: (1418, 'GetClipboardData',线程没有打开的剪贴板)
            time.sleep(1)
            win32gui.SendMessage(win, 770, 0, 0)
            win32gui.SendMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        elif type(send_mess) == bytes:
        	# 文件消息
            w.SetClipboardData(w.CF_HDROP, send_mess)
            time.sleep(1)
            win32api.PostMessage(win, win32con.WM_PASTE, 0, 0)
            time.sleep(1)
            win32gui.SendMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
            mutex.release()
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())


class DROP(ctypes.Structure):
    _fields_ = (('pFiles', wintypes.DWORD),
                ('pt',     wintypes.POINT),
                ('fNC',    wintypes.BOOL),
                ('fWide',  wintypes.BOOL))


def clip_files(file_list, group_name):
    try:
        offset = ctypes.sizeof(DROP)
        length = sum(len(p) + 1 for p in file_list) + 1
        size = offset + length * ctypes.sizeof(ctypes.c_wchar)
        buf = (ctypes.c_char * size)()
        df = DROP.from_buffer(buf)
        df.pFiles, df.fWide = offset, True
        for path in file_list:
            array_t = ctypes.c_wchar * (len(path) + 1)
            path_buf = array_t.from_buffer(buf, offset)
            path_buf.value = path
            offset += ctypes.sizeof(path_buf)
        stg = pythoncom.STGMEDIUM()
        stg.set(pythoncom.TYMED_HGLOBAL, buf)
        send(stg, group_name)
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())


clip_files("1.txt",name)
win32api.keybd_event(0x91, 0, 0, 0)  # 0x91 --> win key
win32api.keybd_event(0x2C, 0, 0, 0)  # 0x2C --> PRINT SCREEN key
win32api.keybd_event(0x91, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(0x2C, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)
win32gui.SendMessage(win, 770, 0, 0)
win32gui.SendMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
win = win32gui.FindWindow(None, group_name)	# 群组名称 or 人名
w.OpenClipboard()
w.EmptyClipboard()
w.SetClipboardData(win32con.CF_UNICODETEXT, str(mess))	# 需要发送的消息
w.CloseClipboard()
time.sleep(1)
win32gui.SendMessage(handle, 770, 0, 0)
if result.startswith('@'):
	# 睡1s模拟人工@方式
    time.sleep(1)
    win32gui.SendMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(1)
    win32gui.SendMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
