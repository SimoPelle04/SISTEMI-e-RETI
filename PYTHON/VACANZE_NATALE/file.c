#include <stdio.h>
#include <stdlib.h>
/*Crea la procedura CRESCENTI(x,y,z) che fa in modo che in x finisca il minore dei 3
numeri, in z il maggiore e in y il numero rimanente.*/
int inserisciNum() {
    int n;

    printf("inserisci num");
    scanf("%d", &n);

    return n;
}

void scambio (int *a, int *b) {
    int temp;
    *a = temp;
    *a = *b;
    *b = temp;

}
void  CRESCENTI(int *x,int *y,int *z) {
    int temp;
    if(*x < *y && *x < *z) {
        if(*z < *y) {
            //scambio(&z,&y);
            temp = *z;
            *z = *y;
            *y = temp;
        }
    } else {
        if(*y < *x && *y < *z) {
            //scambio(&x,&y);
            temp = *x;
            *x = *y;
            *y = temp;
            if(*z < *y) {
                //scambio(&z,&y);
                temp = *z;
                *z = *y;
                *y = temp;
            }
        } else {
            //scambio(&z,&x);
            temp = *z;
            *z = *x;
            *x = temp;
            if(*z < *y) {
            //scambio(&z,&y);
                temp = *z;
                *z = *y;
                *y = temp;
            }
        }

    }

}

int main() {
    int x,y,z;

    x = inserisciNum();
    y = inserisciNum();
    z = inserisciNum();

    CRESCENTI(&x,&y,&z);

    printf("\n %d", x);
    printf("\n %d", y);
    printf("\n %d", z);
    return 0;
}
