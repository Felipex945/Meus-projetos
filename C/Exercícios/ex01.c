#include <stdio.h>

int main(){
    int n1, n2, n3, n4, soma;
    
    printf("Digite o primeiro número: ");
    scanf("%d", &n1);

    printf("Digite o valor do segundo: ");
    scanf("%d", &n2);

    printf("Digite o valor do terceiro: ");
    scanf("%d", &n3);

    printf("Digite o último: ");
    scanf("%d", &n4);

    soma = n1 + n2 + n3 + n4;

    printf("A soma dos quatro valores é %d\n", soma);

    return 0;
}