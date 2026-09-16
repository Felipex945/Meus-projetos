 #include <stdio.h>

int main(){
    float nota;
    printf("Digite a sua nota: ");
    scanf("%f", &nota);

    if (nota < 7.00){
        printf("Você não foi aprovado!\n");
    }
    else{
        printf("Parabéns, você foi aprovado!\n");
    }
    
}
