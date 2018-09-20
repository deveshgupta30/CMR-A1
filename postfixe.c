#define SIZE 50
#include<ctype.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int s[SIZE];
int top=-1;
void push(int elem)
{
	s[++top]=elem;
}
int pop()
{
	return(s[top--]);
}
void main()
{
	char pofx[50], ch;
	int i=0,op1,op2;
	printf("\nEnter Postfix Expression:");
	scanf("%s",pofx);
	while((ch=pofx[i++])!='\0')
	{
		if(isdigit(ch))
			push(ch-'0');
		else
		{
			op1=pop();
			op2=pop();
			switch(ch)
			{
				case '+':
					push(op1+op2);
					break;
				case '-':
					push(op1-op2);
					break;
				case '*':
					push(op1*op2);
					break;
				case '/':
					push(op1/op2);
					break;
			}
		}
	}
	printf("Given Postfix Expression:%s",pofx);
	printf("\nResult after evaluation:%d\n",s[top]);
}
	
