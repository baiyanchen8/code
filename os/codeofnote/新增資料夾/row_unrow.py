import time
import numpy as np

# 測試不連續存取二維陣列的函式
def test_random_access_2d(data):
    rows, cols = data.shape
    start_time = time.time()
    for j in range(rows):
        for i in range(cols):
            value = data[i, j]
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

# 測試連續存取二維陣列的函式
def test_continuous_access_2d(data):
    rows, cols = data.shape
    start_time = time.time()
    for i in range(rows):
        for j in range(cols):
            value = data[i, j]
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

# 主程式
if __name__ == "__main__":
    # 設定測試資料大小
    rows, cols = 10000, 10000

    # 產生測試資料，這裡使用NumPy的隨機數生成
    data = np.random.rand(rows, cols)

    # 測試不連續存取二維陣列的時間
    random_access_time = test_random_access_2d(data)
    print(f"not continue : {random_access_time} sec")

    # 測試連續存取二維陣列的時間
    continuous_access_time = test_continuous_access_2d(data)
    print(f"continue: {continuous_access_time} sec")
