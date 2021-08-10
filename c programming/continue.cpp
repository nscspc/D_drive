#include <stdio.h>
int main()
{
	int l;
	for(l=1;l<=10;l++)
	{
		if (l==5)/*if can be used without curly brackets if only one statement 
					is written in if condition otherwise if statement to be used is 
					more than one then curly brackets should be used.*/
		continue;/*break statement is a statement used with control statements for executing the loop according to the user.
				  :- continue statement do not able to execute the statements below it only when 
					the condition gets true and resumes the loop from starting.*/
		printf("%d\n",l);
	}
	return 0;
}
