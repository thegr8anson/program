# include<stdio.h>
# include<math.h>
int processNumber(int n, int *reverse){
    int r_square; 
    while(n != 0){
        *reverse *= 10;
        *reverse += n % 10;
        n /= 10;
    }
    r_square = pow(*reverse, 2);
    return r_square;
}

int main(){
    int n, reverse = 0;
    printf("Enter a number: ");
    scanf("%d", &n);
    int result = processNumber(n, &reverse);
    printf("Reversed number: %d\n", reverse);
    printf("Square of reversed number: %d", result);
    return 0;
}