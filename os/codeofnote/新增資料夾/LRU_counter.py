def lru_counter(page_sequence, num_frames):
    page_frames = [0 for i in range(num_frames)]  # 存放頁面的列表
    page_faults = 0  # 記錄缺頁數量
    unique_set = set(page_sequence)
    unique_list = list(unique_set)
    page_time = [-1 for i in range(num_frames)]  # 用於記錄頁面的使用順序，包含頁面號碼和時間戳的 tuple
    k=0
    for time in range(len(page_sequence)):
            # 如果頁面已存在，更新對應的時間戳
        if page_sequence[time] in page_frames:
            index = page_frames.index(page_sequence[time])
            page_time[index] = time
            page_in = True
        else:
            page_in = False
            page_faults += 1
        for i in range(num_frames):
            if page_frames[i] == 0:
                # 找到第一個值為零的位置，插入新的頁面
                page_frames[i] = page_sequence[time]
                page_time[i] = time
                page_in = True
                break

        if not page_in:
            # 所有頁面都已佔滿，需要替換最近最少使用的頁面
            min_time = min(page_time)
            min_index = page_time.index(min_time)
            page_frames[min_index] = page_sequence[time]
            page_time[min_index] = time
            


    return page_faults