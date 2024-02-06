def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = round(left + (right - left) / 2)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # 如果目标元素不在数组中，返回 -1


arr=[i for i in range(0,100,3)]
print(arr)
print(binarySearch(arr,33))