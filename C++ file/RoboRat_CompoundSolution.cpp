#include <iostream>
using namespace std;
void CompoundSolution(int nums[], int n, int x){ 
    int left = 0;
    int right = 0;
    for (int i = 0; i < n; i++){
        int index = i;
        for (int j = 1 + i; j < n; j++){
            if (nums[j] < nums[index]){
                index = j;
            }
        }
        if (index != i){
            swap(nums[i], nums[index]);
        }
    }
    for (int i = 0; i < n; i++){
        if (x > nums[i]){
            left ++;
        } else {
            right ++;
        }
    }
    if (left > right){
        cout << left << ' ' << nums[0];
    } else {
        cout << right << ' ' << nums[n - 1];
    }
}

int main(){
    int x, n;
    int food[20];
    cin >> x >> n;
    for (int i = 0; i < n; i++){
        cin >> food[i];
    }    
    CompoundSolution(food, n, x);
    return 0;
}
