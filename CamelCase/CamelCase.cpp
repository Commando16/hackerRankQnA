#include<iostream>
#include<string>

using namespace std;

int main(){

    int count = 0;
    string s;
    
    cout<<"Enter the string-";
    cin>>s;
    for(int i = 0; i < s.length(); i++)
        if(( int(s[i])>=65 ) && ( int(s[i])<=90 ))
            count++;

    cout<<"The total number of words are - "<<count+1;

    return 0;
}


//done