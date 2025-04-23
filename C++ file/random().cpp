#include <iostream>
#include <cstdlib>
using namespace std;

void showTenRand()
{
for(int i = 0; i < 10; ++i)
cout << rand() % 10 + 1 << " ";
cout << endl;
}


int main(){
cout << (float)rand() / RAND_MAX << endl;


showTenRand();
showTenRand();
srand(123);
showTenRand();
srand(123);
showTenRand();

return 0;
}

