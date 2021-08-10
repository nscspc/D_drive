#include<stdio.h>
int main()
{
	int i,y,d,l,nod,m ,arr[7]={1,2,3,4,5,6,7};
	char days[7][20]
	{
		{"sunday"},
		{"monday"},
		{"tuesday"},
		{"wednesday"},
		{"thursday"},
		{"friday"},
		{"saturday"}
	};
	printf("enter date : ");
	scanf("%d",&d);
	printf("enter no. of month : ");
	scanf("%d",&m);
	printf("enter year : ");
	scanf("%d",&y);
	for(i=1;i<y;i++)
	{
	con:
	if(y%400==0)
	{
		l=1;
	}
	else if(y%100==0)
	{
		l=0;
	}
	else if(y%4==0)
	{
		l=1;
	}
	else
	{
		l=0;
	}
	if(y<y)
	if(l==1)
	{
		nod+=365;
	}
	else
	{
		nod+=366;
	}
	if(i==y)
		for(int j=1;j<m;j++)
		{
			if(j%2!=0)
			{
				nod+=31;
			}
			else if(j==2)
			{
				if(l==1)
				nod+=28;
				else
				nod+=29;
			}
			else
			{
				nod+=30;
			}
		}
	}
	
	nod+=d;
	for(i=0;i<7;i++)
	{int a=arr[i];
		for(int j=0;a<=nod;j+=7)
		{
			a+=7;
		}
		if(a==nod)
		break;	
	}
	printf("%d",arr[i]);
	/*for(int j=0;j<20;j++)
	printf("%c",days[i][j]);*/
	/*switch(i)
	{
		case 0:printf("sunday");break;
		case 1:printf("monday");break;
		case 2:printf("tuesday");break;
		case 3:printf("wednesday");break;
		case 4:printf("thursday");break;
		case 5:printf("friday");break;
		case 6:printf("saturday");break;
	}*/
	return 0;
	
}
