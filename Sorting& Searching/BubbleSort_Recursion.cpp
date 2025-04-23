#include <iostream>
#include <vector>
using namespace std;
vector<int> bubble_sort(vector<int> nums, int n){
    if (n == 1)  // 在排完倒數第二個時，其實最後一個也排好了。
        return nums;
    for (int i = 0; i < n - 1; i++){ // 由第一個到最後一個，一一讓最大的浮到最後面
        if (nums.at(i) > nums.at(i + 1)) // ps. 一輪中只需要檢查 n - 1 次(最後比到 nums.at(n - 1))
            swap(nums[i], nums[i + 1]);
    }
    return bubble_sort(nums, n - 1);  // 每次需排序部分-1
}

int main()
{
    vector<int> my_vec = {11111, 999, 666, 77, 66, 55, 3, 1};
    vector<int> sorted_vec = bubble_sort(my_vec, my_vec.size());
    for (int i = 0; i < sorted_vec.size(); i++){
        cout << sorted_vec.at(i) << ' ';
    }
    return 0;
}
