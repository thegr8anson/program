#include <iostream>
using namespace std;
void BubbleSort(int num_array[], int n){
    for (int i = 0; i < n; i++){
    // Loop through the array, bubbling the largest value to the end
        for (int j = 0; j <= n - 2; j++){
            if (num_array[j] > num_array[j+1]){
            // Swap adjacent elements if they are in the wrong order
                swap(num_array[j], num_array[j+1]);
            }
        }
    }
    for (int i = 0; i < n; i++)
        cout << num_array[i] << ' ';
}

int main(){
    int n;
    cin >> n;
    int num_array[n];
    for (int i = 0; i < n; i++)
        cin >> num_array[i];
    BubbleSort(num_array, n);
    return 0;
}