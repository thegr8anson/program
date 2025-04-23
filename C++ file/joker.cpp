#include <bits/stdc++.h>
using namespace std;
void Print_Array (int array[], int elements){
for (int i = 0; i < elements; i++){
    cout << array[i] << ' ';
}
}
int main()
{
/*string name
float height;
char adult;
cout << "請輸入你的姓名->";
cin >> name;
cout << "你的名字是" << name << endl;
cout << "請輸入你的年齡";
cin >> age;
cout << "你的年齡是" << age << endl;
cout << "請輸入你的身高";
cin >> height;
cout << "你的身高是" << height << endl;
cout << "請輸入你是否成年( Y/N 或 y/n )";
cin >> adult;
cout << "是否成年->" << adult << endl;*/
/*if (adult == 'Y' || adult == 'y') {
    cout << "去考駕照" << endl;
} else if(adult == 'N' || adult == 'n') {
    cout << "乖乖讀書" << endl;
} else {
    cout << "請依照指示輸入" << endl;
}*/
if (speed > 80){
    if (speed > 100){
    cout << "你趕著投胎是不是???";
    } else {
    cout << "你有點超速了喔";
    }
}
/*switch (adult){
    case 'Y' :
    case 'y' :
        cout << "去考駕照" << endl;
        break;
    case 'N' :
    case 'n' :
        cout << "乖乖讀書" << endl;
        break;
    default :
        cout << "請依照指示輸入" << endl;
        //若不加break,則當輸入Y or y時,會造成y和n的敘述都執行,輸入N or n時,則只執行n部分的敘述
}*/
/*char x = 6;
string name_1 = "Anson", name_2 = "王浚宇";
cout << static_cast<int>(x) / 3 << endl;
cout << 17 / 3. << endl;
cout << name_1 + name_2 << endl;
cout.precision(3);
cout << 17. / 3;*/
int number[5];
for (int i = 0; i < 5; i++){
    cin >> number[i];
}
/*for (int i = 0; i < 5; i++){
    cout << number[i] << ' ';
}*/
Print_Array (number, 5);
cout << endl;
int Max_Value = number[0];
for (int i = 0; i < 5; i++){
    if (number[i] > Max_Value){
        Max_Value = number[i];
    }
}
cout << Max_Value << endl;
cout << sizeof(number)<< endl;
cout << sizeof(number) / sizeof(number[0]) << endl;
sort(number, number + 5);
Print_Array (number, 5);

cout << endl;


int joker = 0;
for (int i = 1; i <= 10; i++)
    joker += 2.5;
cout << joker << endl;
int arr [3][4];
for (int i = 0; i < 3; i++){
    for (int j = 0; j < 4; j++){
        arr [i][j] = i * 2 + j;

    }
}
for (int i = 0; i < 3; i++){
    for (int j = 0; j < 4; j++){
        cout << arr [i][j] ;

    }
}







return 0;
}
