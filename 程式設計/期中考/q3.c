#define MAX_WORD_LENGTH 50
#include <string.h>
#include <stdio.h>
#include <ctype.h>

// Helper function to remove punctuation from a word
void removePunctuation(char *word) {
    char *src = word, *dst = word;
    while (*src) {
        if (isalpha(*src) || isdigit(*src)) { // Keep only letters and digits
            *dst++ = *src;
        }
        src++;
    }
    *dst = '\0'; // Null-terminate the cleaned word
}

int longestWord(char *sentence) {
    int maxLen = 0, maxPos = -1, pos = 0; // Start position from 0
    char *token = strtok(sentence, " ");
    char cleanedWord[100];
    while (token) {
        strcpy(cleanedWord, token);
        removePunctuation(cleanedWord); // Clean the word of punctuation
        int len = strlen(cleanedWord);
        if (len > maxLen) {
            maxLen = len;
            maxPos = pos;
        }
        token = strtok(NULL, " ");
        pos++;
    }
    return maxPos;
}

int main() {
    char sentence[] = "There are 6 words in the sentence.";
    char copy[100];
    strcpy(copy, sentence);
    char original[100];
    strcpy(original, sentence);

    int pos = longestWord(copy);

    // Extract the longest word again using the position
    int current = 0; // Start position from 0
    char *token = strtok(sentence, " ");
    printf("Input: %s\n", original);
    while (token) {
        if (current == pos) {
            char cleanedWord[100];
            strcpy(cleanedWord, token);
            removePunctuation(cleanedWord); // Clean the word of punctuation
            if (strlen(cleanedWord) > MAX_WORD_LENGTH) {
                printf("The word is too long to be displayed.\n");
            } else {
                printf("\"%s\" is the longest word in the sentence.\n", cleanedWord);
            }
            printf("Position of the word: %d\n", current);
            break;
        }
        token = strtok(NULL, " "); // Move to the next word
        current++; // Increment the current position
    }
    return 0;
}