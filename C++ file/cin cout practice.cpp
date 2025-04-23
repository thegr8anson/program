/*
cin 的箭頭是>> (東西進來)
cout 的箭頭<< (東西出去)
若想輸入整數，並輸出小數，有以下兩種方法:
1.全部變數用float
2.乘除的數字改用.0
*/

#include<iostream>
using namespace std;
int main()
{         
int x,y;
float average;
cin>>x;
cin>>y;
average=(x+y)/4.00;
cout<<average<<endl; 
return 0;
}

