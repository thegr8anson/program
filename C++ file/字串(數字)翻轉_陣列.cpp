#include <bits/stdc++.h>
using namespace std;
int main(){
    string n, m;
    cin >> n;
    int i = n.length() - 1;
    
    while (i >= 0){  
        m += (n.at(i));
        i--;         
    }
    int digit = 0;
    for (int j = 0; j < m.length(); j++){
        if (m[j] == '0'){
            digit++;
        } 
        else{
            break;
        }
    }
    if (digit != 0){
        if (digit == m.length()){
            m.erase(0, digit - 1);
        }
        else{
            m.erase(0, digit);
        }
    }
    cout << m;  
    return 0;
}    