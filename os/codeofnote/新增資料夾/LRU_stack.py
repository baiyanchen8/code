def lru_stack(page_sequence, num_frames):
    page_faults = 0  # 記錄缺頁數量
    page_stack = []

    for page in page_sequence:
        # 檢查頁面是否在緩存中
        if page in page_stack:
            # 如果頁面已經在緩存中，將其移到堆疊頂部，表示最近使用
            page_stack.remove(page)
            page_stack.append(page)
        else:
            page_faults += 1  # 發生缺頁
            # 如果頁面不在緩存中，檢查緩存是否已滿
            if len(page_stack) >= num_frames:
                # 如果緩存已滿，移除堆疊底部的頁面（最久未使用）
                page_stack.pop(0)
            # 將新頁面添加到堆疊頂部
            page_stack.append(page)
    return page_faults
