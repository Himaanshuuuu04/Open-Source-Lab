#include <stdio.h>

int main() {
    int num, reversed = 0;
    printf("Enter a 3-digit number: ");
    scanf("%d", &num);

    // Extract digits and reverse
    reversed = (num % 10) * 100 + ((num / 10) % 10) * 10 + (num / 100);

    printf("Reversed number: %d\n", reversed);
    return 0;
}