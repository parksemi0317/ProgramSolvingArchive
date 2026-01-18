#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>


void printPrime(int num) {
	if (num == 1) {
		return 0;
	}
	else{
		int j = (int)sqrt(num);
		for (int i = 2; i <= j; i++)
		{
			if (num % i == 0)
			{
				return 0;
			}
		}
		printf("%d\n", num);
	}
}

int main(void){

	int M, N;
	scanf("%d %d", &M, &N);
	for (int i = M; i <= N ; i++) {
		printPrime(i);
	}
	return 0;
}