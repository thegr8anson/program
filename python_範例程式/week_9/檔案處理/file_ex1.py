# file_ex1.py
name = input('請輸入你的名字:')
s_id = input('請輸入你的學號:')
birth = input('請輸入你的生日:')

# 寫入檔案
f = open('./out.txt', 'a', encoding='utf-8')
f.write('%s\t%s\t%s' %(name, s_id, birth))
f.close()

# 讀取檔案
g = open('./out.txt' , encoding='utf-8')
line = g.readline()
print(line)
g.close()

