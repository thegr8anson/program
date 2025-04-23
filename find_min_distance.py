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

'''
min(iterable, key=None): Data type such as list or set are iterable. (key is optional) 
key : If key function exists, then min() will compare the values calculated by key instead of the elements.
      Then min() will return the element which makes the key function smallest. 
lambda x : (abs(x - one), x) : The lambda function can read each element in the set (or list) one by one
                               until it reach the end of the set (or list), then use the element read to 
                               perform calculations on the right.
                               It will then return a tuple (distance, values) for min() to compare.
                               min() will start with comparing the first element (distance) of the tuples.
                               If there are two results, it will compare the second element (x, which is
                               the original value) of the tuples. 
                               Finally, return the original value x, which generates the smallest tuple.  
'''  

def nearest_value(values: set, one: int) -> int: # 指定回傳值的data type 為 int
    return min(values, key=lambda x: (abs(x - one), x))

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
    
# The other way:
'''
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
'''
    
    