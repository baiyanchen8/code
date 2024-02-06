import threading

class PetersonSolution:
    def __init__(self):
        self.flag = [False, False]  # 兩個執行緒的標誌
        self.turn = 0  # 用於指示輪到哪個執行緒進入臨界區

    def enter_critical_section(self, thread_id):
        other_thread = 1 - thread_id
        self.flag[thread_id] = True
        self.turn = thread_id

        while self.flag[other_thread] and self.turn == thread_id:
            pass  # 等待直到對方執行緒的標誌變為False並且是自己的輪到

    def leave_critical_section(self, thread_id):
        self.flag[thread_id] = False

# 測試程式碼
def critical_section(thread_id, ps):
    print(f"Thread {thread_id} is entering the critical section.")
    # 在臨界區執行一些任務
    print(f"Thread {thread_id} is leaving the critical section.")

# 使用Peterson's Solution的兩個執行緒
ps = PetersonSolution()
thread0 = threading.Thread(target=critical_section, args=(0, ps))
thread1 = threading.Thread(target=critical_section, args=(1, ps))

# 啟動執行緒
thread0.start()
thread1.start()

# 等待執行緒完成
thread0.join()
thread1.join()

print("Execution completed.")
