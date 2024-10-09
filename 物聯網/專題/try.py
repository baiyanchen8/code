import datetime
import calendar

# 獲取當前日期
current_date = datetime.datetime.now()

# 獲取當前月份的年份和月份
year = current_date.year
month = current_date.month

# 使用calendar模組的monthrange函式獲取當前月份的天數
days_in_month = calendar.monthrange(year, month)[1]

print("當前月份有", days_in_month, "天")

