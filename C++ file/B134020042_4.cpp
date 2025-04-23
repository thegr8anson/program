#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
using namespace std;

const int NUMBER_QUIZZES = 6;
const int MAX_STUDENTS = 10;

void readStudentGrades(int studentGrades[][NUMBER_QUIZZES], int& numberStudents);
void setCoutPrecision(int numberPrecision);
void computeSemesterGrades(const int studentGrades[][NUMBER_QUIZZES], int numberStudents, double semesterGrades[]);
void displaySemesterGrades(const double semesterGrades[], int numberStudents);
int getEasyQuizNumber(const int studentGrades[][NUMBER_QUIZZES], int numberStudents);

int main()
{
  int numberStudents;
  int studentGrades[MAX_STUDENTS][NUMBER_QUIZZES] = {0};
  readStudentGrades(studentGrades, numberStudents);
  double semesterGrades[MAX_STUDENTS] = {0};

  int quizIndex = getEasyQuizNumber(studentGrades, numberStudents);
  cout << "Quiz number " << quizIndex << " is the easiest.\n";

  computeSemesterGrades(studentGrades, numberStudents, semesterGrades);
  displaySemesterGrades(semesterGrades, numberStudents);
  return 0;
}

void readStudentGrades(int studentGrades[][NUMBER_QUIZZES], int& numberStudents)
{
  cout << "Enter the number of students: ";
  cin >> numberStudents;
  cout << "Enter the scores for each student: ";
  for (int i = 0; i < numberStudents; ++i)
  {
     for (int j = 0; j < NUMBER_QUIZZES; ++j)
     {
        cin >> studentGrades[i][j];
     }
  }
}

void setCoutPrecision(int numberPrecision)
{
  cout.setf(ios::fixed);
  cout.setf(ios::showpoint);
  cout.precision(numberPrecision);
}

void displaySemesterGrades(const double semesterGrades[], int numberStudents)
{
  setCoutPrecision(1);
  cout << "Table of Semester Grades:" << endl;
  cout << "       ";
  for (int i = 0; i < numberStudents; ++i)
     cout << setw(6) << "Stud" << i+1;
  cout << endl;
  cout << "Grades:";
  for (int i = 0; i < numberStudents; ++i)
     cout << setw(7) << semesterGrades[i];
  cout << endl;
}

void computeSemesterGrades(const int studentGrades[][NUMBER_QUIZZES], int numberStudents, double semesterGrades[])
{
  // enter your code here
  int temp_array [numberStudents][NUMBER_QUIZZES];
  for (int i = 0; i < numberStudents; i++){
      for (int j = 0; j < NUMBER_QUIZZES; j++){
          temp_array[i][j] = studentGrades[i][j];    
      }
      sort (temp_array[i], temp_array[i] + 6);
  }
  for (int i = 0; i < numberStudents; i++){
      int sum = 0;
      for (int j = 1; j <= NUMBER_QUIZZES - 2; j++){
          sum += temp_array[i][j];
      }
      semesterGrades[i] = sum / 4.;
  }
  // update semesterGrades based on studentGrades
}

int getEasyQuizNumber(const int studentGrades[][NUMBER_QUIZZES], int numberStudents)
{
  // enter your code here
  int easiest_quiz, highest_total_scores = 0;
  for (int i = 0; i < NUMBER_QUIZZES; i++){
      int total_student_scores = 0;
      for (int j = 0; j < numberStudents; j++){
          total_student_scores += studentGrades[j][i];
      }
      if (total_student_scores > highest_total_scores){
          highest_total_scores = total_student_scores;
          easiest_quiz = i + 1;
      }    
  }
  return easiest_quiz;
}