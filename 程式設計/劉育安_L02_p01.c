#include <stdio.h>

int majorityElement(int[], int);  

int main() {

    int nums1[] = {1, 1, 2, 3, 4, 6, 1, 1, 1};
    int numsSize1 = sizeof(nums1) / sizeof(nums1[0]);

    printf("nums1[]=%d\n", majorityElement(nums1, numsSize1)); 

    
    int nums2[] = {2, 2, 1, 1, 1, 2, 2, 3, 8, 2, 2, 2, 7};
    int numsSize2 = sizeof(nums2) / sizeof(nums2[0]);

    printf("nums2[]=%d\n", majorityElement(nums2, numsSize2)); 
    return 0;
}

int majorityElement(int nums[], int numSize) { 
/*請務必寫上註解*/
    int i, j;    
    //  第一層迴圈說明最多執行次數等於陣列元素數量
    for(i = 0; i < numSize; i++){
        int count = 0;
        //  第二層迴圈遍歷陣列，計算與nums[i]相同元素的數量
        for (int j = 0; j < numSize; j++){
            if (nums[j] == nums[i])
                count ++;
                //  若發現元素數量滿足條件則立即回傳，脫離迴圈
                if (count > numSize / 2)
                    return nums[i];
        }
    }
}
