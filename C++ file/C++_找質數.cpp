#include <bits/stdc++.h>
using namespace std;
int main()
{
long long int number;
for (number = 2; number <= 100; number++){
    bool flag = 1;
    for (int j = 2; j * j <= number; j++){
//�]�w���I�� j * j <= number �A�O�]���]�ƥ��w��������A�G�i�N�]�Ʃ��b�A�������]�Ʒ|�O�ڸ�number�A�ӵL�׸Ӧ]�ƬO�_�s�b�A�e�b�̤j���]�ƥ��w�ŦX�p�󵥩�ڸ�number
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
