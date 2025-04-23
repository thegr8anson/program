#include <stdlib.h>
#include <stdio.h>
int main(){
    printf("Enter 5 integers: ");
    int numbers[5]; // Declare an integer array which can accommodate 5 integers.
    int i; // Declare an integer i for looping.
    int sum = 0; // Declare an integer sum to record the sum of the input numbers.
    for (i = 0; i < 5; i++){
        scanf("%d", &numbers[i]); // Allow the user to enter 5 integers.
        sum += numbers[i]; // Use sum to add up and record the input inegers.
    }
    char names[3][20]; // Declare an integer array which can accommodate 5 integers.
    printf("Enter 3 names: "); 
    for (i = 0; i < 3; i++)
        scanf("%s", names[i]); // Allow the user to enter 5 integers.
    printf("\n\n"); 
    printf("The sum of the numbers is: %d\n", sum); // Output the sum of the integers.
    printf("Names in reverse order: "); 
    for (i = 2; i >= 0; i--)
        printf("%s ", names[i]); // Output names in reverse order.
    printf("\n\n");
    printf("Memory addresses of integers:\n");
    for (i = 0; i < 5; i++)
        printf("numbers[%d]: %p\n", i, &numbers[i]); // Output the memory addresses where the numbers are stored.
    printf("\n\n");
    printf("Memory addresses of strings:\n");
    for (i = 0; i < 3; i++)
        printf("names[%d]: %p\n", i, &names[i][0]); // Output the memory addresses where the names are stored.
    printf("Variables declared:\n"); // Output the variables declared.
    printf("Integer array numbers[5], i = %d, sum = %d, 2D character array names[3][20].", i, sum);
    return 0;
}

