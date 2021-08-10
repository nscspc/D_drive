#include<stdio.h>
#include<stdlib.h>
#define NULL 0

typedef struct
{
    int number;
    struct l *next;
}node;

node *find(node *list,int key)
{
    if(key==list->number)
    {
        return list;
    }
    else
    {
        if(list->next->next==NULL)
            return (NULL);
        else
            find(list->next,key);
    }
}


int main()
{
    node *head;
    int key;
    node *new;
    int x;
    node *n1;

    printf("enter value of new item : ");
    scanf("%d",&x);
    
    printf("enter value of key item : ");
    scanf("%d",&key);

    if(head->number == key)
    {
        new=(node*)malloc(sizeof(node));
        new->number=x;
        new->next=head;
        head=new;
    }
    else
    {
        n1=find(head,key);
        if(n1==NULL)
        {
            printf("\nkey not found\n");
        }
        else
        {
            new=(node*)malloc(sizeof(node));
            new->number=x;
            new->next=n1->next;
            n1->next=new;
        }
    }

}
/*node *find(node *p,int a)
{
    if(a==p->number)
    {
        return p;
    }
    else
    {
        find(p->next,a);
    }
}*/