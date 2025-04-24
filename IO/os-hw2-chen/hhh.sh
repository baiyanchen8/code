#!/bin/bash

input_file="hw1.log"
output_file="hw1.csv"

echo "MB,Blocking I/O,Non-Blocking I/O,AIO-4,AIO-8,AIO-16,AIO-32" > "$output_file"

current_size=""
blocking=""
nonblocking=""
aio_4=""
aio_8=""
aio_16=""
aio_32=""

while IFS= read -r line; do
    # 抓取檔案大小
    if [[ "$line" =~ ^([0-9]+)MB ]]; then
        # 若前一組測試完成，輸出結果
        if [[ -n "$current_size" ]]; then
            echo "$current_size,$blocking,$nonblocking,$aio_4,$aio_8,$aio_16,$aio_32" >> "$output_file"
        fi
        # 重設變數
        current_size="${BASH_REMATCH[1]}"
        blocking=""
        nonblocking=""
        aio_4=""
        aio_8=""
        aio_16=""
        aio_32=""
    fi

    # 抓取 Blocking I/O
    if [[ "$line" =~ \[Blocking\ I/O\].*([0-9]+\.[0-9]+)\ 秒 ]]; then
        blocking="${BASH_REMATCH[1]}"
    fi

    # 抓取 Non-Blocking I/O
    if [[ "$line" =~ \[Non-Blocking\ I/O\].*([0-9]+\.[0-9]+)\ 秒 ]]; then
        nonblocking="${BASH_REMATCH[1]}"
    fi

    # 抓取 AIO 並發數
    if [[ "$line" =~ \[AIO（並發數\ ([0-9]+)\）\].*([0-9]+\.[0-9]+)\ 秒 ]]; then
        aio_num="${BASH_REMATCH[1]}"
        aio_time="${BASH_REMATCH[2]}"
        case "$aio_num" in
            4) aio_4="$aio_time" ;;
            8) aio_8="$aio_time" ;;
            16) aio_16="$aio_time" ;;
            32) aio_32="$aio_time" ;;
        esac
    fi
done < "$input_file"

# 最後一組也要寫入
if [[ -n "$current_size" ]]; then
    echo "$current_size,$blocking,$nonblocking,$aio_4,$aio_8,$aio_16,$aio_32" >> "$output_file"
fi
