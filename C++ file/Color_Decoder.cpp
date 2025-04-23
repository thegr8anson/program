#include<iostream>
#include<string>

using namespace std;
/*
 00   -> Red
 01   -> Green
 100  -> Blue
 1010 -> Pink
 1011 -> Orange
 */

int main()
{
string code;
cout << "Enter a sequence of bits: ";
cin >> code;
int i = 0;
while (i < code.length())
{
    // Enter your code here.
    // You can access each input character using either code[i] or code.at(i)
    if (code.at(i) == '0'){
        i++;
        if (code.at(i) == '0'){
            cout << "Red ";
        }
        else{
            cout << "Green ";
        }
    }
    else{
        i += 2;
        if(code.at(i) == '0'){
            cout << "Blue ";
        }
        else{
            i += 1;
            if(code.at(i) == '0'){
                cout << "Pink ";
            }
            else{
                cout << "Orange ";
            }
        }
    }
    i++;
}
cout << endl;
return 0;
}
