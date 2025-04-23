#include<iostream>
#include<string>
using namespace std;
int main(){
    string n;
    getline(cin, n);
    cout << (int)n[0];
    for (int i = 1; i < n.length(); i++){
        cout << '_' << (int)n[i];
    }
    return 0;
}
