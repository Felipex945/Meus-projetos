#include <stdio.h>

int main(){
    float altura;
    int idade;

    printf("Qual sua altura? ");
    scanf("%f", &altura);

    printf("Qual sua idade? ");
    scanf("%d", &idade);

    if (altura >= 1.60 && idade >= 13){
        printf("Você pode ir no brinquedo!\n");
    }
    
    else{
        printf("Você ainda não tem a idade ou altura suficientes!\n");
    }

    return 0;
}