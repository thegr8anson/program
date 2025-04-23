
#include<stdio.h>
int main()
{
	int year;
	printf("Please enter year.(>0 and <10000)\n");
	scanf("%d",&year);
	if(year<=0||year>=10000){
	printf("Error input, year must >0 and <10000!\n");
	return 0;
	}
	if(year%400==0){
		printf("Meet criteria 1\n.");
		printf("Year %d is a leap year.\n",year);
		}else if(year%4==0&&year%100!=0){
			printf("Meet criteria 2.\n");
			printf("Year %d is a leap year.\n",year);
			}else{
				printf("Year %d is not a leap year.\n",year);
			}
		return 0;	
 } 
