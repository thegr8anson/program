#include<iostream>
using namespace std;

int main()
{
  char letter, symbol;
  int height, space_amount, space_count_1, space_count_2;
  cout << "Enter a letter (K or A),\nthe height (as an integer),\nand the symbol (such as o, x, or *): ";
  cin >> letter >> height >> symbol;

  switch(letter)
  {
    case 'k':
    case 'K':
        space_amount = space_count_1 = (height + 1) / 2 - 2;
        for(int i = 1; i < (height + 1) / 2; i++){
            cout << symbol;
            while (space_count_1 > 0){
                cout << ' ';
                space_count_1 --;
            }
            space_count_1 = space_amount - i;
            cout << symbol << endl;
        }
        cout << symbol << endl; //space_count =-1
        for(int i = 1 ; i < (height + 1) / 2; i++){
            cout << symbol;
            while (space_count_1 >= 0){
                cout << ' ';
                space_count_1 --;
            }
            space_count_1 += i;
            cout << symbol << endl;
        }
        break;
    case 'a':
    case 'A':
        space_amount = space_count_1 = space_count_2 = height;
        for (int i = 1; i < height; i++)
            cout << ' ';
        cout << symbol << endl;
        for (int i = 1; i < (height-1) / 2; i++){
            for (int t = 2; t < space_count_1; t++)
                cout << ' ';
            space_count_1 --;
            cout << symbol;
            for (int t = height; t >= space_count_2; t--) // height = 7, height - 1 =6 , t = t - 1
                cout << ' ';
            space_count_2 -= 2;
            cout << symbol << endl;
        }
        for (int i = 1; i <= (height - 1) / 2; i++)
            cout << ' ';
        for (int i = 1; i <= height; i++)
            cout << symbol;
        cout << endl;
        space_count_1 = space_amount;
        for (int i = 1; i <= (height-1) / 2; i++){ //到此正確
            for (int t = (height + 1) / 2 + 1; t < space_count_1; t++) //space_count_1 = 7
                cout << ' ';
            space_count_1 --;
            cout << symbol;
            for (int t = height; t >= space_count_2 - 2; t--) // height = 7, height - 1 = 6 , t = t - 1, space_count_2 = 3
                cout << ' ';
            space_count_2 -= 2;
            cout << symbol << endl;
        }
        break;
    default:
        cout << "Error! Unknown letter: " << letter << endl;
  }
  //記得刪註解
  return 0;
}
