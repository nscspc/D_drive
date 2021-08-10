#include<stdio.h>
int main()
{
int l[100],g=1,i=1,x=4,y=0,z=x-1,b=4,c=1;
while(i<=x*x)
{
    if(g==1)
    {
        while(y<=z)//#0
        {
            l[y]=i;
            i+=1;
            y+=c;//#1234#11 15
        }
        y-=c;//#3 #15
    }
    else
    {
        while(y>=z)//#0
        {
            l[y]=i;
            i+=1;
            y+=c;//#1234#11 15
        }
        y-=c;//#3 #15
    }
    if(y==x-1)
    {
        c=b;//#
        y+=c;//7
        z=x*x-1;//15
        g=1;
    }
    else if(y==x*x-1)
    {
        c=-1;
        y=y+c;
        z=x*x-x+1;
        g=0;
    }
    else if(y==x*x-x+1)
    {
        c=-b;
        y+=c;
        z=x;
    }
    else if(y==x)
    {
        c=1;
        y+=c;
        z=2*x-2;
        g=1;
    }
    else if(y==2*x-2)
    {
        c=-1;
        y+=b;
        z=2*x+1;
        g=0;
    }
    else
    {
        break;
    }
}
int a=0;
i=0;
while(i<x*x)
{
    printf("%d ",l[i]);
    if(i==x+a-1)
    {
        printf("\n");
        a+=4;
    }
    i++;
}

    printf("\n\n%d",l[12]);
    
}
        
    

