# include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int main(){
    int n, strongest_chain = -1;
    cin >> n;
    int chain[100], amount;
    for (int i = 1; i <= n; i++){
        cin >> amount;
        for (int j = 0; j < amount; j++){
            cin >> chain[j];
        }
        int value = 0;
        sort(chain, chain + amount);
        value = chain[0];
        if (value > strongest_chain){
            strongest_chain = value;
        }
    }
    cout << strongest_chain;
    return 0;
}