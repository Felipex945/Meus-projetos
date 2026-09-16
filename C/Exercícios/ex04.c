#include <stdio.h>

int main(){
    float n1, n2;

    printf("Digite o primeiro número: ");
    scanf("%f", &n1);

    printf("Digite o segundo número: ");
    scanf("%f", &n2);

    if (n1 > n2)
    {
        printf("O número %2.f é maior que o número %2.f", n1, n2);
    }
    else if (n1 < n2)
    {
        printf("O número %2.f é maior que o número %2.f\n", n2, n1);
    }
    else if (n1 == n2)
    {
        printf("Os número %2.f e %2.f são iguais\n", n1, n2);
    }

    return 0;
}
