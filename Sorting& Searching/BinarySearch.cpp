# include <iostream>
# include <vector>
using namespace std;

int BinarySearch(vector<int> nums, int target){
    int left = 0;
    int right = nums.size() - 1;
    int mid = (left + right) / 2;
    while (left <= right){
        if (nums[mid] == target)
            return mid;
        else if (nums[mid] > target)
            right = mid - 1;
        else
            left = mid + 1;
        mid = (left + right) / 2;
    }
    return -1;
}

int main(){
    vector<int> number = {0, 22, 55, 99, 777, 999, 10000};
    int target;
    cin >> target;
    cout << BinarySearch(number, target);
    return 0;
}