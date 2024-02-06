count=0
def hanoi(n, source, target, auxiliary):
    global count
    
    if n > 0:
        count+=1
        # 将 n-1 个圆盘从源杆移动到辅助杆
        hanoi(n-1, source, auxiliary, target)
        
        # 将第 n 个圆盘从源杆移动到目标杆
        print(f"Move disk {n} from {source} to {target}")
        # 将 n-1 个圆盘从辅助杆移动到目标杆
        hanoi(n-1, auxiliary, target, source)
# 测试
n = 17  # 圆盘的数量
hanoi(n, 'A', 'C', 'B')
print(count)
