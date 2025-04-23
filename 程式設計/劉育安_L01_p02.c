# include<stdio.h>
int gcd(int a, int b){
    // 由於輾轉相除法在過程中會改變到原本的數字，因此開新變數複製原本的a, b
    int x = a, y = b;
    // 利用輾轉相除法求最大公因數，除到最後不為0的數字就是答案
    while (y != 0){
        int temp = y;
        y = x % y;
        x = temp;
    }
    return x;
}
int main(){
    printf("Enter two numbers:\n");
    int a, b;
    // 讀取兩個整數輸入
    printf("a = ");
    scanf("%d", &a);
    printf("b = ");
    scanf("%d", &b);
    // 輸出原本的數字及結果
    printf("GCD(%d, %d) = %d", a, b, gcd(a, b));
    return 0;
}
