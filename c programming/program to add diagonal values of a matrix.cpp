#include <stdio.h>

int main() 
{
    int r,c,s=0;
    int arr[3][3];
    
    printf("enter value in 3*3 matrix : ");
    for(r=0;r<3;r++)
    {
        for(c=0;c<3;c++)
        {
            scanf("\n%d",&arr[r][c]);
            
        }
    }
    for(r=0;r<3;r++)
    {
        for(c=0;c<3;c++)
        {
            printf("%d ",arr[r][c]);
            
        }
        printf("\n");
    }
    for(r=0;r<3;r++)
    {
        for(c=0;c<3;c++)
        {
        	if (r==c)
			{
				s=s+arr[r][c];
			}
        }
    
    }
    printf("sum of 1diagonal values %d",s);
    return 0;
}
  
