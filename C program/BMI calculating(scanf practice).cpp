// BMI calculating 
#include <stdio.h>
#include <stdlib.h>
int main()
{
	int  Grade, Class, number;
	char Name[100];
	float Height, Weight;
	printf("This is a BMI calculator.\nPlease enter your grade,class,seat number,and name.\n");
	printf("(Please press ENTER after each data.)\n");
	printf("Grade:");
	scanf("%d",&Grade);
	printf("Class:");
	scanf("%d",&Class);
	printf("Seat number:");
	scanf("%d",&number);
	printf("Name:");
	scanf("%s",&Name);
	printf("Please enter your height (meter) and weight (kilogram).\n");
	printf("(Please press ENTER after each data.)\n");
	printf("Height:");
	scanf("%f",&Height);
	printf("Weight:");
	scanf("%f",&Weight);
	printf("Grade: %d\nClass: %d\nSeat number: %d\nName: %s\n",Grade,Class,number,Name);
	printf("Height: %3.2fm\nWeight: %3.2fkg\n",Height,Weight);
	printf("Your BMI is %3.2f.\n",Weight / (Height * Height));
	system("pause");
	return 0;
}
