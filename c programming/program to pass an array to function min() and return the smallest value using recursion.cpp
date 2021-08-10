//program to pass an array to a function min() and return the smallest value.

#include<stdio.h>

int min(int [],int,int);

int r=0;

int main()
{
	int a[]={1,4,2,3,2};
	printf("smallest value in the array is : %d",min(a,5,a[0]));
	
}

int min(int z[],int n,int s)
{
	if(s>z[r])//for smallest value ( > ) and for greatest value ( < )
	s=z[r];
	r++;
	n--;
	if (n!=0)
	{
		min(z,n,s);
	}
	return s;
}
 
