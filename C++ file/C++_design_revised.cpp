#include<iostream>
using namespace std;

int main()
{
  char letter, symbol;
  int height;
  cout << "Enter a letter (K or A),\nthe height (as an integer),\nand the symbol (such as o, x, or *): ";
  cin >> letter >> height >> symbol;

  switch(letter)
  {
    case 'k':
    case 'K':
        for(int i = 1; i < (height + 1) / 2; i++){
            cout << symbol;
            for(int j = 1; j < (height + 1) / 2 - i ; j++)
                cout << ' ';
            cout << symbol << endl;
        }
        cout << symbol << endl;
        for(int i = 1 ; i < (height + 1) / 2; i++){
            cout << symbol;
            for(int j = i ; j > 1; j--)
                cout << ' ';
            cout << symbol << endl;
        }
        break;
    case 'a':
    case 'A':
        for (int i = 1; i < height; i++)
            cout << ' ';
        cout << symbol << endl;
        for (int i = 2; i <= (height-1) / 2; i++){
            for (int j = i; j < height; j++)
                cout << ' ';
            cout << symbol;
            for (int j = 2 * i; j > 3; j--)
                cout << ' ';
            cout << symbol << endl;
        }
        for (int i = 1; i <= (height - 1) / 2; i++)
            cout << ' ';
        for (int i = 1; i <= height; i++)
            cout << symbol;
        cout << endl;
        for (int i = 1; i <= (height - 1) / 2; i++){
            for (int j = (height + 1) / 2 + 1; j <= height - i; j++)
                cout << ' ';
            cout << symbol;
            for (int j = 3; j <= height + 2 * i; j++)
                cout << ' ';
            cout << symbol << endl;
        }
        break;
    default:
        cout << "Error! Unknown letter: " << letter << endl;
  }
  return 0;
}