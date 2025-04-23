#include <iostream>
using namespace std;
int factorial(int number){
    if (number == 0 || number == 1){
        cout << 1;
        return 1;
    }    
    cout << number << " * ";
    return number * factorial(number - 1);
}
int main(){
    int number, answer;
    while (cin >> number){
        cout << number << "! = ";
        answer = factorial(number);
        cout << " = " <<answer << endl;
    }
    return 0;
}
