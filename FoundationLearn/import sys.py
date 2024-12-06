import ctypes
import win32gui
import win32ui
import win32con
from PIL import Image

def screenshot_window_by_handle(hwnd):
    # 获取设备上下文
    hwndDC = win32gui.GetWindowDC(hwnd)  # <-- Win32 API
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)  # <-- Win32 API
    saveDC = mfcDC.CreateCompatibleDC()  # <-- Win32 API

    # 获取窗口的矩形区域
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)  # <-- Win32 API
    width = right - left
    height = bottom - top

    # 创建一个位图对象
    saveBitmap = win32ui.CreateBitmap()  # <-- Win32 API
    saveBitmap.CreateCompatibleBitmap(mfcDC, width, height)  # <-- Win32 API
    saveDC.SelectObject(saveBitmap)  # <-- Win32 API

    # 将窗口的内容拷贝到位图对象
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)  # <-- Win32 API

    # 将位图保存为PIL Image对象
    bmpinfo = saveBitmap.GetInfo()  # <-- Win32 API
    bmpstr = saveBitmap.GetBitmapBits(True)  # <-- Win32 API
    img = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)

    # 清理对象
    saveDC.DeleteDC()  # <-- Win32 API
    win32gui.DeleteObject(saveBitmap.GetHandle())  # <-- Win32 API
    win32gui.ReleaseDC(hwnd, hwndDC)  # <-- Win32 API

    return img

def capture_minimized_window(window_title):
    # 找到窗口句柄
    hwnd = win32gui.FindWindow(None, window_title)  # <-- Win32 API
    if hwnd:
        # 截图
        img = screenshot_window_by_handle(hwnd)
        img.save("screenshot.png")
        print("截图已保存！")
    else:
        print("未找到指定的窗口，请确认窗口标题是否正确。")

# 替换为你要截图的窗口的标题
window_title = "Clash for Windows"  # 示例: "记事本"
capture_minimized_window(window_title)
