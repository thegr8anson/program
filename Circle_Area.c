/*****************************************************************
This program calculates the area of the circle based on the radius 
determined by the user. Then, if the area is greater than or equal 
to 50, display "The circle's area is large". Otherwise, display 
"The circle's area is small".
*****************************************************************/
#include <stdio.h>
int main() {
    const float PI = 3.14159;  // Declare a float constant named PI with the value 3.14159.
    float radius; // Declare a float variable named radius.
    float area; // Declare a float variable named area.
    printf("Enter the radius of the circle: "); // Display "Enter the radius of hte circle: "
    scanf("%f", &radius); // Get the radius from the user.
    area = PI * radius * radius; // Calculate the area of the circle.
    // Determine whether the area is above or below 50.
    if (area >= 50) {
        printf("The circle's area is large.\n"); // Display "The circle's area is large." if area >= 50
    } else {
        printf("The circle's area is small.\n"); // Display "The circle's area is small." otherwise
    }
    printf("Variables declared: PI = %f, radius = %f, area = %f.", PI, radius, area); // Display variables declared.
    return 0; 
}

