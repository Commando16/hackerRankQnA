#include<iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> serviceLane(int n, vector<int> width, vector<vector<int>> cases) {
    vector<int> result;
    
    for( int i = 0; i < cases.size(); i++){
        
        int min = 99999;

        //cout<<cases[i][0]<<"to"<<cases[i][1]<<endl;

        for(int j = cases[i][0]; j <= cases[i][1];  j++)
        {
            if( width[j] < min){
                min = width[j];
            }
        }
        
        cout<<min<<endl;
        result.push_back(min);
        
    }

    return result;
}


int main(){
    vector<vector<int>> cases = {
        {0, 3},
        {4, 6},
        {6, 7},
        {3, 5},
        {0, 7}
    };
    
    vector<int> width = { 2, 3, 1, 2, 3, 2, 3, 3};

    serviceLane(5, width, cases);

    return 0;
}


//Done