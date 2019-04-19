#include<iostream>
using namespace std;
int main()
{
    int n,i;
    int * p;
    int candles[i];
    p= new (nothrow) int[i];//dynamic memory allocation
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>candles[i];
    }
    int maxi = candles[0];
    for(int i=0;i<n;i++)
    {
        if(maxi < candles[i+1])
        {
            maxi = candles[i+1];
        }
    }
    int counts = 0;
    for(int i=0;i<n;i++)
    {
        if(maxi == candles[i])
        {
            counts ++;
        }

    }
    cout<<counts;
}
