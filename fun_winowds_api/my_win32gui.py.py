from plyer import notification

# 設定通知的標題、訊息內容和持續時間
title = '通知'
message = '這是一個使用plyer庫發送的通知訊息'
duration = 5  # 持續時間（秒）

# 發送通知
notification.notify(
    title=title,
    message=message,
    timeout=duration
)
