#include <stdio.h>
#define texto "Entrada e saída de dados"

int main(){
    printf("%s\n", texto);

    int idade = 0;
    float altura = 0.0;
    char nome[50] = "";

    printf("Digite sua idade: ");
    scanf("%d", &idade);

    printf("Digite seu altura: ");
    scanf("%f", &altura);

    printf("Digite seu nome: ");
    scanf("%s", &nome);

    printf("Os dados informados foram: \n");
    printf("Idade: %d anos\n", idade);
    printf("Altura: %.2fm\n", altura);
    printf("Nome: %s\n", nome);
}