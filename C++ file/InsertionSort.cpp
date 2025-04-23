#include <iostream>
using namespace std;
void InsertionSort(int arr[], int n){
    for (int i = 1; i < n; i++){
        int insert_element = arr[i];
        int j = i - 1;
        while (j >= 0 && insert_element < arr[j]){
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = insert_element;
    }
}

int main(){
    int arr[] = {29, 10, 14, 37, 13, 0};
    int n = 6;
    InsertionSort(arr, n);
    for (int i = 0; i < n; i++){
        cout << arr[i] << ' ';
    }
    return 0;
}