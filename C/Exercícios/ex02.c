#include <stdio.h>

int main(){
    float salario, percentual, aumento, novo_salario;

    printf("Digite o valor do salário: ");
    scanf("%f", &salario);

    printf("Digite o percentual de aumento: ");
    scanf("%f", &percentual);

    aumento = salario * (percentual/100);
    novo_salario = salario + aumento;

    printf("O valor do aumento é %.2f\n", aumento);
    printf("Valor do novo salário: %.2f\n", novo_salario);

    return 0;
}