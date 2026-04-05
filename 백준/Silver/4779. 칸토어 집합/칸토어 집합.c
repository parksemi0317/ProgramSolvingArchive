#include <stdio.h>

void printResult(char* str, int startIdx, int size){
    if (size <= 1)
        return;
    
    printResult(str, startIdx, size/3);

    for(int i = 0 ; i <size/3 ; i++){
        str[startIdx+size/3+i] = ' ';
    }
    
    printResult(str, startIdx + size/3 * 2, size/3);
}

int main() {
    int N;

    while(scanf("%d", &N) != EOF){
        int len = 1;
        for(int i=0 ; i <N ; i++)
            len*=3;
        
        char str[len+1];
        for(int i= 0 ; i < len ; i++){
            str[i] = '-';
        }
        str[len] = '\0';
        
        printResult(str, 0, len);
        printf("%s\n", str);
    }
}