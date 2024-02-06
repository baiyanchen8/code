def fifo(page_sequence, num_frames):
    page_frames = []  # 存放頁面的列表
    page_faults = 0  # 記錄缺頁數量

    for page in page_sequence:
        if page not in page_frames:
            page_faults += 1
            if len(page_frames) < num_frames:
                page_frames.append(page)
            else:
                page_frames.pop(0)  # FIFO，移除最早進入的頁面
                page_frames.append(page)

        # print(f"Page: {page} - Page Frames: {page_frames}")

    return page_faults

def tmp(page_sequence, num_frames, *args):
    for arg in args:
        total_page_faults = arg(page_sequence, num_frames)
        k=f"{str(total_page_faults).zfill(3)}"
        print(f"{arg.__name__}: {k}", end="\t")
    print()
# 測試
import random
import optimal
import LRU_stack
import LRU_counter
k=20
page_sequence= [random.randint(3,k) for i in range(10*k)]

count= [0 for i in range(k+1)]
for i in page_sequence:
    count[i]+=1
print(count)
for num_frames in range(2,20):
    k=f"{str(num_frames).zfill(2)}"
    print(f"{k}",end=" ")
    tmp(page_sequence,num_frames,fifo,optimal.optimal,LRU_stack.lru_stack,LRU_counter.lru_counter)
   
    
# tmp(page_sequence,11,LRU_stack.lru_stack)