#include "stdio.h"


int main(int argc, char const *argv[])
{
	/* code */
	int i;

	for (int i = 65; i < 65 + 26; i++)
	{
		printf("%c\t %d\n", (char) i, i );
	}
}