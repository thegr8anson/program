#include <bits/stdc++.h>
using namespace std;
int main() {
    int row;
    cin >> row;
    cout << "*" << endl;
    for (int i = 2; i < row; i++){
        cout << "*";
        for (int j = 2; j < i; j++){
            cout << " ";
        }
        cout << "*" << endl;
    }
    for (int i = 1; i <= row; i++){
        cout << "*";
    }
    return 0;
}
