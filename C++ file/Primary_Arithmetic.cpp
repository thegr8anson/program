#include <iostream>
using namespace std;

int main(){
    int a, b;
    while(cin >> a >> b){
        if(a == 0 && b == 0)
            break;
        if (b > a){  // Set a as the bigger number. 
            int tmp = a;
            a = b;
            b = tmp;
        }
        int carry = 0;
        bool flag = false;
        while (a > 0){
            if (a % 10 + b % 10 + flag >= 10){
                carry += 1;
                flag = true;
            } else {
                flag = false;
            }
            a /= 10;
            b /= 10;
        }
        if (carry == 0)
            cout << "No carry operation." << endl;
        else if (carry == 1)
            cout << "1 carry operation." << endl;
        else
            cout << carry << " carry operations." << endl;        
    }        
    return 0;    
}