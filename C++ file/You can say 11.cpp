#include <iostream>
#include <string>
using namespace std;
int main(){
    string n;
    while(cin >> n){
        if (n == "0")
            break;
        int even = 0, odd = 0;
        for (int i = 0; i < n.length(); i++){
            if (i % 2 == 0)
                even += (n[i] - '0');
            else
                odd += (n[i] - '0');
        }
        if (abs(even - odd) % 11 == 0)
            cout << n << " is a multiple of 11." << endl;
        else
            cout << n << " is not a multiple of 11." << endl;
    }
    return 0;
}