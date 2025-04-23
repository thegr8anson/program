#include <stdio.h>
#include <stdlib.h>
int main()
{
   int p,a,r,c;
   printf("Enter the number of candy and the number of people.\n");
   scanf("%d %d",&c,&p);
   r=c%p;
   printf("Remainder=%d\n",r);
   
   printf("(1) Remainder=0.(1:T,0:F):%d\n",r==0);	
   printf("(2) Remainder is odd.(1:T,0:F):%d\n",(r>0)&&(r%2!=0));
   printf("(3) Remainder is even.(1:T,0:F):%d\n",(r>0)&&(r%2==0));	
   system("pause"); 
   return 0;
}
