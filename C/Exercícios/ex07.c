#include <stdio.h>

int main() {
    int soma_total = 0;
    int numero = 0;

    while(numero < 10) {
        numero += 1;
        soma_total += numero;
    }
    printf("A soma dos numeros entre 1 e 10 é: %d", soma_total);

    return 0;
}