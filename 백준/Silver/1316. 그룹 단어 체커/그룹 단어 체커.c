#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int checkGroupWord(char str[], int length)
{
	int checker[26];
	for (int i = 0; i < 26; i++)
	{
		checker[i] = -1;
	}
	for (int i = 0; i < length; i++)
	{
		if (checker[str[i] - 97] == -1)
		{
			checker[str[i] - 97] = i;
		}
		else
		{
			if (i > checker[str[i] - 97] + 1)
			{
				return 1;
			}
			else
			{
				checker[str[i] - 97] = i;
			}
		}
	}
	return 0;
}

int main()
{
	int n;
	scanf("%d", &n);

	char inputStr[100];
	int len;
	int counter = 0;
	for (int i = 0; i < n; i++)
	{
		scanf("%s", inputStr);
		len = strlen(inputStr);
		if (checkGroupWord(inputStr, len) == 0)
		{
			counter += 1;
		}
	}
	printf("%d", counter);
}