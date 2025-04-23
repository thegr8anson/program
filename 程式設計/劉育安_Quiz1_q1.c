# include<stdio.h>
int cal_sum(int n){
    int i, sum = 0;
    for(i = 1; i <= n; i++){
        sum += i;
    }
    return sum;
}

int main(){
    int n, sum = 0; 
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    printf("%d", cal_sum(n));
    return 0;
}
