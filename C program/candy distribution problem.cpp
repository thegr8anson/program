#include <stdio.h>
#include <stdlib.h>
int main()
{
   int p,a,r,c;
   printf("Enter the number of people, candy per person, and remainder.\n");
   scanf("%d %d %d",&p,&a,&r);
   c=p*a+r;
   printf("(1) Total number of candies:%d\n",c);
   p=p+1;
   a=c/p;
   r=c%p;
   printf("(2) Assign %d candies to %d people.\n",c,p);	
   printf("Number of candy per person:%d\n",a);
   printf("Number of left candy:%d\n",r);	
   system("pause"); 
   return 0;
}
