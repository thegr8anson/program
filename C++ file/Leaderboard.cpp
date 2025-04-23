#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>

using namespace std;

typedef vector<int> ScoreVec;
typedef vector<string> NameVec;

void initialize_system(ScoreVec& scores, NameVec& names);
void display_items(const ScoreVec& scores, const NameVec& names);
void add_item(int newScore, string newName, ScoreVec& scores, NameVec& names);
void delete_item(int itemValue, ScoreVec& scores, NameVec& names);

void noninteractive_test();
void interactive_test();

const int NUM_SCORES = 5;

int main()
{
   interactive_test();
   // noninteractive_test();
   return 0;
}

void initialize_system(ScoreVec& scores, NameVec& names)
{
    for (int i = 0; i < NUM_SCORES; ++i)
    {
        scores.push_back(0);
        names.push_back("Anonymous");
    }
}

void display_items(const ScoreVec& scores, const NameVec& names)
{
    if (scores.size() != NUM_SCORES || names.size() != NUM_SCORES){
        cout << "Error! The size of score/name vector is not equal to " << NUM_SCORES << ".\n";
        exit(1);
    }
    cout << "The top five scores are: " << endl;
    for (int i = 0; i < NUM_SCORES; ++i)
    {
        cout << setw(4) << i+1 << ". "
             << setw(12) << names.at(i)
             << ", Score: " << scores.at(i) << endl;
    }
}

void add_item(int newScore, string newName, ScoreVec& scores, NameVec& names)
{
    // enter your code here
    if (newScore > scores.at(4)){
        for (int i = 0; i < 5; i++){
            if (newScore > scores.at(i)){
                scores.insert(scores.begin() + i, newScore);
                names.insert(names.begin() + i, newName);
                scores.pop_back();
                names.pop_back();
                break;
            }
        }
    }
}

void delete_item(int itemValue, ScoreVec& scores, NameVec& names)
{
    // enter your code here
    for (int i = 0; i < 5; i++){    
        if (itemValue == scores.at(i)){
            scores.erase(scores.begin() + i, scores.begin() + i + 1);
            names.erase(names.begin() + i, names.begin() + i + 1);
            scores.push_back(0);
            names.push_back("Anonymous");
            break;
        }    
    }
}

void noninteractive_test()
{
    ScoreVec scores;
    NameVec names;   
    initialize_system(scores, names);
    add_item(68, "Lily", scores, names);
    add_item(25, "Emma", scores, names);
    add_item(25, "Aria", scores, names);
    add_item(71, "Elizabeth", scores, names);
    display_items(scores, names);
    delete_item(25, scores, names);
    display_items(scores, names);
}

void interactive_test()
{
    ScoreVec scores;
    NameVec names;   
    initialize_system(scores, names);
    cout << "Enter commands (add, del, show, exit): " << endl;
    string command;
    cin >> command;
    while (command != "exit")
    {
        if (command == "add")
        {
            int score;
            string name;
            cin >> score >> name;
            add_item(score, name, scores, names);
        }
        else if(command == "del")
        {
            int score;
            cin >> score;
            delete_item(score, scores, names);
        }
        else if(command == "show")
        {
            display_items(scores, names);
        }
        else
        {
            cout << "Unknown command: " << command << endl;
        }
        cin >> command;
    }
}