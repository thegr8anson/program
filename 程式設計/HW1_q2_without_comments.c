# include<stdio.h>
# include<stdlib.h>

void rMatrix(int *arr, int n){
    for (int i = 0; i < n - 1; i++){
        for (int j = i + 1; j < n; j++){
            int tmp = *(arr + i * n + j);
            *(arr + i * n + j) = *(arr + j * n + i);
            *(arr + j * n + i) = tmp;
        }
    }
    printf("Rotated Matrix:\n");
    for (int i = 0; i < n; i++){
        for (int j = n - 1; j >= 0; j--)
            printf("%-4d", *(arr + i * n + j));
        printf("\n");
    }
}

int main(){
    int n;
    printf("Enter the matrix size n: ");
    scanf("%d", &n);
    int *arr = (int *)calloc(n * n, sizeof(int)); 
    printf("Original Matrix:\n");
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            *(arr + i * n + j) = 1 + i * n + j;
            printf("%-4d", *(arr + i * n + j));
        }
        printf("\n");
    }
    rMatrix(arr, n);
    free(arr);
    return 0;
}