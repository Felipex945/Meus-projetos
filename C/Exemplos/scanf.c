#include  <stdio.h>

int main(){

    int idade = 0;
    int ano = 0;
    printf("Valor inicial da idade e do ano: %d e %d.\n", idade, ano);

    printf("Digite uma idade: ");
    scanf("%d", &idade);
    
    printf("Digite um ano: ");
    scanf("%d", &ano);

    printf("Idade informada : %d.\n", idade);
    printf("ano informado: %d.\n", ano);
}