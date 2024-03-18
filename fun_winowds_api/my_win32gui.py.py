import os
from plyer import notification

# 檢測 VS Code 是否正在運行
def is_vscode_running():
    processes = os.popen('tasklist').read()
    return 'controller_viewer.exe' in processes

# 如果 VS Code 正在運行，發送通知
if is_vscode_running():
    title = 'VS Code 啟動通知'
    message = 'Visual Studio Code 已經啟動！'
    duration = 5  # 持續時間（秒）

    # 發送通知
    notification.notify(
        title=title,
        message=message,
        timeout=duration
    )
