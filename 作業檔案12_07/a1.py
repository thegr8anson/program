'''
a1.py 
請完成 sum2()、rsum()
題目敘述在課程簡報
'''

def sum2(n):
    # step1: 若n≤0，回傳-1
    # step2: 若n=1，回傳2
    # step3: 用遞迴方式計算 2 + 4 + 6 + … 2n 的和
    # step4: 回傳計算結果
    ######## code here ########
    if(n <= 0):
        return -1
    elif(n == 1):
        return 2
    else:
        return 2 * n + sum2(n - 1)
    ######## code here ########

def rsum(n):
    # step1: 若n≤0，回傳-1
    # step2: 若n=1，回傳1
    # step3: 若n=2，回傳1*2
    # step4: 用遞迴方式計算 1*2 + 2*3 + 3*4 + … + (n-1)*n 的和
    # step5: 回傳計算結果
    ######## code here ########
    if (n <= 0):
        return -1
    elif (n == 1):
        return 1
    elif (n == 2):
        return 1 * 2
    else:
        return (n - 1) * n + rsum(n - 1)
    ######## code here ########

if __name__ == '__main__':
    # Self-checking asserts
    assert sum2(0) == -1
    assert sum2(1) == 2
    assert sum2(2) == 6
    assert sum2(3) == 12
    assert sum2(5) == 30
    #----------------------------
    assert rsum(-1) == -1
    assert rsum(0) == -1
    assert rsum(1) == 1
    assert rsum(2) == 2
    assert rsum(3) == 8
    assert rsum(4) == 20
    assert rsum(5) == 40
    assert rsum(10) == 330
    print("All correct")