// This program checks whether a number is prime and prints the result.
#include <stdio.h>
#include <stdbool.h> // Include header file <stdbool.h> in order to declare and use boolean variables.
int main(){
    int number = 17; // Declare integer variable named number with the value 17.
    bool isPrime = true; // Declare a boolean variable named isPrime and initialize it to true.
    int i; // Declare an integer variable i for later use in the for loop.
    for(i = 2; i < number; i++){ // Create a loop that runs from 2 to number - 1, and i increases 1 each time. 
        if (number % i == 0){ // If number can be divided by i
            isPrime = false; //Set isPrime to false.
            break; // Then end the loop immediately.
        }
    }
    switch (isPrime){ // Create a switch () which will perform different tasks based on the value of isPrime.
        case true: 
            printf("The number is prime.\n");
            break; // If isPrime == true, display the above messages then exit switch statement.
        case false:
            printf("The number is not prime.\n");
            break; //If isPrime == false, display the above messages then exit switch statement.
    }
    printf("Variables declared: number = %d, isPrime = %d", number, isPrime); // Display variables declared.
    return 0;
}



