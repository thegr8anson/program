# include<stdio.h>

int main(){
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf("Original value: %d\n", num);
    int *ptr = &num;
    int **pptr = &ptr;
    **pptr = 10;
    printf("Value after pointer-to-pointer modification: %d", num);
    return 0;
}


