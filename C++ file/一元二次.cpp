#include <bits/stdc++.h>
using namespace std;
int main ()
{
int a,b,c,root_1,root_2;
cin >> a >> b >> c;
if (b*b-4*a*c >= 0){
    if (b*b-4*a*c > 0){
        root_1 = (-b+sqrt(b*b-4*a*c)) / (2*a);
        root_2 = (-b-sqrt(b*b-4*a*c)) / (2*a);
        cout << "Two different roots x1=" << root_1 << " , x2=" << root_2;
        }
    if (b*b-4*a*c == 0){
        root_1 = -b / (2*a);
        cout << "Two same roots x=" << root_1;
    }
} else {
    cout << "No real root";
}
return 0;
}
