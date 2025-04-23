#include <iostream>
using namespace std;
void f(int n){
    while(n > 0){
        if (n >= 10000000){
            cout << n / 10000000<< " kuti ";
            n %= 10000000;
        } else if (n >= 100000){
            cout << n / 100000 << " lakh ";
            n %= 100000;
        } else if (n >= 1000){
            cout << n / 1000 << " hajar ";
            n %= 1000;
        } else if (n >= 100){
            cout << n / 100 << " shata ";
            n %= 100;
        } else {
            cout << n << ' ';
            break;
        }
    }    
}

int main(){
    long long n;
    int case_num = 1;
    while (cin >> n){
        cout << "    " << case_num << ". ";
        if (n == 0){
            cout << 0 << endl;
            case_num += 1;
            continue;
        } else if (n >= 10000000){
            f(n / 10000000);
            cout << "kuti ";
            n %= 10000000;
        }
        f(n);
        cout << endl;
        case_num += 1;
    }
    return 0;
}