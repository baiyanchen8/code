import cv2

# 打開攝像頭
cap = cv2.VideoCapture(3)

# 檢查攝像頭是否成功打開
if not cap.isOpened():
    print("無法打開攝像頭")
    exit()

while True:
    # 從攝像頭讀取影像
    ret, frame = cap.read()

    # 如果讀取成功，顯示影像
    if ret:
        cv2.imshow('Camera', frame)

    # 按下 ESC 鍵退出迴圈
    if cv2.waitKey(1) == 27:
        break

# 釋放攝像頭資源並關閉視窗
cap.release()
cv2.destroyAllWindows()
