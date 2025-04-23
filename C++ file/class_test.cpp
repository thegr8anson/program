#include <iostream>
#include <string>
using namespace std;


class country{
    public :
    country(string a);
    private:
    string country_name;
    int people;
    void check_new_country();
};
// country::country(string a){
//     country = a;
//     people = 1;
// }
country::country(string a) :
country_name(a), people(1)
{ check_new_country(); }

void country::check_new_country(){

}

int main(){
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++){
        string a;
        cin >> a;
        country data1("Taiwan");

    }
}