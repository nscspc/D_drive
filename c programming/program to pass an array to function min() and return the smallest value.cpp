//program to pass an array to a function min() and return the smallest value.

#include<stdio.h>

int min(int [],int);

int main()
{
	int a[]={1,0,2,3,2};
	printf("smallest value in the array is : %d",min(a,5));
	
}

int min(int z[],int n)
{
	int r,s=z[0];
	for(r=0;r<n;r++)
	{
		if(s>z[r])//for smallest value ( > ) and for greatest value ( < )
		{
			s=z[r];
		}
	}
	return s;
}
 
