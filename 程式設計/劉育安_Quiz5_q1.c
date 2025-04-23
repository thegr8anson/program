# include<stdio.h>
void reverseIntArray(int intArray[], int out[], int a_size){
    if (a_size <= 0)
        return;
    *out = *(intArray + a_size - 1);
    return reverseIntArray(intArray, out + 1, a_size - 1);
}

int main(){
    int intArray[] = {35, 23, 17, 2, 5, 11, 20 ,1};
    int a_size = sizeof(intArray) / sizeof(intArray[0]);
    int out[a_size];
    reverseIntArray(intArray, out, a_size);
    printf("Reversed array:\n");
    for (int i = 0; i < a_size; i++)
        printf("%d ", out[i]);
    return 0;
}