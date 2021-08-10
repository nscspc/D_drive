#include<stdio.h>
int main()
{
	int a,b,c=1,i=0,n,fact=1,s,permutation,facts,l;
	//int arr[n],crr[n];
	printf("how many digit number do you want to enter : ");
	scanf("%d",&n);
	int arr[n],crr[n];
	while(i<n)
	{
		printf("enter number : ");
		scanf("%d",&arr[i]);
		i++;
	}
	/*printf("enter second number : ");
	scanf("%d",&b);
	printf("enter third number : ");
	scanf("%d",&c);*/
	
	for(i=1;i<=n;i++)
	{
		fact=fact*i;
	}
	for(i=0;i<n;i++)
	{
		s=0;
		if(i!=0)
		{
			for(b=0;b<l;b++)
			{
				if(arr[i]==crr[b])
				{
					s=1;
					break;
				}
			}
		}
		if(s==1)
		{
			continue;
		}
		
		for(a=0;a+i<n;a++)
		{
			if(arr[i]==arr[a+i])
			{
				c++;
			}		
			//crr[i]=arr[i];
		}
		crr[i]=arr[i];
		l++;
	}
	
	for(i=1;i<=c;i++)
	{
		facts=facts*i;
	}
	
	permutation=fact/facts;
	
	printf("permutations of the entered number is %d",permutation);
	
	
}
