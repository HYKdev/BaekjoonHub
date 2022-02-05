#include<stdio.h>
int c = 0;
int arr[30008];
int shd[30008];
int cyc(int n1, int n2)
{
    arr[0] = n1;
    arr[1] = n2;
    while(1)
    {
        arr[c + 2] = arr[c] - arr[c + 1];
        if(arr[c + 2] < 0)
        {
            break;
        }
        c++;
    }
    return c + 2;
}
int main()
{
    int n, x, max = 0;
    scanf("%d", &n);
    for(int i = 0; i <= n; i++)
    {
        c = 0;
        x = cyc(n, i);
        if(max < x)
        {
            max = x;
            for(int i = 0; i < max; i++)
            {
                shd[i] = arr[i];
            }
        }
    }
    printf("%d\n", max);
    for(int i = 0; i < max; i++)
    {
        printf("%d ", shd[i]);
    }
}
