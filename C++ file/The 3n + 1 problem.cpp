#include <iostream>
using namespace std;
int getcycle(int n){
    int cycle = 1;
    while (n != 1){
        cycle += 1;
        if (n % 2 == 1)
            n = 3 * n + 1;
        else 
            n /= 2;
    }
    return cycle;
}
int main(){
    int n, m;
    while (cin >> n >> m){
        int max_cycle = -1;    
        for (int i = min(n, m); i <= max(n, m); i++){
            int cycle = getcycle(i); 
            if (cycle > max_cycle)
                max_cycle = cycle;
        }
        cout << n << ' ' << m << ' ' << max_cycle << endl;
    }
    return 0;
}

