#include <stdio.h>
#include <assert.h>
#include "myheader.h"


int main(void) {
	say_hello(10);
	good(5);
	int dt[5];

	for (int j = 0; j < 6; j++) {
		assert(j < 5);
		dt[j] = j;
	};

	printf("%d",dt[2]);
	return 0;
}


