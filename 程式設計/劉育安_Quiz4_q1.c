# include<stdio.h>
int main(){
    int studentIds[] = {101, 102, 103, 104, 105, 106, 107, 108, 109, 110};
    int scores[] = {85, 92, 78, 88, 95, 80, 87, 90, 83, 91};
    printf("Enter your student ID: ");
    int input;
    scanf("%d", &input);
    int i, index = -1;
    int scores_len = sizeof(scores) / sizeof(scores[0]);
    for (i = 0; i < scores_len; i++){
        if (studentIds[i] == input){
            index = i;
            break;
        }
    }
    if (index == -1)
        printf("The student ID is invalid.");    
    else
        printf("Your score is %d.", scores[index]);
    return 0;
}
