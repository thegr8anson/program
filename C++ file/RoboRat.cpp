#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int x, n;
    int left = 0;
    int right = 0;
    int food[20];
    cin >> x >> n;
    for (int i = 0; i < n; i++){
        cin >> food[i];
    }    
    sort(food, food + n);
    for (int i = 0; i < n; i++){
        if (x > food[i]){
            left ++;
        } else {
            right ++;
        }
    }
    if (left > right){
        cout << left << ' ' << food[0];
    } else {
        cout << right << ' ' << food[n - 1];
    }
    return 0;
}