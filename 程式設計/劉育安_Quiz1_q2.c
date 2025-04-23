# include<stdio.h>
int main(){
    int a, b, c;
    printf("Enter three integers:");
    scanf("%d""%d""%d", &a, &b, &c);
    int max, min, middle;
    if (a >= b && a >= c){
        max = a;
    } else if (b >= a && b >= c){
        max = b;
    } else {max = c;}
    if (a <= b && a <= c){
        min = a;
    } else if (b <= a && b <= c){
        max = b;
    } else {min = c;}
    middle = a + b + c - max - min;
    if (min + middle > max){
        if (a == b && b == c){
            printf("This is an equilateral triangle.");
        } else if (min == middle || middle == max){
            printf("This is an isosceles triangle.");
        } else {
            printf("This is a scalene triangle.");
        }
    } else {
        printf("Cannot form a valid triangle.");
    }
    return 0;
}