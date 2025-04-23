#include<iostream>
using namespace std;

int main()
{
  int total,num50,num20,num10,num5,num1;
  cout << "Enter a EUR amount: ";
  cin >> total;
  num50 = total/50;
  num20 = total%50/20;
  num10 = (total-50*num50-20*num20)/10;
  num5 = total%10/5;
  num1 = total%5;
  cout << "The input corresponds to" << endl;
  cout << "$50 bills: " << num50 << endl;
  cout << "$20 bills: " << num20 << endl;
  cout << "$10 bills: " << num10 << endl;
  cout << " $5 bills: " << num5 << endl;
  cout << " $1 coins: " << num1 << endl;
  return 0;
}
