#  請將num1,num2 這兩個 list 交集的部分print出來
#  Hint: 用python dictionary 的結構做出hash table 並用以檢查交集的部分
#  nums1=[1,2,3,4,5]
#  nums1_hash={1: True, 2: True, 3: True, 4: True, 5: True}

nums1=[1,2,3,4,5]
nums2=[2,3,4]
result_list = []

#===================================== code here
nums1_dict = {num: True for num in nums1}

    
for num in nums2:
    if num in nums1_dict:
        result_list.append(num)
    
#===================================== code here


print(result_list)