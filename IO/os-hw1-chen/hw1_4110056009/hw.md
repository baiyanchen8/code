# 實驗流程
## HW1 （使用fwrite fread....）
```c
create_file();             // 建立 100MB 測試檔案
sequential_read();         // 測試順序讀取(每次讀取 4KB）
sequential_write();        // 測試順序寫入(每次寫入 2KB 並 fsync）
random_read();             // 測試隨機讀取
random_buffered_write_1(); // 測試隨機緩衝寫入（不立即 fsync）
random_buffered_write_2(); // 測試隨機緩衝寫入（每次寫入後立即 fsync）
```

### result
``` text
100MB 檔案已建立。
順序讀取時間：0.030928 秒
順序寫入時間：149.279788 秒
隨機讀取時間：0.050751 秒
隨機緩衝寫入（不立即同步）：0.452392 秒
隨機緩衝寫入（每次同步）：203.673432 秒
```

## erase cache
```Bash
su root
echo 3 > /proc/sys/vm/drop_caches
exit
```

## HW2(使用 Read write....)
```c
create_test_file();               // 建立 100MB 測試檔案
measure_sequential_read();        // 測量順序讀取
measure_sequential_write();       // 測量順序寫入
measure_random_read();            // 測量隨機讀取
measure_random_buffered_write_1();// 測量隨機緩衝寫入（無同步）
measure_random_buffered_write_2();// 測量隨機緩衝寫入（每次寫入後立即同步）
```

### result
``` text
100MB 檔案已建立。
順序讀取時間： 0.028579 seconds
順序寫入時間： 128.129814 seconds
隨機讀取時間: 0.096665 seconds
隨機緩衝寫入（無同步）時間: 0.942310 seconds
隨機緩衝寫入（每次同步）時間: 180.121076 seconds
```

## erase cache
```Bash
su root
echo 3 > /proc/sys/vm/drop_caches
exit
```

## HW3(使用mmap)
```c
create_test_file();
mmap_sequential_read();
mmap_sequential_write();
mmap_random_read();
mmap_random_buffered_write_1();
mmap_random_buffered_write_2();
```

### result
```text
100MB 檔案已建立。
順序讀取(mamap)時間： 0.272896 seconds
順序寫入(mmap)時間: 56.040899 seconds
隨機讀取(mmap)時間： 0.040676 seconds
隨機緩衝寫入（不立即同步)：0.332220 seconds
隨機緩衝寫入（每次同步）：110.445688 seconds
```

# 分析
這份實驗資料相當完整，涵蓋了使用三種不同方式（`fread/fwrite`、`read/write`、`mmap`）來做 I/O 測試，並對應了順序讀/寫、隨機讀/寫（含同步與不同步）等操作。下面我來幫你做一份清楚的分析，並用台灣常用的說法呈現：

---

## 📊 整體結果彙整比較表：

| 測試項目 | `fread/fwrite` | `read/write` | `mmap` |
|----------|----------------|--------------|--------|
| 順序讀取 | 0.0309s        | 0.0286s      | **0.2729s** ❗ |
| 順序寫入 | 最慢：149.28s  | 128.13s      | **56.04s** ✅ |
| 隨機讀取 | **0.0508s**    | 0.0967s      | 0.0407s ✅ |
| 隨機寫入（不同步） | 0.452s     | 0.942s       | **0.332s** ✅ |
| 隨機寫入（每次同步） | 最慢：203.67s | 180.12s  | **110.45s** ✅ |

---

## 🔍 各實驗結果分析

### ✅ **1. 順序讀取（sequential read）**
- `fread` / `read` 的效能非常接近（皆 < 0.03s），這是因為 Linux 有效使用了 **page cache**，順序存取會預讀（readahead），效率很好。
- `mmap` 反而最慢（0.27s），原因可能是因為要使用`mmap`映射反而有 **Overhead**

### ✅ **2. 順序寫入（sequential write）**
- `fwrite` 最慢（149s），`write` 也很慢（128s），但 `mmap` 最快（56s）。
- 為什麼 `mmap` 寫入快？
  - 因為 `mmap` 寫入時是直接修改記憶體，不會馬上觸發 `write()` 系統呼叫，只要最後一併 `msync()` 寫入即可，系統可以優化寫入動作。
  - 而 `write/fwrite` 每次呼叫都會觸發系統呼叫，`fsync()` 又會強制寫入磁碟，開銷大。

### ✅ **3. 隨機讀取（random read）**
- `mmap` 與 `fread` 的表現都非常好（0.04~0.05s），`read` 略慢（0.096s）。
- 可能是因為 `fread` 本身就有內建的緩衝區（buffering），可幫忙減少系統呼叫次數。

### ✅ **4. 隨機寫入（不同步）**
- `mmap` 依然最快（0.33s），`fwrite` 約 0.45s，`write` 約 0.94s。
- 主因：
  - `fwrite` 會累積到緩衝區才寫出，效率不錯。
  - `mmap` 直接記憶體修改，效率最高。
  - `write` 每次都會進入核心，效率最差。

### ✅ **5. 隨機寫入（每次同步）**
- `fwrite` 最慢（203s），`write` 次之（180s），`mmap` 最快（110s）。
- 差異關鍵在於 **fsync/msync** 頻率與效能：
  - `fsync` 每次強制寫入磁碟，成本非常高。
  - `mmap` 的 `msync` 寫入通常能整批同步，比較有效率。
