#include <stdio.h>

int main(){
    float n1, n2, soma, subtr;
    int um_oudois;

    printf("Digite o primeiro número: ");
    scanf("%f", &n1);

    printf("Digite o segundo número: ");
    scanf("%f", &n2);

    printf("Digite 1 para somar, ou 2 para subtrair: ");
    scanf("%d", &um_oudois);

    soma = n1 + n2;
    subtr = n1 - n2;

    if (um_oudois = 1){
        printf("O número %.2f + %.2f = %.2f\n", n1, n2, soma);
    }
    else if (um_oudois = 2){
        printf("O número %.2f - %.2f = %.2f\n", n1, n2, subtr);
    }
    else{
        printf("Opção inválida!\n");
    }
    
    return 0;

}