/*
This is a program which outputs the designated texts and values to the user.
*/
#include <stdio.h> // Include the header file required for input-output functions.
int main(){  // Declare the main function.
    int age = 18;  // Declare variable age with the data type int and assign the value 18 to it. 
    float height = 1.62;  // Declare variable height with the data type float and assign the value 1.62 to it.
    char initial = 'A';  // Declare variable initial with the data type char and assign the value A to it.
    printf("Hello! My age is %d, my height is %.2f meters, and my initial is '%c'.", age, height, initial);
    // Output the sentence and fetch the data declared beforehand.
    return 0;  // End the program with exit code 0 if run successfully.
}        
