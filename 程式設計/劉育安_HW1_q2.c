# include<stdio.h>
// Include<stdlib.h> to perform dynamic memory allocation.
# include<stdlib.h>

void rMatrix(int *arr, int n){
    /* Transpose array: 行列互換，每次以第i列第i行開始交換，第i層需要(n - 1 - i)次(不含第i列第i行的元素)
       Fact: It still works if you set (i < n) and (j = i).
       It simply takes out the element at row i column i and puts it back to where it was. */  
    // i < n - 1 since the element at the bottom right(last row & column) doesn't need to change
    for (int i = 0; i < n - 1; i++){
        for (int j = i + 1; j < n; j++){
            // Store the value at the original position with tmp.
            int tmp = *(arr + i * n + j);
            // Replace the value with the one at the corresponding position.
            *(arr + i * n + j) = *(arr + j * n + i);
            // Replace the value at the corresponding position with tmp.
            *(arr + j * n + i) = tmp;
        }
    }
    printf("Rotated Matrix:\n");
    // Print each row in reverse order.
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
    // Create a dynamic array and initialize it with zeros.
    int *arr = (int *)calloc(n * n, sizeof(int)); 
    printf("Original Matrix:\n");
    // Fill the array and print it out simultaneously. 
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