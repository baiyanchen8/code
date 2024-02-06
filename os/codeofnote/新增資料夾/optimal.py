def optimal(page_sequence, num_frames):
    page_frames = []  # 存放頁面的列表
    page_faults = 0  # 記錄缺頁數量

    for i, page in enumerate(page_sequence):
        if page not in page_frames:
            page_faults += 1
            if len(page_frames) < num_frames:
                page_frames.append(page)
            else:
                # 找到未來最長時間內不再被使用的頁面
                future_occurrences = {p: page_sequence[i:].index(p) if p in page_sequence[i:] else float('inf') for p in page_frames}
                page_to_replace = max(future_occurrences, key=future_occurrences.get)
                page_frames.remove(page_to_replace)
                page_frames.append(page)

        # print(f"Page: {page} - Page Frames: {page_frames}")

    return page_faults


