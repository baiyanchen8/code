from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 設定Chrome WebDriver的路徑
webdriver_path = '/usr/local/bin/chromedriver'

# 設定Chrome WebDriver的選項
chrome_options = Options()
chrome_options.add_argument('--headless')  # 在後台執行，無需顯示瀏覽器視窗
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')

chrome_options.binary_location='/usr/bin/chromedriver'
print("ok")
# 建立 WebDriver
driver = webdriver.Chrome(chrome_options)
print("ok")
# 載入目標網頁
url = "https://opendata.cwa.gov.tw/dataset/forecast?page=1"
driver.get(url)

# 取得網頁內容
html_content = driver.page_source

# 關閉 WebDriver
driver.quit()

# 將 HTML 內容寫入檔案
with open("datapage.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("網頁內容已成功儲存為 datapage.html")

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 找到所有的 <tr> 標籤
rows = soup.find_all('tr')

# 逐一處理每一個 <tr> 標籤
for row in rows:
    # 找到該列中的所有 <td> 標籤
    cells = row.find_all('td')
    # 如果該列有包含 <td> 標籤
    if cells:
        # 第一個 <td> 標籤是資料名稱，第二個是資料編號
        data_name = cells[0].text.strip()
        data_id = cells[1].text.strip()
        # 輸出資料編號和資料名稱
        print(f"資料編號: {data_id}, 資料名稱: {data_name}")
