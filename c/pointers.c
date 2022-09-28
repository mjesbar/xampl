#include<stdlib.h>
#include<stdio.h>
#include<stddef.h>


int main(void)		{

	int value = 10;
	int *pointer = &value;		/* this assignment store the memory location of the variable 'value' */
	printf("The pointer store the value: %d\n", *pointer);
	printf("The pointer to value: %p\n", (void*)pointer);
	printf("The value's address: %p\n", &value);
	printf("The pointer's address itself: %p\n", &pointer);		/* the pointer address is different to the value address due to
																		   they are not the same thing, the value is an integer value
																		   stored at somewhere on memory, and the pointer is another variable
																		   who store the place of memory the variable value is stored in.
																		   they cannot indeed occupy the same location on memory, the pointer
																		   is just beside of the value var, chasing it all the time, so that
																		   the pointer in itself is shifted a few bytes next to the value
																		   address allocation. */

	int pval = &value;
	int pptr = &pointer;
	int pd = pptr - pval;
	printf("Pointer shifting:\npointer: %p\n&value: %p, diff: %d", (void*)pptr, (void*)pval, pd);
}




