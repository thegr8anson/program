#include<iostream>
using namespace std;
int main(){
int n,m;
cin >> n >> m;
if (n%m == 0){
    cout << "��� " << n / m;
}
if (n%m != 0){
    if(n < m){
        cout << "�u���� " << n << "/" << m;
    } else {
        cout << "�a���� " << n/m << " " << n%m << "/" << m;
    }
}
return 0;
}
