#include <bits/stdc++.h>
using namespace std;
int main()
{
long long int number;
for (number = 2; number <= 100; number++){
    bool flag = 1;
    for (int j = 2; j * j <= number; j++){
//砞﹚沧翴 j * j <= number 琌计ゲ﹚Θ蛮Θ癸珿盢计╊Θㄢい丁计穦琌腹numberτ礚阶赣计琌玡程计ゲ﹚才单腹number
        if (number % j == 0){
            flag = 0;
            break;
        }
    }
    if (flag)
        cout << number << " is a prime number.\n";
}
return 0;
}
