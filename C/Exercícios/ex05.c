#include <stdio.h>

int main() {
    float n1, n2;
    int opcao;
    float soma, subtracao, multiplicacao, divisao;

    printf("Digite o primeiro numero: ");
    scanf("%f", &n1);

    printf("Digite o segundo numero: ");
    scanf("%f", &n2);

    soma = n1 + n2;
    subtracao = n1 - n2;
    multiplicacao = n1 * n2;
    divisao = n1 / n2;

    printf("[1] Somar\n");
    printf("[2] Subtrair\n");
    printf("[3] Multiplicar\n");
    printf("[4] Dividir\n");
    printf("Escolha uma das opcões acima: \n");
    scanf("%d", &opcao);

    if (opcao == 1) {
        printf("A soma entre os números é %2.f\n", soma);
    }
    else if (opcao == 2) {
        printf("A diferença entre eles é %2.f\n", subtracao);
    }
    else if (opcao == 3) {
        printf("Os dois multiplicados é igual a %2.f\n", multiplicacao);
    }
    else if (opcao == 4) {
        printf("A divisão entre os dois é %2.f\n", divisao);
    }
    else {
        printf("Opcao invalida!\n");
    }

    return 0;
}