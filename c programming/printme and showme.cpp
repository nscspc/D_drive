#include<stdio.h>

// user functions declaration.
printme(); // no return no argument.
void showme();

int main()
{
	printme(); // function call.
	showme();
	printme();
	printme();
}

//function defination.
void printme()
{
	// task performed.
	printf("printme function .\n");
	showme();
}

void showme()
{
	// task performed.
	printf("showme function .\n");
	
}
