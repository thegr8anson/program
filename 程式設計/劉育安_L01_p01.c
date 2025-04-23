# include<stdio.h>
int main(){
    printf("請輸入菱形的大小");
    int n;
    // 讀取輸入
    scanf("%d", &n);
    // 宣告迴圈變數
    int i, j;
    // 使用多重迴圈繪製出上半部的圖形(空格、星號及換行)
    for (i = 1; i <= n; i++){
        for (j = 1; j <= n - i; j++)
            printf(" ");
        for (j = 1; j < i * 2; j++)
            printf("*");
        printf("\n");
    }
    // 使用多重迴圈繪製出下半部的圖形
    for (i = 1; i <= n; i++){
        for (j = 1; j <= i; j++)
            printf(" ");
        for (j = 1; j < n * 2 - i * 2; j++)
            printf("*");
        printf("\n");
    }
    return 0;
}