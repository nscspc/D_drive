#include<stdio.h>
#include<math.h>
int main()
{
	int sd,n,x,i;
	float arr[n],mean,sigma=0,root,q,r;
	printf("how many elements do you want to enter : ");
	scanf("%d",&n);
	printf("enter elements : \n");
	for(i=0;i<n;i++)
	{
		scanf("%f",&arr[i]);
	}
	i=0;
	while(i<n)
	{
		mean=mean+arr[i];
		i++;
	}
	mean=mean/n;
	i=0;
	do
	{
		sigma=sigma+(mean-arr[i])*(mean-arr[i]);
		i++;
	}while(i<n);
	
	/*root=0.1;
	while(root<=sigma/2)
	{
		q=sigma/root;
		r=sigma%root;
		if(q==0 && r==0)
		{
			break;
		}
		root=root+0.1;
	}*/
	
	printf("standard deviation is = %f",sqrt(sigma/n));
	
	return 0;
}
