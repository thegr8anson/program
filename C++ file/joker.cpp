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
cout << "�п�J�A���m�W->";
cin >> name;
cout << "�A���W�r�O" << name << endl;
cout << "�п�J�A���~��";
cin >> age;
cout << "�A���~�֬O" << age << endl;
cout << "�п�J�A������";
cin >> height;
cout << "�A�������O" << height << endl;
cout << "�п�J�A�O�_���~( Y/N �� y/n )";
cin >> adult;
cout << "�O�_���~->" << adult << endl;*/
/*if (adult == 'Y' || adult == 'y') {
    cout << "�h�Ҿr��" << endl;
} else if(adult == 'N' || adult == 'n') {
    cout << "�Ĩ�Ū��" << endl;
} else {
    cout << "�Ш̷ӫ��ܿ�J" << endl;
}*/
if (speed > 80){
    if (speed > 100){
    cout << "�A���ۧ�L�O���O???";
    } else {
    cout << "�A���I�W�t�F��";
    }
}
/*switch (adult){
    case 'Y' :
    case 'y' :
        cout << "�h�Ҿr��" << endl;
        break;
    case 'N' :
    case 'n' :
        cout << "�Ĩ�Ū��" << endl;
        break;
    default :
        cout << "�Ш̷ӫ��ܿ�J" << endl;
        //�Y���[break,�h���JY or y��,�|�y��y�Mn���ԭz������,��JN or n��,�h�u����n�������ԭz
}*/
/*char x = 6;
string name_1 = "Anson", name_2 = "���C�t";
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
