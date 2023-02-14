
#include<stdio.h>
#include<conio.h>
struct node
{
    int data;
    struct node *next;
    struct node *prev;
}*head=NULL,*temp,*previous;
int display();
int insertbeg();
int insertend();
int insertloc();
int deletebeg();
int deleteend();
int deleteloc();

void main()
{
    int c;
    while(1)
    {
        printf("\n Select the operation to be exicuted");
        printf("\n 1. Display\n 2. insert at beggining\n 3. insert at end\n 4. insert at specific location\n 5. Delete at beggining\n 6. Delete at end\n 7. Delete at specific location\n");
        printf("\n enter the choice : ");
        scanf("%d",&c);
        switch(c)
        {
        case 1:
            display();
            break;
        case 2:
            insertbeg();
            break;
        case 3:
            insertend();
            break;
        case 4:
            insertloc();
            break;
        case 5:
            deletebeg();
            break;
        case 6:
            deleteend();
            break;
        case 7:
            deleteloc();
            break;
        default:
            printf("\n Enter a valid choice. ");

        }
    }
}
int display()
{
    temp=head;
    while(temp->next!=NULL)
    {

        printf("%d->",temp->data);
        temp=temp->next;
    }
    printf("%d->NULL",temp->data);

}
int insertbeg()
{
    int x;
    printf("\nenter the value to be inserted : ");
    scanf("%d",&x);
    struct node *newnode=(struct node *)malloc(sizeof(struct node));
    newnode->data=x;
    if(head==NULL)
    {
        head=newnode;
        newnode->prev=NULL;
        newnode->next=NULL;
        printf("%d",x);
    }
    else
    {
        newnode->next=head;
        newnode->prev=NULL;
        head->prev=newnode;
        head=newnode;



    }

}
int insertend()
{
    int x;
    printf("\n enter the value to be inserted: ");
    scanf("%d",&x);
    struct node *newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=x;
    newnode->next=NULL;
    if (head==NULL)
    {
        head=newnode;
        newnode->prev=NULL;
        printf("%d",x);
    }
    else
    {
        temp=head;
        while(temp->next!=NULL)
        {
            temp=temp->next;

        }
        newnode->prev=temp;
        temp->next=newnode;

    }
}
int insertloc()
{
    int x,key;
    printf("\nenter the value to be inserted : ");
    scanf("%d",&x);
    printf("\n enter the location to be %d insereted : ",x);
    scanf("%d",&key);
    struct node*newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=x;
    if(head==NULL)
    {
        printf("the list is empty");
    }
    else
    {

        temp=head;
        while(temp->data!=key)
        {
            temp=temp->next;
        }
        if(temp->prev==NULL && temp->next==NULL)
        {
            temp->next=newnode;
            newnode->prev=temp;
            newnode->next=NULL;
            return 0;
        }
        else if (temp->next==NULL)
        {
            temp->next=newnode;
            newnode->prev=temp;
            newnode->next=NULL;
            return 0;
        }
        else
            newnode->prev=temp;
        newnode->next=temp->next;
        temp->next->prev=newnode;
        temp->next=newnode;

    }
}
int deletebeg()
{
    if (head==NULL)
    {
        printf("the list is empty");

    }
    else
    {
        temp=head;
        head=temp->next;
        temp->next->prev=NULL;
        free(temp);

    }
}
int deleteend()

{
    if(head==NULL)
    {
        printf("\nthe list is empty");
    }
    else
    {

        temp=head;
        while(temp->next!=NULL)
        {
            temp=temp->next;
        }
        temp->prev->next=NULL;
        free(temp);
    }
}
int deleteloc()
{
    int x;
    printf("\nenter the value to be the value deleted : ");
    scanf("%d",&x);
    if (head==NULL)
    {
        printf("the list is empty");
    }
    else
    {
       temp=head;
        while(temp->data!=x)
        {
            temp=temp->next;
            if (temp==NULL)
            {
                printf("element not found");
                return 0;
            }

    }
    if(temp->prev==NULL && temp->next==NULL)
            {

                head=NULL;
                free(temp);
                printf("NULL");

            }
            else if(temp->next==NULL)
            {
                temp->prev->next=NULL;
                free(temp);
            }
            else if(temp->prev==NULL)
            {
                temp->next->prev=NULL;
                head=temp->next;
                free(temp);
            }
        else
        {
            temp->prev->next=temp->next;
            temp->next->prev=temp->prev;
            free(temp);

        }

    }
}
