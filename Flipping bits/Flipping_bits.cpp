#include<iostream>
#include<vector>
#include<string>
#include <bitset>

using namespace std;

long flippingBits(long n) {
    bitset<32> dec_to_binary(n); 
    //cout<<"binary converstion - "<<dec_to_binary<<endl;
    for(int i = 0; i < dec_to_binary.size(); i++)
    {
        dec_to_binary[i] = !dec_to_binary[i];
    }
    //cout<<"flipped binary will be - "<<dec_to_binary<<endl;
    //cout<<"decimal converstion - "<<dec_to_binary.to_ulong();
    return dec_to_binary.to_ulong();
}

int main(){

	long num = 4;
	cout<<flippingBits();

	return 0;
}

//done