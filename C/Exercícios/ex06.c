#include <stdio.h>

int main() {

    float nota1, nota2, nota3;

    printf("Digite a primeira nota (Trabalho de Laboratório): ");
    scanf("%f", &nota1);

    printf("Digite a segunda nota (Avaliação semestral): ");
    scanf("%f", &nota2);

    printf("Digite a terceira nota (Exame final): ");
    scanf("%f", &nota3);

    nota1 = nota1 * 2;
    nota2 = nota2 * 3;
    nota3 = nota3 * 5;
    float media = (nota1 + nota2 + nota3)/10;

    if (media <= 5) {
        printf("A sua nota é E.");
    }
    else if (media >= 5 && media <= 6) {
        printf("A sua nota é D.");
    }
    else if (media >= 6 && media <= 7) {
        printf("A sua nota é C.");
    }
    else if (media >= 7 && media <= 8) {
        printf("A sua nota é B.");
    }
    else if (media >= 8 && media <= 10) {
        printf("Meus parabéns! A sua nota é A!");
    }

    return 0;
}