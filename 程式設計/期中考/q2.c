# include<stdio.h>
int is_palindrome(int num) {
    int rev = 0, temp = num;
    while (temp) {
        rev = rev * 10 + temp % 10;
        temp /= 10;
    }
    return rev == num;
}

int reverse_int(int num) {
    int rev = 0;
    while (num) {
        rev = rev * 10 + num % 10;
        num /= 10;
    }
    return rev;
}

int main() {
    int n;
    printf("Please enter a positive integer: ");
    scanf("%d", &n);

    int count = 0;
    printf("Numbers yielding reversible sum palindromes:\n");
    for (long long i = 10; i <= n; i++) {
        if (is_palindrome(i)) continue;
        long long rev = reverse_int(i);
        if (i < rev && is_palindrome(i + rev)) {
            printf("%d + %d = %d\n", i, rev, i + rev);
            count++;
        }
    }
    printf("Total count: %d\n", count);
    return 0;
}

    
