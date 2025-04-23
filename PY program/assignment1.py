name = input("請輸入你的名字: ")
sid = input("請輸入你的學號: ")
intro = input("請輸入你的自我介紹: ")
sentence = "我的名字是{}，我的學號是{}."
outcome = sentence.format(name,sid)
print(outcome)
print(intro)