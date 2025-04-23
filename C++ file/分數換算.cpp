#include<iostream>
using namespace std;
int main(){
int n,m;
cin >> n >> m;
if (n%m == 0){
    cout << "整數 " << n / m;
}
if (n%m != 0){
    if(n < m){
        cout << "真分數 " << n << "/" << m;
    } else {
        cout << "帶分數 " << n/m << " " << n%m << "/" << m;
    }
}
return 0;
}
