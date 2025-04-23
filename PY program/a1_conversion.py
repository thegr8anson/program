# 輸入一個秒數，請將秒數轉換成 小時 分鐘 秒數

seconds = int(input("請輸入秒數"))
r_hours = seconds // 3600
r_minutes = seconds % 3600 // 60
r_seconds = seconds % 3600 % 60
print(f' {seconds} = {r_hours}小時 {r_minutes}分 {r_seconds}秒')