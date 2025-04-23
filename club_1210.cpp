#include<iostream>
using namespace std;
int gcd(int a, int b){
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

void time_table(int i, int j){
    if (i == 1 and j == 1)
        cout << "1*1=1" << '\t';
    else if (i != 1 && j == 1){
        time_table(i - 1, 9);
        cout << endl;
        cout << i << '*' << j << '=' << i * j << '\t';
    } else {
        time_table(i, j - 1);
        cout << i << '*' << j << '=' << i * j << '\t';
    }
}
void BubbleSort(int n[], int i){

    
}

int main(){
    int a, b;
    cin >> a >> b;
    // cout << gcd(a, b);
    time_table(a, b);
    return 0;
}

