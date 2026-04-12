#include <stdio.h>

// 거듭제곱을 정수형으로 직접 계산 (오차 방지)
long long ipow(int exp) {
    long long res = 1;
    while (exp-- > 0) res *= 3;
    return res;
}

void printResult(long long len) {
    if (len == 1) {
        printf("-");
        return;
    }

    int next_len = len / 3;
    printResult(next_len);
    for (int i = 0; i < next_len; i++) {
        printf(" ");
    }

    printResult(next_len);
}

int main() {
    int N;
    while (scanf("%d", &N) != EOF) {
        printResult(ipow(N));
        printf("\n");
    }
    return 0;
}