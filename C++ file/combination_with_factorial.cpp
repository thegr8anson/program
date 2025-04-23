#include <iostream>
using namespace std;
int factorial(int n){
    if(n == 0)
        return 1;
    return n * factorial(n - 1);
}

int main(){
    int n, m;
    while (cin >> n >> m){  
        int answer;
        answer = factorial(n) / factorial(m) / factorial(n - m);
        cout << answer << endl;
    }
    return 0;
}

