#!/bin/bash

# 輸出標題行
echo "Size (MB), 3,4-4,4-8,4-16,4-32" > output.csv

# 用於收集每個 size 對應的時間數據
size=""
times=()

# 讀取 hw2.log 檔案並提取 size 和執行時間
grep -oP '\d+MB|\[\w+\s*\+\s*Matrix\]\s*執行時間：\d+\.\d{6}' hw2.log | while read -r line; do
    if [[ "$line" =~ ([0-9]+)MB ]]; then
        # 如果是 size 行，將數字提取出來
        if [ ${#times[@]} -gt 0 ]; then
            # 如果有收集到時間，將結果寫入 CSV 文件
            echo "${size}, ${times[0]}, ${times[1]}, ${times[2]}, ${times[3]}, ${times[4]}, ${times[5]}" >> hw2.csv
            # 清空時間數組
            times=()
        fi
        size=${BASH_REMATCH[1]}
    elif [[ "$line" =~ 執行時間：([0-9]+\.[0-9]+) ]]; then
        # 如果是執行時間行，將數字提取出來並加入到時間數組中
        times+=("${BASH_REMATCH[1]}")
    fi
done

# 確保最後一行也寫入
if [ ${#times[@]} -gt 0 ]; then
    echo "${size}, ${times[0]}, ${times[1]}, ${times[2]}, ${times[3]}, ${times[4]}, ${times[5]}" >> hw2.csv
fi
