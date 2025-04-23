# include<stdio.h>
# include<stdbool.h>

int reverse(int n){
    int reverse_n = 0;
    while (n > 0){
        reverse_n *= 10;
        reverse_n += n % 10;
        n /= 10;
    }
    return reverse_n;
}

void rSumPalindrome(int n){
    int i, count = 0;
    for(i = 10; i <= n; i++){
        int reverse_i = reverse(i);
        long long sum = i + reverse_i;
        if (i < reverse_i && sum == reverse(sum)){
            printf("%d + %d = %d\n", i, reverse_i, sum);
            count++;
        } else
            continue;
    }
    printf("Total count: %d", count);
}

int main(){
    printf("Please enter a positive integer: ");
    int n;
    scanf("%d", &n);
    printf("Numbers yielding reversible sum palindromes:\n");
    rSumPalindrome(n);
    return 0;
}