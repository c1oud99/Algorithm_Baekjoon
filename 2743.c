#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	char str[100] = { '\0' };
	scanf("%s", str);
	printf("%d", strlen(str));
	return 0;
}
