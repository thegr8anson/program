'''
給定一組數字 values（以集合的形式提供）和一個目標數字 one
請實作一個函式 nearest_value，
找到集合中最接近目標數字的元素，並回傳。
若有兩個或以上的數字與目標數字距離相同，則返回其中較小的數字。


Hint:
使用 abs 函數計算數字之間的距離，這樣可以找到集合中和目標數字距離最小的數字。
若有多個數字距離相同，使用 min 函數的參數key，算出set中每個元素的距離

min(values,key=lambda x)
'''

def nearest_value(values: set, one: int) -> int:
#code here
    values = list(values)
    distance = []
    result = []
    
    for i in values:
        distance.append(abs(i - one))
    
    for i in values:
        if(abs(i - one) == min(distance)):
            result.append(i)
    
    result = min(result)                
    return result
#code here


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
    
    # Self-checking asserts
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7   
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1