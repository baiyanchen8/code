import random 
arr=[i for i in range(1,101)]
random.shuffle(arr)
longs = len(arr)
def shell_sort(list):
    n = len(list)
    # 初始步長
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            # 每个步長進行插入排序
            temp = list[i]
            j = i
            # 插入排序
            while j >= 0 and j-gap >= 0 and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        # 得到新的步長
        gap = gap // 2
    return list
print(shell_sort(arr))