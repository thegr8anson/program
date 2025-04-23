#include <iostream>
#include <vector>
using namespace std;
vector<int> SelectionSort(int nums[], int n){
    vector<int> answer; 
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
        answer.push_back(nums[i]);
    }
    return answer;
}

int main(){
    int x, n;
    int left = 0;
    int right = 0;
    int food[20];
    cin >> x >> n;
    for (int i = 0; i < n; i++){
        cin >> food[i];
    }    
    vector<int> new_food = SelectionSort(food, n);
    for (int i = 0; i < n; i++){
        if (x > new_food[i]){
            left ++;
        } else {
            right ++;
        }
    }
    if (left > right){
        cout << left << ' ' << new_food[0];
    } else {
        cout << right << ' ' << new_food[n - 1];
    }
    return 0;
}

