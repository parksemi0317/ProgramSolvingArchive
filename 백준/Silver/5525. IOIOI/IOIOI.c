#include <stdio.h>

int main(void)
{
    int N, M;
    scanf("%d", &N);
    scanf("%d", &M);
    char inputStr[M + 1];
    scanf("%s", inputStr);

    int startIdxArr[1000000] = {
        0,
    };

    int startIdx = 0;
    char CHAR[2] = {'I', 'O'};
    for (int i = 0; i < M; i++)
    {
        if (inputStr[i] != CHAR[(i - startIdx) % 2])
        {
            if (inputStr[i] == CHAR[0])
            {
                startIdx = i;
                startIdxArr[i] = i;
            }
            else
            {
                startIdxArr[i] = -1;
                startIdx = i + 1;
            }
        }
        else
        {
            startIdxArr[i] = startIdx;
        }
    }


    int result = 0;
    for (int i = 0; i < M; i++)
    {

        int size = i - startIdxArr[i] + 1;
        if (inputStr[i] == CHAR[0] && (i - startIdxArr[i] + 1) >= N * 2 + 1)
        {
            result += 1;
        }
    }

    printf("%d", result);
}