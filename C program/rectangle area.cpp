/*  Given the perimeter of a rectangle=100, enter the length of the rectangle and calculate its area.*/
#include <stdio.h>
#include <stdlib.h>
const int perimeter=100;
int length,width,area;
int main()
{
	printf("The perimeter of the rectangle is %d.\n",perimeter);
	printf("Please enter the length of the rectangle.\n");
	scanf("%d",&length);
	width=50-length;
	area=length*width;
	printf("perimeter=%d,length=%d,width=%d.\n",perimeter,length,width);
	printf("The area of the rectangle is %d.\n",area);
	system("pause");
	return 0;
}


