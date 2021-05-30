#include<iostream>
#include<vector>

using namespace std;

int main(){

    string alphabets[] = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
    int n;
    
    cout<<"Enter the size-";
    cin>>n;

    int rows = n+(n-1);
    int columns = rows+(rows-1);
    vector<string> patern_row;

    

    cout<<"no. of rows- "<<rows<<" no. of columns- "<<columns<<endl;

    for(int i=n-1; i>=0; i--)
    {
        string r = "";
        int j= n-1;
        for( ; j>=i; j-- )
        {
            r=r+alphabets[j]+"-";
        }
        j+=2;
        for( ;j <= n-1 ;j++)
        {
            r=r+alphabets[j]+"-";
        }

        int dash_count = ((columns - r.length())+1)/2;
        if( dash_count > 0){
            r = string(dash_count,'-')+r+string(dash_count-1,'-');
            patern_row.push_back(r);
        }
        else{
            patern_row.push_back(r.substr(0,r.length()-1));
        }
    }

    
    for(int i = 0 ; i < patern_row.size(); i++)
    {
        cout<<patern_row[i]<<endl;
    }
    for(int i =  (patern_row.size()-2); i >= 0; i--)
    {
        cout<<patern_row[i]<<endl;
    }


    return 0;

}


//done