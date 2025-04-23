#include<iostream>
using namespace std;
int main(){
    int n, m;
    while (cin >> n >> m){
        int matrix[100][100];
        // n列m行的矩陣
        // 從第一列開始依序輸入每行的元素
        for (int i = 0; i < n; i++){      // 列
            for (int j = 0; j < m; j++){  // 行
                cin >> matrix[i][j];
            }    
        }
        // 矩陣行列對調，[2][0] -> [0][2]
        // 從第一行開始依序輸出每列的元素
        // 2 * 3 的矩陣會變成 3 * 2 

        for (int i = 0; i < m; i++){        // 行
            for (int j = 0; j < n; j++){    // 列
                cout << matrix[j][i] << ' ';
            }
            cout << endl;
        }
    } 
    return 0;
}