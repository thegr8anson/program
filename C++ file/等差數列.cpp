#include <bits/stdc++.h>
using namespace std;
int main(){
int a1,an,d;
cin >> a1 >> an >> d;
if (d > 0){
    for (int i = a1; i <= an; i += d){
        cout << i << " ";
}
} else if (d == 0){
    cout << a1;
} else {
    for (int i = a1; i >= an; i += d){
        cout << i << " ";
    }
}
return 0;
}
