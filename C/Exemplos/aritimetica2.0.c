#include <stdio.h>

int main(){
    int dado = 10;
    printf("Dado antes do incremento: %d\n", dado);

    dado ++;
    printf("Depois do incremento: %d.\n", dado);

    dado --;
    printf("Depois do decremento: %d\n", dado);

    dado += 3;
    printf("Dado após o incremento de 3 unidades: %d\n", dado);

    dado -= 2;
    printf("Dado após decremento de 2 unidades: %d\n", dado);

    dado *= 10;
    printf("Dado após multiplicado por 10: %d\n", dado);

}