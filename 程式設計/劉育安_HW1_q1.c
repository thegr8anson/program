# include<stdio.h>
int main(){
    int n, count = 0;
    printf("Please enter a number: ");
    scanf("%d", &n);
    for (int i = 1; i <= n / 2; i++){
        int sum = 0;
        for (int j = i; j <= n / 2 + 1; j++){
            sum += j;
            if (sum == n){
                printf("%d to %d\n", i, j);
                count++;
            } else if (sum > n)
                break;
        }
    }
    printf("There are total %d set(s)", count);
    return 0;
}