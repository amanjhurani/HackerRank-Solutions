#include<iostream>
using namespace std;
int main()
{
    int due[3];
    int ret[3];
    for(int i=0;i<3;i++)
    {
        cin>>ret[i];
    }
    for(int i=0;i<3;i++)
    {
        cin>>due[i];
    }
    if(due[0]==ret[0] && due[1]==ret[1] && due[2]==ret[2])
    {
        cout<<"0";
    }
    else if(due[0]<ret[0] && due[1]==ret[1] && due[2]==ret[2])
    {
        int fine = 15*(ret[0]-due[0]);
        cout<<fine;
    }
    else if(due[1]<ret[1] && due[2]==ret[2])
    {
        int fine = 500*(ret[1]-due[1]);
        cout<<fine;
    }
    else if(ret[2]>due[2])
    {
        cout<<'10000';
    }
    else
    {
        cout<<"0";
    }
}
