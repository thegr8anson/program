#include <iostream>
#include <string>
#include <map>
using namespace std;
int main(){
    map<string, int> country;
    int n;
    cin >> n;
    cin.ignore(); // 若在cin後要使用getline()，要先使用cin.ignore()清空緩衝區的資料。
    cin.ignore(); // 此題因為網站實際上在行數n與字串資料中多了一個空行，因此才使用了第二個cin.ignore()。 
    for (int i = 1; i <= n; i++){
        string a, country_name = "";
        getline(cin, a);
        int index = 0;
        while (a[index] != ' '){
            country_name += a[index];
            index++;
        }
        country[country_name]++;
    }
    for (const auto& it : country) {
        cout << it.first << ' ' << it.second << "\n";
    }
    return 0;
}

