// ============================
// Question 4
// ============================
// Check if truncating the leftmost digit results in a divisor of the original number

#include <stdio.h>
#include <math.h>

int num_digits(int n) {
    int count = 0;
    while (n > 0) {
        count++;
        n /= 10;
    }
    return count;
}

int main() {
    int N;
    printf("Please enter a positive integer: ");
    scanf("%d", &N);

    if (N >= 100) {
        int count = 0;
        printf("The numbers that satisfy the truncated divisibility condition are:\n");
        for (int i = 100; i <= N; i++) {
            int digits = num_digits(i);
            int divisor = pow(10, digits - 1);
            int truncated = i % divisor;
            if (truncated != 0 && i % truncated == 0) {
                printf("%d / %d = %d\n", i, truncated, i / truncated);
                count++;
            }
        }

        if (count == 0)
            printf("No number satisfies the condition.\n");
        else
            printf("Total count: %d\n", count);
        
    } else
        printf("Input must be 100 or greater.\n");

    return 0;
}
