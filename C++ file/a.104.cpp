#include <iostream>
using namespace std;
void SelectionSort(int arr[], int n){
    for (int i = 0; i < n - 1; i++){
        int minindex = i;
        for (int j = i + 1; j < n; j++){
            if (arr[j] < arr[minindex]){
                minindex = j;
            }
        }
        int tmp = arr[i];
        arr[i] = arr[minindex];
        arr[minindex] = tmp;
    }
}

int main(){
    int n;
    while (cin >> n){
        int arr[n];
        for (int i = 0; i < n; i++){
            cin >> arr[i];
        }
        SelectionSort(arr, n);
        for (int i = 0; i < n; i++){
            cout << arr[i] << ' ';
        }
    }
    cout << endl;
    return 0;
}