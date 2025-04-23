
#include <stdio.h>
#include <stdlib.h>
#define PERIMETER 100
int main()
{
	int length,width,area;
	printf("The perimeter of the rectangle is %d.\n",PERIMETER);
	printf("Please enter the length of the rectangle.\n");
	scanf("%d",&length);
	width=50-length;
	area=length*width;
	printf("perimeter=%d,length=%d,width=%d.\n",PERIMETER,length,width);
	printf("The area of the rectangle is %d.\n",area);
	system("pause");
	return 0;	
}
