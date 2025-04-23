#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int option1(){
    printf("Enter starting integer (a): ");
    int a, b, i, sum = 0;
    scanf("%d", &a);
    printf("Enter ending integer (b): ");
    scanf("%d", &b);
    for (i = a; i <= b; i++){
        sum += i;
    }
    printf("Summation of numbers from %d to %d = %d\n", a, b, sum);
}

int option2(){
    printf("Enter starting integer (a): ");
    int a, b, i, product = 1;
    scanf("%d", &a);
    printf("Enter ending integer (b): ");
    scanf("%d", &b);
    for (i = a; i <= b; i++){
        product *= i;
    }
    printf("Product of numbers from %d to %d = %d\n", a, b, product);
}

int option3(){
    printf("Enter base (B): ");
    int B, E, i, result = 0;
    scanf("%d", &B);
    printf("Enter exponent (E): ");
    scanf("%d", &E);
    result = pow(B, E);
    printf("%d^%d = %d\n", B, E, result);
}

int main(){
while(true){
    printf("Menu:\n1. Compute Summation\n\
2. Compute Product\n\
3. Compute Power (Base^Exponent)\n\
4. Exit\n\
Enter your choice: ");
    int selected_option;
    scanf("%d", &selected_option);    
    if (selected_option == 1){
        option1();
    } else if (selected_option == 2){
        option2();
    } else if (selected_option == 3){
        option3();
    } else if (selected_option == 4){
        printf("Exiting program...");
        break;    
    } else {
        printf("Invalid input.\n");
    }
}
return 0;
}