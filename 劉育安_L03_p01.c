#include <stdio.h>

// Function to find the missing number in an array of size "size"
// The array contains numbers from 0 to size (inclusive), but one number is missing
int missingNumber(int arr[], int size) {
    // The sum of all numbers from 0 to size (inclusive) using arithmetic series formula
    int expectedSum = size * (size + 1) / 2;

    // Variable to store the actual sum of elements in the array
    int actualSum = 0;

    // Loop through the array and add up all the numbers
    for (int i = 0; i < size; i++) {
        actualSum += arr[i];
    }

    // The missing number is the difference between the expected sum and actual sum
    return expectedSum - actualSum;
}

int main() {
    // Example 1: array of 3 elements with one number missing from the range 0-3
    int nums1[] = {3, 0, 1}; // Missing 2

    // Example 2: array of 9 elements with one number missing from the range 0-9
    int nums2[] = {9, 6, 4, 2, 3, 5, 7, 0, 1}; // Missing 8

    // Calculate the number of elements in each array
    int size1 = sizeof(nums1) / sizeof(nums1[0]); // gives 3
    int size2 = sizeof(nums2) / sizeof(nums2[0]); // gives 9

    // Call missingNumber function and store the answer for each array in result1 & result2
    int result1 = missingNumber(nums1, size1);
    int result2 = missingNumber(nums2, size2);

    // Print rhe result for each array
    printf("nums1[]  :%d\n", result1); // Output should be 2
    printf("nums2[]  :%d\n", result2); // Output should be 8

    return 0;
}