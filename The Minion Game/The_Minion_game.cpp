#include<iostream>

using namespace std;

bool is_vowel( char s ){

    char vovel[] = {'a', 'e', 'i', 'o', 'u'};
    int flag = 0;
    for(int i = 0; i<5; i++){
        if( s == vovel[i]){   
            flag = 1;
            break;
        }
    }

    if( flag == 0 )
        return false;
    else
        return true;

}

int main(){
    
    string word = "Banana";

    int length = word.length();

    // Score for Stuart (consonent)
    long stuart = 0;
    for(int i=0; i<length; i++)
    {
        if(!is_vowel(word[i])){
            //cout<<length<<"-"<<i<<" ="<<length-i<<endl;
            stuart+=(length-i);
        }
    }

    // Score for Stuart (consonent)
    long kevin = 0;
    for(int i=0; i<length; i++)
    {
        if(is_vowel(word[i])){
            //cout<<length<<"-"<<i<<" ="<<length-i<<endl;
            kevin+=(length-i);
        }
    }

    if(stuart>kevin){
        cout<<"Stuart "<<stuart;
    }
    else if (kevin>stuart){
        cout<<"Kevin "<<kevin;
    }
    else{
        cout<<"Draw";
    }

    return 0;
}


//Done