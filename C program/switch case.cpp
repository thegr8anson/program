
#include<stdio.h>
int main()
{
	int year,month,days;
	printf("Please enter year(>0 and <10000) and month(1~12).\n");
	scanf("%d %d",&year,&month);
	if(year<=0||year>=10000){
	printf("Error input, year must >0 and <10000!\n");
	return 0;
	}
	if(month<1||month>12){
	printf("Error input, month must be between 1 and 12!\n");
	return 0;
	}
	switch(month){
		case 1:
		case 3:
		case 5:
		case 7:
		case 8:
		case 10:
		case 12:	
		days=31;
		break;
		case 4:
		case 6:
		case 9 :
		case 11:
		days=30;
		break;
		case 2:
		days=29;
		break;
		}
	if(year%400==0){
		printf("Meet criteria 1\n.");
		printf("Year %d is a leap year.\n",year);
		}else if(year%4==0&&year%100!=0){
			printf("Meet criteria 2.\n");
			printf("Year %d is a leap year.\n",year);
			}else{
				printf("Year %d is not a leap year.\n",year);
			 if(month==2)
			 days=28;
			}
	printf("Month %d has %d days.\n",month,days);
	return 0;	
 } 
