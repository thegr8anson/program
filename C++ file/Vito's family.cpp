#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    int number[500];
    for (int i = 1; i <= n; i++){
        int people;
        cin >> people;
        for (int j = 0; j < people; j++){
            cin >> number[j];
        }
        sort(number, number + people);
        int location = 0;
        if (people % 2 == 0){
            location = (number[people / 2 - 1] + number[people / 2]) / 2;
        } else{
            location = number[people / 2];
        }
        int sum = 0;
        for (int j = 0; j < people; j++){
            sum += abs(location - number[j]);
        }
        cout << sum << endl;
    }
    return 0;
}
