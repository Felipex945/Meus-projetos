#include <stdio.h>

int main(){
    int A, B, soma, subtr, multi, divi;

    printf("Digite o valor do primeiro número: ");
    scanf("%d", &A);
    printf("Digite o valor do segundo número: ");
    scanf("%d", &B);

    soma = A + B;
    subtr = A - B;
    multi = A * B;
    divi = A / B;

    printf("Resultados das operações:\n");
    printf("Soma: %d + %d = %d\n", A, B, soma);
    printf("Subtração: %d - %d = %d\n", A, B, subtr);
    printf("Mutiplicação: %d × %d = %d\n", A, B, multi);
    printf("Divisão: %d ÷ %d = %d\n", A, B, divi);
}