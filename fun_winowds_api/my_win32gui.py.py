import tkinter as tk
import win32gui
import win32con

def set_topmost(window):
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(window, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# 建立主視窗
root = tk.Tk()
root.title("永遠最上層的桌面工具")

# 隱藏視窗
root.withdraw()

# 設置視窗永遠最上層
set_topmost(root.winfo_id())

# 啟動主迴圈
root.mainloop()
