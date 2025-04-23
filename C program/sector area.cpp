
#include <stdio.h>
#include <stdlib.h>
#define PI 3.14159
int main()
{
	float radius,angle,area;
	printf("Please enter the radius and the degree of the sector:\n");
	scanf("%f %f",&radius,&angle);
	area=radius*radius*PI*angle/360;
	printf("The sector with radius:%f and angle:%f degree\n",radius,angle);
	printf("The area of the sector is %.2f\n",area);
	system("pause");
	return 0;
}
