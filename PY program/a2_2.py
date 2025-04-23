#  請將num1,num2 這兩個 list 交集的部分print出來
#  Hint: 用python dictionary 的結構做出hash table 並用以檢查交集的部分
#  nums1=[1,2,3,4,5]
#  nums1_hash={1: True, 2: True, 3: True, 4: True, 5: True}

nums1=[1,2,3,4,5]
nums2=[2,3,4]
result_list = []
dict1 = {}
dict2 = {}
#===================================== code here 
for i in nums1:
    dict1[i] = True
for i in nums2:     
    dict2[i] = True  
for i in nums1:
    if (dict1.get(i) == dict2.get(i)):
        result_list.append(i)                 
#===================================== code here
print(result_list)