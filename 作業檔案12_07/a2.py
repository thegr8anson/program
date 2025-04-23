'''
a2.py
請完成 f()、g()
題目敘述在課程簡報
'''

def f(number):
    # step1: 計算總和
    # step2: 丟回g()
    ######## code here ########
    if (number == 0):
        return 0
    return number % 10 + f(number // 10)
    ######## code here ########

def g(number):
    # step1: 檢查number是不是個位數
    # step2: 若不是個位數，就丟到f()繼續計算加總
    ######## code here ########
    number = f(number)
    if (number < 10):
        return number
    return g(number)
    ######## code here ########

if __name__ == '__main__':    
    # Self-checking asserts
    assert g(1234567892) == 2 
    assert g(2461552837723) == 1 
    assert g(883518202512) == 9
    assert g(92816645754233123) == 8

    print("All corrrect")